.. include:: /substitutions.rst

.. The text of this page should be kept in sync with the README.md document in the
   top-level git project directory.

Welcome to |pydwf| !
====================

This is the documentation of |pydwf|, a Python package to control the Digilent Waveforms lineup of electronic test and measurement devices made by |Digilent|.

It wraps all functions of |libdwf|, the |low-level C library:link| provided by Digilent, in an easy-to-use, class-based Python API. Like the C library, the |pydwf| package supports Windows, Linux (Intel and ARM), and macOS.

The DWF library can be downloaded and installed from Digilent's website; see |installing-dwf-here:link| for details, including advice on how to avoid the annoying confirmation-by-email process that Digilent saw fit to implement in 2023.

The current release of |pydwf| is version |release|.
It is based on version |libdwf-version| of |libdwf|, but it should also work with other versions.

The |pydwf| package comes with documentation and a number of ready-to-run |examples:link| that demonstrate how |pydwf| can be used to perform common and not-so-common tasks.

A |command-line tool:link| is provided that can be used, among other things, to list the available Digilent Waveforms devices and their configurations.

This section contains information about the project. Readers who want to learn how to use |pydwf| are referred to the |API documentation:link|.

Supported devices
-----------------

The following devices can be controlled using |pydwf|:

* |Electronics Explorer:link| (legacy)
* |Analog Discovery:link| (legacy)
* |Analog Discovery 2:link|
* |Analog Discovery 3:link|
* |Digital Discovery:link|
* |Analog Discovery Studio:link|
* |DPS3340 Discovery:link|
* |Analog Discovery Pro 3x50:link| (3250 and 3450 models)
* |Analog Discovery Pro 5250:link| (a National Instruments VB-8012 rebranded as a Digilent device; Windows only)

The |pydwf| package has been extensively tested with the Analog Discovery 2, Digital Discovery, and ADP3450 devices. It should also work with the other devices listed, but these haven't been tested. If you have such a device and encounter problems, please report an issue on the `GitHub issue tracker <https://github.com/sidneycadot/pydwf/issues>`_.

Dependencies
------------

The |pydwf| package requires Python 3.6 or higher.

In order for |pydwf| to work, recent versions of the Digilent Adept and Digilent Waveforms packages must be installed. These provide the C libraries that |pydwf| uses to interact with devices. Generally speaking, if the Waveforms GUI application provided by Digilent works on your system, you're good to go.

|pydwf| depends on the |numpy:link| package to handle the considerable amount of data transferred between the PC and Digilent Waveforms devices when performing high-speed signal generation or capture operations.

Some of the |examples:link| depend on the |matplotlib:link| package, but |pydwf| itself will work without it.

Project hosting
---------------

The project repository and issue tracker are hosted on |GitHub|:

https://github.com/sidneycadot/pydwf/

Installation using |pip|
------------------------

The installable package is hosted on |PyPI|:

https://pypi.org/project/pydwf/

This allows installation using the standard |pip| (or |pip3|) tool:

.. code-block:: sh

   pip install pydwf

After installing |pydwf|, the following command will show the version of |pydwf| and the underlying DWF library:

.. code-block:: sh

   python -m pydwf version

The following command will list all Digilent Waveforms devices connected to the system and, for each of them, list the supported configurations:

.. code-block:: sh

   python -m pydwf list -c

Documentation
-------------

The project documentation is hosted on |Read the Docs|. The latest version can be reached via the following link:

https://pydwf.readthedocs.io/en/latest/

If desired, the documentation can also be installed locally after installing the package by executing the following command:

.. code-block:: sh

   python -m pydwf extract-html-docs

This will create a local directory called *pydwf-docs-html* containing the project documentation in HTML format.

Alternatively, a PDF version of the manual can be extract as well:

.. code-block:: sh

   python -m pydwf extract-pdf-manual

Examples
--------

The Python |examples:link| can be installed locally after installing the |pydwf| package by executing the following command:

.. code-block:: sh

   python -m pydwf extract-examples

This will create a local directory called *pydwf-examples* containing the Python examples that demonstrate many of the capabilities of the Digilent Waveforms devices and |pydwf|.

These examples are intended as a useful starting point for your own Python scripts. See the |examples overview:link| for more information.

Acknowledgements
----------------

Many thanks to Digilent for making the awesome Waveforms devices, and to provide not only the very capable *Waveforms* GUI software, but also the cross-platform SDK on which |pydwf| is based. Great work!

My company |Jigsaw B.V.| supported the effort to make |pydwf|. If you need any kind of high-tech software (with or without Digilent Waveforms devices), and you're somewhat in the vicinity of Delft, The Netherlands, |give us a call|.

Thanks to my longtime friend Pepijn for proof-reading the documentation and providing his perspective on several issues that came up while implementing |pydwf|. The package is a lot better because of your help.

Lastly, thanks to Petra for your patience with having all kinds of electronics equipment in the living room while developing this package (and before, and after, …). You may not share my enthusiasm for this particular hobby, but I am very fortunate that you are at least enthusiastic about my enthusiasm, if that makes sense.

*— SC*
