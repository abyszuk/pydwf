.. include:: /substitutions.rst

The |DwfLibrary| class
======================

The |DwfLibrary| class is the entry point to all |pydwf| functionality. Most importantly, it is needed to obtain |DwfDevice| instances.

Using the |DwfLibrary| class
----------------------------

The |DwfLibrary| class is defined in the |pydwf.core.dwf_library| module. The top-level |pydwf| package imports it from that module to make it available to user scripts. To use the |DwfLibrary:link| class, you should import it from the top-level |pydwf| package and create an instance:

.. code-block:: python

   from pydwf import DwfLibrary

   dwf = DwfLibrary()

   print("DWF library version:", dwf.getVersion())

After instantiating a |DwfLibrary|, you can use the handful of methods the instance provides. These methods are documented as part of the |DwfLibrary:link| class in the next section.

Three attributes are provided to access particular sub-APIs of a |DwfLibrary| instance:

* |deviceEnum:link| provides |device enumeration:link| functionality;
* |deviceControl:link| provides |device control:link| functionality;
* |spectrum:link| provides |signal processing:link| functionality.

In most programs, the |DwfLibrary| instance is only used for opening a |DwfDevice|, using either one of the |DeviceControl.open:link| or |DeviceControl.openEx:link| methods, or the |pydwf.utilities.openDwfDevice:link| convenience function; the latter takes a |DwfLibrary| instance as a parameter.

|DwfLibrary| reference
----------------------

.. autoclass:: pydwf.core.dwf_library.DwfLibrary()
   :special-members: __init__
