.. Sphinx index.rst


MWTP v\ |version| documentation
===============================

:mod:`mwtp` is a parser for `MediaWiki`_ titles which relies on
information provided by user (`dependency injection`_) instead of
using hard-coded data. Currently it only supports Python 3.11
and later.

It is authored and maintained by `NguoiDungKhongDinhDanh`_
(a.k.a. NDKDD). Please direct any suggestions and bug
reports `to GitHub`_.


.. _MediaWiki: http://www.mediawiki.org
.. _dependency injection: https://en.wikipedia.org/wiki/Dependency_injection
.. _NguoiDungKhongDinhDanh: https://meta.wikipedia.org/wiki/User:NguoiDungKhongDinhDanh
.. _to GitHub: https://github.com/NguoiDungKhongDinhDanh/mwtp


Installation
------------

Since we are talking about Python packages, the only sane way
to install ``mwtp`` is to use |pip|_:

.. code-block:: console

   $ pip install mwtp


.. |pip| replace:: ``pip``
.. _pip: https://pypi.python.org/project/pip


.. toctree::
   :caption: Contents:
   :maxdepth: 2

   Usage <usage>
   Limitations <limitations>
   API references <api>


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
