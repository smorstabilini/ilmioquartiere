.. -*- coding: utf-8 -*-

=====================
 Emacs Support Files
=====================

:Date: $Date: 2007-12-03 21:04:09 +0100 (Mon, 03 Dez 2007) $

This directory contains the following Emacs lisp package files:

* rst.el: Emacs support for reStructuredText_.  This file contains a
  major mode that provides:

  * Section decoration/adornment creation and updating (M. Blais);
  * Table-of-contents mode and insertion (M. Blais);
  * Font-lock syntax highlighting (S. Merten);
  * Some handy editing functions (D. Goodger).
  * Some functions for converting rest documents from within emacs (M. Blais).  

* tests subdirectory: automated tests for some of the features in rst.el.
  Please make sure the tests pass if you change the LISP code.  Just type "make"
  to run the tests.

To install the package, put a copy of the package file in a directory on your
``load-path`` (use ``C-h v load-path`` to check).

For setup and usage details, see `Emacs Support for reStructuredText
<../../../docs/user/emacs.html>`_.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
