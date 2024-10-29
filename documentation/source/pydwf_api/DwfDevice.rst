.. include:: /substitutions.rst

The |DwfDevice| class
=====================

The |DwfDevice| class represents a previously opened Digilent Waveforms device. It is the entry point to all useful functionality of the Digilent Waveforms device.

Using the |DwfDevice| class
---------------------------

To obtain a |DwfDevice:link| instance you first need to initialize a |DwfLibrary:link| instance. The |DwfLibrary| can then be used to obtain a |DwfDevice|, either by using the |DeviceControl.open:link| method or by using the |pydwf.utilities.openDwfDevice:link| convenience function.

After the program is done using a device, it should be closed. This can be done explicitly, via the |DwfDevice.close:link| method, or implicitly, by using the |DwfDevice| as a so-called *context manager* for itself. The latter method is often preferable, since it guarantees that the device will be closed even when an exception occurs while using it:

.. code-block:: python

   from pydwf import DwfLibrary
   from pydwf.utilities import openDwfDevice

   dwf = DwfLibrary()

   with openDwfDevice(dwf) as device:
        # When we leave the 'with' statement, the device is guaranteed to be closed.
        print("Trigger sources supported by this device:", device.triggerInfo())

        # This is true even if an exception is raised inside the 'with' statement's body:
        raise RuntimeError("yikes!")

After obtaining a |DwfDevice|, you can use the dozen or so methods it provides. These methods are documented as part of the |DwfDevice:link| class in the next section.

Twelve attributes are provided to access particular sub-APIs of a |DwfDevice| instance. Depending on the type of task that you are using your Digilent Waveforms device for, one or several of these attributes will be your main handle to configure instruments and to send or receive data:

* |analogIn:link| provides a multi-channel oscilloscope;
* |analogOut:link| provides a multi-channel analog signal generator;
* |analogIO:link| provides voltage, current, and temperature monitoring and control;
* |analogImpedance:link| provides measurement of impedance and other quantities;
* |digitalIn:link| provides a multi-channel digital logic analyzer;
* |digitalOut:link| provides a multi-channel digital pattern generator;
* |digitalIO:link| provides static digital I/O functionality;
* |protocol.uart:link| provides UART protocol configuration, send, and receive functionality;
* |protocol.spi:link| provides SPI protocol configuration, send, and receive functionality;
* |protocol.i2c:link| provides I²C protocol configuration, send, and receive functionality;
* |protocol.can:link| provides CAN protocol configuration, send, and receive functionality;
* |protocol.swd:link| provides SWD protocol configuration, send, and receive functionality.

|DwfDevice| reference
---------------------

.. autoclass:: pydwf.core.dwf_device.DwfDevice()
