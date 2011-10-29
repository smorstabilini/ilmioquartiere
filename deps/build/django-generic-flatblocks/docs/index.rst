.. index:

Welcome to django-generic-flatblocks's documentation!
=====================================================

If you want to add tiny snippets of text to your site, manageable by the admin
backend, you would use either `django-chunks`_ or `django-flatblocks`_.
However, both of them have one problem: you are limited to a predefined
content field; a "text" field in chunks and a "title" and "text" field in
flatblocks.

django-generic-flatblocks solves this problem as it knows nothing about the 
content itself. You *attach* your hand made content node (a simple model) where
you can define any fields you want.

.. _`django-flatblocks`: http://github.com/zerok/django-flatblocks/tree/master
.. _`django-chunks`: http://code.google.com/p/django-chunks/

Contents:

.. toctree::
   :glob:
   
   index
   installation
   configuration
   ref/usage
   ref/creating_nodes
   ref/contributed_nodes
   changelog