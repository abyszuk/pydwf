.. include:: /substitutions.rst

Triggering explained
====================

.. todo::

    **This section is currently incomplete.**

    The intention is to discuss here the triggering bus architecture of the Digilent Waveforms devices, and to provide a detailed explanation of the possibilities and limitations.

    It would also be useful to provide some specs (latency, jitter) for common devices, which could be measured.

The Digilent Waveforms devices provide an internal triggering bus, allowing the |AnalogIn|, |AnalogOut|, |DigitalIn|, and |DigitalOut| instruments to start their operation (signal capture or signal generation) at a precisely defined time relative to some internal or external event.

The triggering infrastructure is highly flexible. The trigger detector functionality of the |AnalogIn| and |DigitalIn| instruments can be used not only by those instruments themselves, but also by any of the other instruments, and it is also possible to have instruments trigger on the start of one of the other instruments, externally supplied trigger signals, or a trigger signal sent from the controlling PC.

Trigger sources
---------------

The following trigger sources are available:

* :py:attr:`DwfTriggerSource.None_              <pydwf.core.auxiliary.enum_types.DwfTriggerSource.None_>`
* :py:attr:`DwfTriggerSource.PC                 <pydwf.core.auxiliary.enum_types.DwfTriggerSource.PC>`
* :py:attr:`DwfTriggerSource.DetectorAnalogIn   <pydwf.core.auxiliary.enum_types.DwfTriggerSource.DetectorAnalogIn>`
* :py:attr:`DwfTriggerSource.DetectorDigitalIn  <pydwf.core.auxiliary.enum_types.DwfTriggerSource.DetectorDigitalIn>`
* :py:attr:`DwfTriggerSource.AnalogIn           <pydwf.core.auxiliary.enum_types.DwfTriggerSource.AnalogIn>`
* :py:attr:`DwfTriggerSource.DigitalIn          <pydwf.core.auxiliary.enum_types.DwfTriggerSource.DigitalIn>`
* :py:attr:`DwfTriggerSource.DigitalOut         <pydwf.core.auxiliary.enum_types.DwfTriggerSource.DigitalOut>`
* :py:attr:`DwfTriggerSource.AnalogOut1         <pydwf.core.auxiliary.enum_types.DwfTriggerSource.AnalogOut1>`
* :py:attr:`DwfTriggerSource.AnalogOut2         <pydwf.core.auxiliary.enum_types.DwfTriggerSource.AnalogOut2>`
* :py:attr:`DwfTriggerSource.AnalogOut3         <pydwf.core.auxiliary.enum_types.DwfTriggerSource.AnalogOut3>`
* :py:attr:`DwfTriggerSource.AnalogOut4         <pydwf.core.auxiliary.enum_types.DwfTriggerSource.AnalogOut4>`
* :py:attr:`DwfTriggerSource.External1          <pydwf.core.auxiliary.enum_types.DwfTriggerSource.External1>`
* :py:attr:`DwfTriggerSource.External2          <pydwf.core.auxiliary.enum_types.DwfTriggerSource.External2>`
* :py:attr:`DwfTriggerSource.External3          <pydwf.core.auxiliary.enum_types.DwfTriggerSource.External3>`
* :py:attr:`DwfTriggerSource.External4          <pydwf.core.auxiliary.enum_types.DwfTriggerSource.External4>`
* :py:attr:`DwfTriggerSource.High               <pydwf.core.auxiliary.enum_types.DwfTriggerSource.High>`
* :py:attr:`DwfTriggerSource.Low                <pydwf.core.auxiliary.enum_types.DwfTriggerSource.Low>`
* :py:attr:`DwfTriggerSource.Clock              <pydwf.core.auxiliary.enum_types.DwfTriggerSource.Clock>`

Trigger timing and precision
----------------------------

(to be written)
