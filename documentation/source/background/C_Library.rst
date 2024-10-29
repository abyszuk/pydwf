.. include:: /substitutions.rst

About the DWF C Library
=======================

|Digilent| provides the Digilent Waveforms library to control their line of line of electronic test and measurement devices. The library is available as a DLL on Microsoft Windows, a shared object ("so") library on Linux, and a framework on Apple's macOS. The provided library is accompanied by a C header file; together with the shared library file itself, this allows access to the functionality provided from the C and C++ programming languages.

.. _Installing DWF:

Installing the DWF library
--------------------------

The |libdwf| library is automatically installed as part of Digilent's *Waveforms* software, which can be downloaded from |waveforms-download-here| (official link, with mandatory email address harvesting) or |waveforms-download-direct-here| (non-official link, without email harvesting).

Depending on your OS, you may need to install the Digilent's *Adept* software as well. Ik can be downloaded from |adept-download-here| (with email address harvesting) or |adept-download-direct-here| (without email harvesting).

Accessing the DWF library from Python
-------------------------------------

Most popular programming languages provide a mechanism to access functions in shared libraries. In Python, such a mechanism is provided by the |ctypes:link| module that is part of the standard Python library.

The |pydwf| package is a binding to the functionality provided by the DWF library, using the |ctypes:link| module. It makes all types and functions provided by the DWF library available for use in Python programs, wrapping them in a small set of classes that makes them easy to use.

Overview of the C API
---------------------

The DWF library comes with a C header file that (for version |libdwf-version|) defines the |libdwf-enum-count| enumeration types and |libdwf-func-count| function calls that together make up the DWF API. Of the |libdwf-func-count| function calls provided, |libdwf-func-count-obsolete| are labeled *obsolete*. Their functionality is usually superseded by newer, more general functions.

The API functions are organized in 16 sub-categories, each providing access to a subset of the DWF functionality — for example, a specific type of instrument, or functions to send and receive messages using a certain protocol.

The function counts for each of the sub-categories of functionality are listed below, to give some idea of the complexity of the different areas of the API.

.. table:: DWF C API function counts (by category), version |libdwf-version|
   :align: center

   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | **C API category**  | **pydwf equivalent**                              | **active** | **obsolete** | **total** |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | *(miscellaneous)*   | |DwfLibrary:link|                                 |          5 |            0 |         5 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfEnum            | |DwfLibrary.deviceEnum:link|                      |         11 |            4 |        15 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfDevice          | |DwfLibrary.deviceControl:link|, |DwfDevice:link| |         16 |            0 |        16 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfSpectrum        | |DwfLibrary.spectrum:link|                        |          3 |            0 |         3 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfAnalogIn        | |DwfDevice.analogIn:link|                         |        100 |            1 |       101 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfAnalogOut       | |DwfDevice.analogOut:link|                        |         58 |           25 |        83 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfAnalogIO        | |DwfDevice.analogIO:link|                         |         17 |            0 |        17 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfAnalogImpedance | |DwfDevice.analogImpedance:link|                  |         23 |            0 |        23 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfDigitalIn       | |DwfDevice.digitalIn:link|                        |         60 |            2 |        62 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfDigitalOut      | |DwfDevice.digitalOut:link|                       |         52 |            1 |        53 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfDigitalIO       | |DwfDevice.digitalIO:link|                        |         25 |            0 |        25 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfDigitalUart     | |DwfDevice.protocol.uart:link|                    |         10 |            0 |        10 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfDigitalSpi      | |DwfDevice.protocol.spi:link|                     |         32 |            0 |        32 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfDigitalI2c      | |DwfDevice.protocol.i2c:link|                     |         14 |            0 |        14 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfDigitalCan      | |DwfDevice.protocol.can:link|                     |          7 |            0 |         7 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | FDwfDigitalSwd      | |DwfDevice.protocol.swd:link|                     |         12 |            0 |        12 |
   +---------------------+---------------------------------------------------+------------+--------------+-----------+
   | **TOTAL**                                                               |        445 |           33 |       478 |
   +-------------------------------------------------------------------------+------------+--------------+-----------+

From this table, it is clear that the most complex parts of the API are the AnalogIn ("oscilloscope") and AnalogOut ("waveform generator") instruments, followed by the DigitalIn ("logic analyzer") and DigitalOut ("pattern generator") instruments. About 60% of all the functions provided by the DWF library are directly related to control of these four powerful instruments.

Error handling in the C API
---------------------------

Each function in the C API returns an integer, indicating its success or error status. A value of 0 indicates an error, while a value of 1 indicates success.

Note:
    This is different from the convention used in most C libraries, where a 0 return value indicates success.

    In earlier versions of *libdwf* the return value of operations was specified to be of type *bool*, with *true* (1) indicating success and *false* (0) indicating failure. The return type was changed to *int* at some point, but the values for success and failure remained the same for reasons of backward compatibility.

In case a function returns 0, indicating some kind of failure, the C API provides two functions to inquire the reason of the failure. The *FDwfGetLastError* function returns a value of C enumeration type DWFERC (represented in Python by the enumeration type |DwfErrorCode:link|), indicating the cause of the last error, while function *FDwfGetLastErrorMsg* returns a string describing the error.

In |pydwf|, the low-level error reporting provided by the C API is handled by checking the return value of any C API call, and raising a |DwfLibraryError:link| whenever a failure is detected.
