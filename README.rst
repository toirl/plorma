plorma README
==================
Plorma is a webapplication to **pl**an, **or**ganise and **ma**nage tasks.
While it tries to be as generic as possible it can be esspecially used as a
simple issue or bug tracker in software development.

**Warning**: Plorma is in a very early development stage. Do not use it in
productional environments!

Getting Started
---------------

- cd <directory containing this file>

- $venv/bin/python setup.py develop

- $venv/bin/plorma-admin db init

- $venv/bin/plorma-admin fixtures load

- $venv/bin/pserve development.ini

Test Users
----------
The following test users are available

===== ======== ============
Login Password Role
===== ======== ============
admin secret   admin
dave  dave     developer
peter peter    productowner
===== ======== ============
