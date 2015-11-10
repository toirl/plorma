#!/usr/bin/env python
# encoding: utf-8

import poplib, email
import re
import argparse
import sqlalchemy as sa
from ringo.model.user import Profile, User
from ringo.scripts.admin import get_config_path
from ringo.scripts.db import get_session, get_appsettings
from plorma.views.tasks import _send_notification_mail, _add_user_to_nosy
from plorma.model.task import Task
from ringo_comment.model import Comment

def parse_message(message):
    subject = message["Subject"]
    email = message["Return-path"].strip("<>")
    for part in message.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))

        # skip any text/plain (txt) attachments
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)  # decode
            break
        # not multipart - i.e. plain text, no attachments, keeping
        # fingers crossed
        else:
            body = message.get_payload(decode=True)
    return subject, email, body

def parse_subject(subject):
    id, title = None, None
    # Try to find [ & ]
    p1 = subject.find("[")
    p2 = subject.find("]")
    if p1 > -1 and p2 > -1:
        tmpid = subject[p1+1:p2]
        id = re.findall("\D*(\d+)\D*",  tmpid)[0]
        title = subject[p2+1::].strip()
    else:
        title = subject
    return id, title

def get_user(email, db):
    try:
        profil = db.query(Profile).filter(Profile.email == email).one()
        return profil.user
    except Exception as e:
        print "User with email %s can not be identified: %s" % (email, e)
        return None

def get_task(id, db):
        try:
            task = db.query(Task).filter(Task.id == int(id)).one()
            return task
        except sa.orm.exc.NoResultFound:
            return None

def handle_message(message, db, settings):
    """Will handle the email message and add new or modifiy existings tasks.
    If the handling was successfull the function returns True other wise False.

    :message: email message
    :returns: True or False 

    """
    subject, email, body = parse_message(message)
    task_id, title = parse_subject(subject)
    user = get_user(email, db)
    if not user:
        return False
    if task_id:
        task = get_task(task_id, db)
        if task:
            # Add Comment
            comment = Comment()
            comment.text = body
            comment.uid = user.id
            comment.gid = user.default_gid
            task.comments.append(comment)
            db.flush()
            recipients = []
            for nuser in task.nosy:
                email = nuser.profile[0].email
                if email and user.id != nuser.id :
                    recipients.append(email)
            _send_notification_mail(task, recipients, settings)
            _add_user_to_nosy(task, user)
            db.commit()
            return True
        else:
            return False
    else:
        # Create Task
        task = Task()
        task.uid = user.id
        task.gid = user.default_gid
        task.name = subject

        # Add Comment
        comment = Comment()
        comment.text = body
        comment.uid = user.id
        comment.gid = user.default_gid

        task.comments.append(comment)
        _add_user_to_nosy(task, user)
        db.add(task)
        db.flush()
        db.commit()
        recipients = []
        for user in db.query(User).all():
            email = user.profile[0].email
            if email:
                recipients.append(email)
        _send_notification_mail(task, recipients, settings)
        return True

def retr_messages(mailbox):
    messages = []
    nummailboxessages = len(mailbox.list()[1])
    for i in range(nummailboxessages):
        try:
            messages.append(email.message_from_string("\n".join(mailbox.retr(i+1)[1])))
        except Exception as e:
            print e
    return messages

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Mail gateway command")
    parser.add_argument('--config',
                        default=get_config_path(),
                        metavar="INI",
                        help="Configuration file for the application")
    args = parser.parse_args()
    db = get_session(args.config, transactional=False)
    settings = get_appsettings(args.config)
    server = settings.get("mail.host")
    username = settings.get("mail.username")
    password = settings.get("mail.password")

    mailbox = poplib.POP3_SSL(server)
    mailbox.user(username)
    mailbox.pass_(password)
    for num, message in enumerate(retr_messages(mailbox)):
        handle_message(message, db, settings)
        mailbox.dele(num+1)
    mailbox.quit()
