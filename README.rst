.. image:: https://travis-ci.org/jonDel/loggers.svg?branch=master
   :target: https://travis-ci.org/jonDel/loggers
   :alt: Travis CI build status (Linux)

.. image:: https://coveralls.io/repos/github/jonDel/loggers/badge.svg?branch=master
   :target: https://coveralls.io/github/jonDel/loggers?branch=master

.. image:: https://readthedocs.org/projects/loggers/badge/?version=master
   :target: http://loggers.readthedocs.io/en/latest/?badge=master
   :alt: Documentation Status

.. image:: https://landscape.io/github/jonDel/loggers/master/landscape.svg?style=flat
   :target: https://landscape.io/github/jonDel/loggers/master
   :alt: Code Health

.. image:: https://www.versioneye.com/user/projects/58233ff57a7295003aab5425/badge.svg?style=flat
   :target: https://www.versioneye.com/user/projects/58233ff57a7295003aab5425

.. image:: https://img.shields.io/pypi/v/loggers.svg
   :target: https://pypi.python.org/pypi/loggers/
   :alt: Latest PyPI version

loggers
===========

**loggers** is a Python library that provides usefull wrapper methods for logging class. To be used as a superclass for your own classes.


Example
--------------------

.. code:: python

  >>> from loggers import Loggers
  >>>
  >>> class spamClass(Loggers):
  ...   def __init__(self, logFolder=None):
  ...       super(spamClass, self).__init__('spamClass', logFolderPath=logFolder)
  ...   def do_stuff(self, arg):
  ...       if not type(arg) == str:
  ...         self.log.error("I was expecting a string. :( ")
  ...       else:
  ...         self.log.debug("I received my string. :)")
  ...
  >>> spam = spamClass('/tmp/logs/spamClass')
  >>> spam.log.error('ERROR')
  Log: ERROR | Log level:ERROR | Date:31/10/2016 16:51:47
  >>> spam.set_log_rotate_handler(True)
  >>> spam.do_stuff(123)
  Log: I was expecting a string. :(  | Log level:ERROR | Date:31/10/2016 16:51:47
  >>> spam.do_stuff('Eggs')
  >>> spam.set_log_level('DEBUG')
  Log: Changing log level to DEBUG | Log level:DEBUG | Date:31/10/2016 16:51:47
  >>> spam.do_stuff('Spam')
  Log: I received my string. :) | Log level:DEBUG | Date:31/10/2016 16:51:47

Installation
------------

To install loggers, simply run:

::

  $ pip install loggers

loggers is compatible with Python 2.6+

Documentation
-------------

https://loggers.readthedocs.io

Source Code
-----------

Feel free to fork, evaluate and contribute to this project.

Source: https://github.com/jonDel/loggers

License
-------

GPLv3 licensed.

