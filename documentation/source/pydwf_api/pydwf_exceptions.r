.. include:: /substitutions.rst

|pydwf| exceptions
==================

The |PyDwfError| and |DwfLibraryError| exceptions are used to report errors from |pydwf| to user programs.

Using the |pydwf| exceptions
----------------------------

The |PyDwfError| and |DwfLibraryError| exceptions are defined in the |pydwf.core.auxiliary.exceptions| module. The top-level |pydwf| package imports both of them from that module to make them available to user scripts. To use either of them, they should be imported from the top-level |pydwf| package:

.. code-block:: python

   from pydwf import DwfLibrary, PyDwfError, DwfLibraryError

   dwf = DwfLibrary()

   try:
       use_pydwf(dwf)
   except DwfLibraryError as e:
       print("An error occurred at the C library level:", e)
   except PyDwfError as e:
       print("An error occurred at the Python module level:", e)

Error handling in the |pydwf| package
-------------------------------------

Python provides exceptions to handle errors, which is quite different from the lower level return-value based mechanism used in the C API. Fortunately, it is possible to turn the low-level errors reported by the C API functions into Python exceptions.

To do this, the |pydwf| package inspects the return value of each call to the C API, and, in case of an error (i.e., a return value unequal to 1), it raises a |DwfLibraryError:link| exception that contains both the DWERC error code of the last function called and its corresponding textual description, as obtained by calling the *FDwfGetLastError* and *FDwfGetLastErrorMsg* functions in the shared library.

Exceptions raised by the |pydwf| package
----------------------------------------

Almost all exceptions raised by |pydwf| are a result of a failure reported by the underlying C library. However, there are a few circumstances where |pydwf| detects an error condition before or after such a call was made. Such errors are handled by raising a |PyDwfError:link| exception, which derives from Python's standard |Exception| class.

.. graphviz::
   :caption: Inheritance diagram of |pydwf| exceptions
   :align: center

   digraph {

      rankdir=BT;

      // nodes
      node          [shape="rectangle"];

      exception_err [label="Exception"];
      pydwf_err     [label="PyDwfError"];
      dwflib_err    [label="DwfLibraryError"];

      // edges
      edge         [arrowhead="onormal"];

      dwflib_err -> pydwf_err;
      pydwf_err  -> exception_err;
   }

As the inheritance diagram shows, the |DwfLibraryError| exception type derives from |PyDwfError|. This makes it easy to catch any |pydwf| error in code:

.. code-block:: python

   from pydwf import DwfLibrary, PyDwfError

   dwf = DwfLibrary()

   try:
       use_pydwf(dwf)
   except PyDwfError as e:
       print("An error occurred at the C library -or- Python module level:", e)

*pydwf* exceptions reference
----------------------------

.. autoclass:: pydwf.core.auxiliary.exceptions.PyDwfError()

.. autoclass:: pydwf.core.auxiliary.exceptions.DwfLibraryError()
