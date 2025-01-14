# pydwf

**NOTICE**: this is a copy of original project at https://github.com/sidneycadot/pydwf obtained from archive of softwareheritage.org.
Version in the archive is 1.1.17, while the newest available version is 1.1.19.
The author has taken down the repo in response to change in Digilent's approach to how they distribute their software.
I think this library is too useful to disappear from the internet, so I made a copy.

This is the README of *pydwf*, a Python package to control the Digilent Waveforms lineup of electronic test and measurement devices made by [Digilent](https://store.digilentinc.com/).

It wraps all functions of *libdwf*, the [low-level C library](https://pydwf.readthedocs.io/en/latest/background/C_Library.html) provided by Digilent, in an easy-to-use, class-based Python API. Like the C library, the *pydwf* package supports Windows, Linux (Intel and ARM), and macOS. The *libdwf* library is automatically installed as part of Digilent's *Waveforms* software, which can be downloaded from [here](https://digilent.com/shop/software/digilent-waveforms/download/) (official link, with mandatory email harvesting) or [here](https://lp.digilent.com/complete-waveforms-download/) (non-official link, without email harvesting).

The current release of *pydwf* is version 1.1.17.
It is based on version 3.20.1 of *libdwf*, but it should also work with other versions.

The *pydwf* package comes with documentation and a number of ready-to-run [examples](https://pydwf.readthedocs.io/en/latest/background/Examples.html) that demonstrate how *pydwf* can be used to perform common and not-so-common tasks.

A [command-line tool](https://pydwf.readthedocs.io/en/latest/background/CommandLineTool.html) is provided that can be used, among other things, to list the available Digilent Waveforms devices and their configurations.

This README file contains information about the project. Readers who want to learn how to use *pydwf* are referred to the [API documentation](https://pydwf.readthedocs.io/en/latest/pydwf_api/pydwf_overview.html).

## Supported devices

The following devices can be controlled using *pydwf*:

* [Electronics Explorer](https://digilent.com/reference/test-and-measurement/electronics-explorer/start) (legacy)
* [Analog Discovery](https://digilent.com/reference/test-and-measurement/analog-discovery/start) (legacy)
* [Analog Discovery 2](https://digilent.com/reference/test-and-measurement/analog-discovery-2/start)
* [Analog Discovery 3](https://digilent.com/reference/test-and-measurement/analog-discovery-3/start)
* [Digital Discovery](https://digilent.com/reference/test-and-measurement/digital-discovery/start)
* [Analog Discovery Studio](https://digilent.com/reference/test-and-measurement/analog-discovery-studio/start)
* [DSP3340 Discovery USB power supply](https://digilent.com/reference/test-and-measurement/discovery-power-supply-3340/start)
* [Analog Discovery Pro 3x50](https://digilent.com/reference/test-and-measurement/analog-discovery-pro-3x50/start) (3250 and 3450 models)
* [Analog Discovery Pro 5250](https://digilent.com/reference/test-and-measurement/analog-discovery-pro-5250/start) (a National Instruments VB-8012 rebranded as a Digilent device; Windows only)

The *pydwf* package has been extensively tested with the Analog Discovery 2, Digital Discovery, and ADP3450 devices. It should also work with the other devices listed, but these haven't been tested. If you have such a device and encounter problems, please report an issue on the [GitHub issue tracker](https://github.com/sidneycadot/pydwf/issues).

## Dependencies

The *pydwf* package requires Python 3.6 or higher.

In order for *pydwf* to work, recent versions of the Digilent Adept and Digilent Waveforms packages must be installed. These provide the C libraries that *pydwf* uses to interact with devices. Generally speaking, if the Waveforms GUI application provided by Digilent works on your system, you're good to go.

*pydwf* depends on the [numpy](https://numpy.org/) package to handle the considerable amount of data transferred between the PC and Digilent devices when performing high-speed signal generation or capture operations.

Some of the [examples](https://pydwf.readthedocs.io/en/latest/background/Examples.html) depend on the [matplotlib](https://matplotlib.org/) package, but *pydwf* itself will work without it.

## Project hosting

The project repository and issue tracker are hosted on [GitHub](https://github.com/):

https://github.com/sidneycadot/pydwf/

## Installation using *pip*

The installable package is hosted on [PyPI](https://pypi.org/):

https://pypi.org/project/pydwf/

This allows installation using the standard *pip* (or *pip3*) tool:

```
pip install pydwf
```

After installing *pydwf*, the following command will show the version of *pydwf* and the underlying DWF library:

```
python -m pydwf version
```

After installing *pydwf*. the following command will list all Digilent Waveforms devices connected to the system and, for each of them, list the supported configurations:

```
python -m pydwf list -c
```

## Documentation

The project documentation is hosted on [Read the Docs](https://readthedocs.org/). The latest version can be reached via the following link:

https://pydwf.readthedocs.io/en/latest/

If desired, the documentation can also be installed locally after installing the package by executing the following command:

```
python -m pydwf extract-html-docs
```

This will create a local directory called *pydwf-docs-html* containing the project documentation in HTML format.

Alternatively, a PDF version of the manual can be extracted as well:

```
python -m pydwf extract-pdf-manual
```

## Examples

The Python [examples](https://pydwf.readthedocs.io/en/latest/background/Examples.html) can be installed locally after installing the *pydwf* package by executing the following command:

```
python -m pydwf extract-examples
```

This will create a local directory called *pydwf-examples* containing the Python examples that demonstrate many of the capabilities of the Digilent Waveforms devices and *pydwf*.

These examples are intended as a useful starting point for your own Python scripts. See the [Examples overview](https://pydwf.readthedocs.io/en/latest/background/Examples.html) for more information.

## Acknowledgements

Many thanks to Digilent for making the awesome Waveforms devices, and to provide not only the very capable *Waveforms* GUI software, but also the cross-platform SDK on which *pydwf* is based. Great work!

My company [Jigsaw B.V.](https://www.jigsaw.nl/) supported the effort to make *pydwf*. If you need any kind of high-tech software (with or without Digilent Waveforms devices), and you’re somewhat in the vicinity of Delft, The Netherlands, [give us a call](https://jigsaw.nl/#Contact).

Thanks to my longtime friend Pepijn for proof-reading the documentation and providing his perspective on several issues that came up while implementing *pydwf*. The package is a lot better because of your help.

Lastly, thanks to Petra for your patience with having all kinds of electronics equipment in the living room while developing this package (and before, and after, …). You may not share my enthusiasm for this particular hobby, but I am very fortunate that you are at least enthusiastic about my enthusiasm, if that makes sense.

*— SC*
