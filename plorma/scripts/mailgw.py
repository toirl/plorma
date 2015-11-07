#!/usr/bin/env python
# encoding: utf-8

import poplib, email
import re
import argparse
from ringo.model.user import Profile
from ringo.scripts.admin import get_config_path
from ringo.scripts.db import get_session, get_appsettings
from plorma.model.task import Task

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
    return id, title

def get_user(email, db):
    try:
        profil = db.query(Profile).filter(Profile.email == email).one()
        return profil.user
    except:
        print "User can not be found"
        return None

def get_task(id, db):
    try:
        #task = db.query(Task).filter(Task.id == id).one()
        task = None
        return task
    except:
        print "Task can not be found"
        return None

def handle_message(message, db):
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
            print "Modifying task"
    else:
        task = Task()
        task.uid = user.id
        task.name = subject
        db.add(task)
        db.flush()
        print "Creating new task %s" % task
    db.commit()


def get_messages(server, user, password):
    mailbox = poplib.POP3_SSL(server)
    mailbox.user(username)
    mailbox.pass_(password)
    return retr_messages(mailbox)
    mailbox.close()

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

    for message in get_messages(server, username, password):
        handle_message(message, db)
