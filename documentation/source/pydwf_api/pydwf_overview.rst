.. include:: /substitutions.rst

Overview of |pydwf|
===================

All core |pydwf| functionality is made available for import from the top-level |pydwf| package:

* the |DwfLibrary:link| class, which is the starting point for all |pydwf| functionality;
* the |PyDwfError:link| and |DwfLibraryError:link| exceptions;
* the |enumeration types:link| that are used for parameters and result values of |pydwf| methods.

A small number of convenience functions and types have been implemented on top of the core |pydwf| package to simplify often-recurring tasks. These can be found in the |pydwf.utilities:link| package.

A minimal example of |pydwf| usage
----------------------------------

In practice, Python scripts that use |pydwf| will deal almost exclusively with just two classes: |DwfLibrary| and |DwfDevice|.

The following is a minimal example of using |pydwf| that uses both of these classes to produce a 1 kHz tone on the first analog output channel:

.. code-block:: python

   """A minimal, self-contained example of using pydwf."""

   from pydwf import DwfLibrary, DwfAnalogOutNode, DwfAnalogOutFunction
   from pydwf.utilities import openDwfDevice

   dwf = DwfLibrary()

   with openDwfDevice(dwf) as device:

       CH1 = 0  # Analog-out channel numbering starts at zero.
       node = DwfAnalogOutNode.Carrier

       device.analogOut.reset(CH1)

       device.analogOut.nodeEnableSet(CH1, node, True)
       device.analogOut.nodeFunctionSet(CH1, node, DwfAnalogOutFunction.Sine)
       device.analogOut.nodeFrequencySet(CH1, node, 1000.0)

       # Start the channel.
       device.analogOut.configure(CH1, True)

       input("Producing a 1 kHz tone on CH1. Press Enter to quit ...")

With this example in mind, we can introduce the all-important |DwfLibrary| and |DwfDevice| classes.

The two main |pydwf| classes
----------------------------

As a |pydwf| user, you will interact directly with two classes: |DwfLibrary| and |DwfDevice|. We shortly summarize what they do here. They each have their own more comprehensive sections later on.

.. rubric:: The |DwfLibrary| class

The |DwfLibrary:link| class represents the loaded Digilent Waveforms shared library itself, and provides methods that are not specific to a particular previously opened device. Examples include querying the library version, enumeration of devices, and opening a specific device for use.

Typically, a script will instantiate a single |DwfLibrary| and use that instance to open a specific Digilent Waveforms device, yielding a |DwfDevice| instance that can be used for the task at hand. This is also what happens in the example shown above.

A |DwfLibrary| instance provides a small number of methods and attributes that provide access to further functionality:

* |deviceEnum:link|    provides device enumeration functionality;
* |deviceControl:link| provides functionality to open a single device and to close all previously opened devices.
* |spectrum:link|      provides functionality for signal processing.

In most programs, the |DwfLibrary| class is only used to open a device for use, optionally selecting a specific |device configuration:link|. Since this is such an often-occurring operation, |pydwf| provides the |pydwf.utilities.openDwfDevice:link| convenience function that handles several practical use-cases, such as opening a specific device by its serial number, and/or selecting a device configuration that maximizes the buffer size for a certain instrument.

A comprehensive description of the |DwfLibrary| and its attributes can be found :py:doc:`here </pydwf_api/DwfLibraryToC>`.

.. rubric:: The |DwfDevice| class

The |DwfDevice:link| class represents a specific Digilent Waveforms device, such as an Analog Discovery 2 or a Digital Discovery, connected to the computer.

Instances of |DwfDevice| are obtained either by calling on of the low-level |DeviceControl.open:link| or |DeviceControl.openEx:link| methods, or by calling the higher-level, more powerful |pydwf.utilities.openDwfDevice:link| convenience function.

The |DwfDevice| class provides several miscellaneous methods, but the bulk of its functionality is accessible via one of the attributes listed below:

* |analogIn:link|        provides a multi-channel oscilloscope;
* |analogOut:link|       provides a multi-channel analog signal generator;
* |analogIO:link|        provides voltage, current, and temperature monitoring and control;
* |analogImpedance:link| provides measurement of impedance and other quantities;
* |digitalIn:link|       provides a multi-channel digital logic analyzer;
* |digitalOut:link|      provides a multi-channel digital pattern generator;
* |digitalIO:link|       provides static digital I/O functionality;
* |protocol.uart:link|   provides UART protocol configuration, send, and receive functionality;
* |protocol.spi:link|    provides SPI protocol configuration, send, and receive functionality.
* |protocol.i2c:link|    provides I²C protocol configuration, send, and receive functionality;
* |protocol.can:link|    provides CAN protocol configuration, send, and receive functionality;
* |protocol.swd:link|    provides SWD protocol configuration, send, and receive functionality.

After use, a Python script should :py:meth:`~pydwf.core.dwf_device.DwfDevice.close` the |DwfDevice|. Alternatively, the |DwfDevice| can act as a *context manager* for itself, to make sure it is closed whenever the containing *with* statement ends.

A comprehensive description of the |DwfDevice| and its attributes can be found :py:doc:`here </pydwf_api/DwfDeviceToC>`.
