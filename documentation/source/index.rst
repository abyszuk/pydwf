.. include:: /substitutions.rst

pydwf |release| — Table of Contents
===================================

.. Note: in the 'latexpdf' rendering, the title above will appear nowhere;
   but it needs to be present, otherwise the title of the first chapter will not appear (?!?).

   Strange Sphinx behavior:

     In the HTML rendering, this page WILL appear, so we put a proper title and a ToC.

.. Some comments on formatting:

   Useful links for reStructuredText usage:

       https://docutils.sourceforge.io/rst.html
       https://docutils.sourceforge.io/docs/ref/rst/directives.html

       https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

   Header levels used in the documentation:

       ########## with overline for parts
       ********** with overline for chapters
       ==========               for sections      <----- we use this level for page headers, and levels below.
       ----------               for subsections
       ^^^^^^^^^^               for subsubsections
       """"""""""               for paragraphs

.. More strange Sphinx behavior:
   The depth of the toctree below is used in the PDF document, but not in the HTML version.

.. toctree::
   :caption: Introduction

   /welcome

.. toctree::
   :caption: The pydwf package
   :maxdepth: 2

   /pydwf_api/pydwf_overview
   /pydwf_api/DwfLibraryToC
   /pydwf_api/DwfDeviceToC
   /pydwf_api/pydwf_exceptions
   /pydwf_api/pydwf_enumeration_types
   /pydwf_api/pydwf_utilities

.. toctree::
   :caption: Background information

   /background/CommandLineTool
   /background/Triggering
   /background/DeviceParameters
   /background/DigilentWaveformsDevices
   /background/C_Library
   /background/Examples
