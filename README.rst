plorma README
=============
Plorma is a webapplication to plan, organise and manage tasks. While it tries to be as generic as possible it can be especially used as a simple issue or bug tracker in software development.

Prerequisites
-------------
Plorma requires a PostgreSQL database. The default database (configured in the
ini file) is named plorma. Please make sure this database is created and
accessible before invoking the following commands.

Getting Started
---------------

- cd <directory containing this file>

- $venv/bin/python setup.py develop

- $venv/bin/plorma-admin db init

The following steps are optional and only needed if you want to have some demo
data to play around.

- $venv/bin/plorma-admin fixtures load --path plorma/fixtures/demo

- $venv/bin/plorma-admin db fixsequence

Finally start the sperver

- $venv/bin/pserve development.ini

Testuser
--------

- Admin: Login: admin Passwort: secret
- Productowner: Login: peter Passwort: peter
- Developer: Login: dave Passwort: dave