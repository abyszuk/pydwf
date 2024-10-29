.. include:: /substitutions.rst

Example scripts
===============

The Python examples can be installed locally after installing the |pydwf| package by executing the following command:

.. code-block:: sh

   python -m pydwf extract-examples

This will create a local directory called *pydwf-examples* containing the Python examples that demonstrate many of the capabilities of the Digilent Waveforms devices and |pydwf|.

.. todo::

    **This section is currently incomplete.**

    Some examples that are currently missing:

    * We need more examples for the |DigitalIn:link| and |DigitalOut:link| instruments.
    * The four main instruments need examples for all their modes.
    * We need examples using inter-instrument triggering.
    * We need examples for the |AnalogImpedance:link| functionality.
    * We need examples for the |Spectrum:link| functionality.
    * We need examples for the |DeviceEnum:link| and |DeviceControl:link| APIs.

The following examples are currently provided:

.. rubric:: |DeviceControl| functionality example

`DigitalDiscoveryLedBrightnessParameter.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/DigitalDiscoveryLedBrightnessParameter.py>`_
  Modulate the brightness of the Digital Discovery power-on LED.

  This example only works with the Digital Discovery device.

.. rubric:: |DeviceEnumeration| functionality example

No example available (yet).

For now, it is recommended to have a look at the *list_devices()* function in the `__main.py__ <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf/__main__.py>`_ top-level module.

.. rubric:: |AnalogIn| instrument examples

`AnalogInSimple.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/AnalogInSimple.py>`_
  This example demonstrates the easiest way to obtain samples from the analog input channels.

  The method used by the example is useful if triggering or precise timing is not important.

`AnalogInShiftScanShiftScreenDemo.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/AnalogInShiftScanShiftScreenDemo.py>`_
  This example demonstrates recording using the |AnalogIn| instrument, in *ScanScreen* or *ScanShift* modes.

  The acquisition mode (*ScanScreen* or *ScanShift*) can be selected using a command line parameter.

`AnalogInRecordMode.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/AnalogInRecordMode.py>`_
  This example demonstrates acquisition using the |AnalogIn| instrument.

  The script emits sinusoid signals on the first two channels of the |AnalogOut| instrument, and continuously samples the first two channels of the |AnalogIn| instrument.

  This example assumes that the analog output channels are connected to the analog input channels.

  Availability of the |matplotlib:link| package is assumed for plotting results.

.. rubric:: |AnalogOut| instrument examples

`AnalogOutShowChannelAndNodeInfo.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/AnalogOutShowChannelAndNodeInfo.py>`_
  This program starts by selecting the device configuration that has the largest count of analog output channels.

  It then enumerates all these output channels and shows their capabilities, including all sub-nodes of each channel, and *their* capabilities.

  This example is mostly interesting to show the capabilities of the rarely used third and fourth analog output channels of the Analog Discovery 2, which are only available in one device configuration. These two extra channels are essentially the V+ and V- power supply outputs.

`AnalogOutSimple.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/AnalogOutSimple.py>`_
  Show simple control of the analog output channels of the |AnalogOut| instrument.

  This example programs an |AnalogOut| output channel for a square output waveform, but doesn't actually start it. By configuring the channel to drive the *Initial* waveform value on its output while idle, the output voltage can be controlled directly by manipulating the channel's *amplitude* setting.

  This method is useful if the output needs to change only occasionally, and if triggering or precise timing is not important.

  This technique is much faster than the alternative approach of changing the channel's *offset* setting, which takes a long time to stabilize after a change due to the presence of an analog low-pass filter.
  The demonstrated technique can change the analog output value at a rate of several hundred times per second.

`AnalogOutPlayFunction.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/AnalogOutPlayFunction.py>`_
  Play one of the built-in analog output waveforms using the |AnalogOut| instrument.

  The user can select the waveform, frequency, amplitude, offset, phase, and symmetry parameters using command line options.

`AnalogOutShowFunctionSymmetry.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/AnalogOutShowFunctionSymmetry.py>`_
  Show the way the *symmetry* setting changes the behavior of the built-in analog output waveforms of the |AnalogOut| instrument.

  This example assumes that the first analog output channel is connected to the first analog input channel.

  Availability of the |matplotlib:link| package is assumed for plotting results.

`AnalogOutAmplitudeModulationDemo.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/AnalogOutAmplitudeModulationDemo.py>`_
  Show the way Amplitude Modulation (AM) changes a carrier sine wave using AnalogOut instrument.

  This example assumes that the first analog output channel is connected to the first analog input channel.

    Availability of the |matplotlib:link| package is assumed for plotting results.

`AnalogOutPlayCustomWaveform.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/AnalogOutPlayCustomWaveform.py>`_
  Show a custom waveform on CH1 of the |AnalogOut| instrument. The custom waveform can be given as a file containing human-readable numbers.
  If no filename is specified, a default custom waveform is generated.

  Hook up the first analog output channel of your device to an oscilloscope to see the custom waveform.

`AnalogOutContinuousPlay.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/AnalogOutContinuousPlay.py>`_
  Show either a circle or a polygon on CH1 (X) and CH2 (Y) of the |AnalogOut| instrument.

  To properly appreciate this example, hook up these two channels to a second oscilloscope that is configured for X-vs-Y display mode.

`AnalogOutSpinningGlobe.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/AnalogOutSpinningGlobe.py>`_
  Show a spinning globe on CH1 (X) and CH2 (Y) of the |AnalogOut| instrument.

  To properly appreciate this example, hook up these two channels to a second oscilloscope that is configured for X-vs-Y display mode.

.. rubric:: |AnalogIO| functionality example

`AnalogIO.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/AnalogIO.py>`_
  This example enumerates all |AnalogIO| channels and their nodes. After that, it continuously reports the quantities associated with the "USB Monitor" channel.

.. rubric:: Analog Impedance examples

Not yet available.

.. rubric:: |DigitalIn| instrument examples

Not yet available.

.. rubric:: |DigitalOut| instrument examples

`DigitalOutShowStatusDuringPulsePlayback.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/DigitalOutShowStatusDuringPulsePlayback.py>`_
  Demonstrate the behavior of the |DigitalOut| instrument status during Pulse playback.

.. rubric:: |DigitalIO| functionality example

`DigitalIO.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/DigitalIO.py>`_
  Demonstrate static monitoring and control of the digital input and output pins.

.. rubric:: Protocol examples

`ProtocolUART.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/ProtocolUART.py>`_
  An example showing loopback transmission and reception using the UART protocol.

`ProtocolCAN.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/ProtocolCAN.py>`_
  An example showing loopback transmission and reception of messages using the CAN bus protocol.

`ProtocolSPI.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/ProtocolSPI.py>`_
  This example demonstrates continuous readout of an ADXL345 triple-axis accelerometer using the SPI protocol.

  The program expects to find the accelerometer IC attached to the proper pins. See the source code for a description on how to hook up an ADXL345 to make this work.

`ProtocolI2C.py <https://github.com/sidneycadot/pydwf/blob/master/source/pydwf-examples/ProtocolI2C.py>`_
  This example demonstrates continuous readout of an ADXL345 triple-axis accelerometer using the I²C protocol.

  The program expects to find the accelerometer IC attached to the proper pins. See the source code for a description on how to hook up an ADXL345 to make this work.
