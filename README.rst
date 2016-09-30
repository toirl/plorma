Plorma README
=============
Plorma is a web application to plan, organise and manage tasks in the software
development. Plorma is influenced by agile development methods like Scrum.
Tasks can be organised on Kanban boards and the progress of a sprint can be
visualized in a Burndown chart. 

Although Plorma is especially suited to support an agile software development
it tries to be as general as possible to be used in other fields of activity.

Licence
-------
Plorma is licensed under the GPL version 2 or later

Get the source
--------------
Plorma is hosted on `Github <https://github.com/toirl/plorma>`_::

        git clone https://github.com/toirl/plorma.git

Documentation
-------------
Documentation is available here: `Plorma documentation
<http://plorma.readthedocs.org>`_

Getting Started
---------------
The following steps will show how to get a running Plorma application when
starting with the source of Plorma.
An alternative way to setup Plorma when installing it per pip is described in
the User documentation.

Install a development environment and activate the devopment environment. More
information on how to setup a development environment can be found in the
`Ringo documentation <http://ringo.readthedocs.io/en/latest/start.html#installation>`_::

        curl -O https://raw.githubusercontent.com/ringo-framework/ringo/master/bootstrap-dev-env.sh
        sh bootstrap-dev-env.sh -c https://github.com/toirl/plorman.git plorma
        cd plorma
        source env/bin/activate

The get Plorma up and running do::

        cd <directory containing this file>
        python setup.py develop
        plorma-admin db init

The following steps are optional and only needed if you want to have some demo
data to play around::

        plorma-admin fixtures load --path plorma/fixtures/demo
        plorma-admin db fixsequence

Finally start the server::

        pserve development.ini

Testuser
--------
In case you installed the demo data the following users are available.

- Admin: Login: admin Passwort: secret
- Productowner: Login: peter Passwort: peter
- Developer: Login: dave Passwort: dave

The admin user is available even if you did not install the demo data. Use this
user to setup your application.
