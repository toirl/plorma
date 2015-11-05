************
Introduction
************
What is Plorma
==============
Plorma is a webapplication to plan, organise and manage tasks in the software
development. Plorma is influenced by agile development methods like Scrum.
Tasks can be organised on Kanban boards and the progress of a sprint can be
visualized in a Burndown chart. 

Although Plorma is especially suited to support an agile software development
it tries to be as general as possible to be used in other fields of activity.

Licence
=======
Plorma is licensed under the GPL version 2 or later

Installation
============
Pip
---
Plorma is available from `Pypi <https://pypi.python.org/pypi/plorma>`_::

        pip install plorma
        plorma-admin app init myplorma
        cd myplorma
        # Adapt database connection etc in the created production.ini file.
        plorma-admin db init --config production.ini
        # Optionally install the demodata
        plorma-admin fixtures load --path /path/to/plorma/fixtures/demo --config production.ini
        # Finally start the server
        pserve --reload production.ini

Docker
------
A `Docker image <http://https://hub.docker.com/r/toirl/docker-plorma/>`_ including demo data can be started with::

        docker run -it -p 6543:6543 -d toirl/docker-plorma

From source
-----------
Please read the `REAME
<http://https://raw.githubusercontent.com/toirl/plorma/master/README.rst>`_
coming with the source of Plorma.

Get the source
==============
Plorma is hosted on `Github <https://github.com/toirl/plorma>`_::

        git clone https://github.com/toirl/plorma.git
