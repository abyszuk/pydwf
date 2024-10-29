.. include:: /substitutions.rst

*pydwf* utilities
=================

The |pydwf.utilities| package provides functionality built on top of the core functionality that is available in the |pydwf| core package. It provides high-level functions that reflect best-practice implementations for common use-cases of |pydwf|.

Currently, only a single utility function is provided by the |pydwf.utilities| module: |pydwf.utilities.openDwfDevice:link|, which is documented below.

Using the |pydwf.utilities| functionality
-----------------------------------------

To use functionality from the |pydwf.utilities| package, import the symbols you need from it:

.. code-block:: python

   """Demonstrate use of the openDwfDevice function."""

   from pydwf import DwfLibrary
   from pydwf.utilities import openDwfDevice

   dwf = DwfLibrary()

   with openDwfDevice(dwf) as device:
       use_dwf_device(device)

The example above demonstrates the use of the |pydwf.utilities.openDwfDevice:link| function. This function encapsulates a number of core |pydwf| functions to allow easy selection of devices and device configurations. It is documented below.

*pydwf.utilities.openDwfDevice* function reference
--------------------------------------------------

.. autofunction:: pydwf.utilities.open_dwf_device.openDwfDevice
