Limitations
===========

`Interwiki links`_ (e.g. ``w:``) are not supported.
Neither do fragments (e.g. ``#Foo``).

An interwiki :class:`Title <.title.Title>` cannot be resolved
completely, since there is no way to know what the other
wiki's namespace configurations are.

A title is supposed to represent an "address" or a "path",
not the real page. That said, the fragment is not considered
a part of a title. However, the parser will strip out the
fragment part, if any.

Note that :meth:`Title.fragments <.title.Title.fragments>` returns something entirely
different: a list of strings created by splitting the title
by ``/``.


.. _Interwiki links: https://www.mediawiki.org/wiki/Manual:Interwiki