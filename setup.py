#!/usr/bin/env python
# encoding: utf-8

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES')).read()

requires = [
    'psycopg2',
    'ringo',
    'ringo_comment',
    'ringo_tag',
    'pygal'
]

setup(name='plorma',
      version='0.3',
      description=('Plorma is a task management application to plan '
                   'organise and manage your tasks.'),
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Torsten Irländer',
      author_email='torsten@irlaender.de',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='plorma',
      setup_requires=["hgtools"],
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = plorma:main
      [console_scripts]
      plorma-admin = ringo.scripts.admin:main
      [babel.extractors]
      tableconfig = ringo.lib.i18n:extract_i18n_tableconfig
      formconfig = formbar.i18n:extract_i18n_formconfig
      """,
      message_extractors = {'plorma': [
            ('**.py', 'python', None),
            ('templates/**.html', 'mako', None),
            ('templates/**.mako', 'mako', None),
            ('views/**.xml', 'formconfig', None),
            ('views/**.json', 'tableconfig', None),
            ('static/**', 'ignore', None)]},
      )
