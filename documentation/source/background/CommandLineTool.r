.. include:: /substitutions.rst

Using |pydwf| as a command line tool
====================================

After installation, the |pydwf| package itself can by executed as a command line tool:

.. code-block::

   $ python3 -m pydwf

This tool provides a number of sub-commands:

version
  Show the version of the |pydwf| package and the DWF C library.

list
  List all available Digilent Waveforms devices. Add the option '-c' to show the supported configurations for each device.

extract-examples
  Extract a local directory with example Python scripts.

extract-html-docs
  Extract a local directory with the HTML documentation.

extract-pdf-manual
  Extract the documentation as a PDF file.

The command line tool will output help if the '-h' command line option is provided. Below, the output of the generic help is shown.

.. code-block::

   $ python3 -m pydwf -h
   usage: python -m pydwf [-h] {version,list,ls,extract-examples,extract-html-docs} ...

   Utilities for the pydwf package.

   positional arguments:
     {version,list,ls,extract-examples,extract-html-docs}
       version             show version of pydwf and the DWF library
       list (ls)           list Digilent Waveform devices
       extract-examples    extract pydwf example scripts to 'pydwf-examples' directory
       extract-html-docs   extract pydwf HTML documentation to 'pydwf-html-docs' directory
       extract-pdf-manual  extract pydwf PDF manual in current directory

   optional arguments:
     -h, --help            show this help message and exit

To get help for a specific sub-command, specify the sub-command in question followed by the '-h' command line option.
