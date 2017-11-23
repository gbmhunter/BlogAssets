.. role:: bash(code)
    :language: bash

.. role:: cpp(code)
    :language: cpp

============
BlogAssets
============

--------------------------------------------------------------------------------------------------
Data, code, graphs, images and other assets that are used on the blog www.mbedded.ninja.
--------------------------------------------------------------------------------------------------

-----------
Mathematics
-----------

QuadToQuad
----------

Python script that performs 2D quad-to-quad projections.

.. code::

    $ python3 main.py
    ...output text and image

Dependencies:

- numpy
- matplotlib

-----------
Programming
-----------

ProfilingGprof
==============

Example code for using :code:`gprof`.

Run the commands:

.. code::

    $ gcc -pg -no-pie profiling_test.c -o profiling_test
    $ ./profiling_test
    $ gprof ./profiling_test
    Flat profile:

    Each sample counts as 0.01 seconds.
    %   cumulative   self              self     total           
     time   seconds   seconds    calls  ms/call  ms/call  name    
     60.96      0.68     0.68        1   676.63   676.63  fibonacci
     31.84      1.03     0.35        1   353.47   353.47  loop100M
      8.19      1.12     0.09                             frame_dummy
    ...

To create a profile visualization, install :code:`gprof2dot` and then run:

.. code::

    $ gcc -pg -no-pie profiling_test.c -o profiling_test
    $ ./profiling_test
    $ gprof ./profiling_test > profiling.txt
    $ gprof2dot ./profiling.txt | dot -Tpng -o profiling.png

ProfilingValgrind
=================

Profiling example code using Valgrind/Callgrind and displaying the results with kcachegrind.

Run the command:

.. code::

    $ ./run.sh

Swig
====

*How To Run Examples:*

Run the command:

.. code::

    $ ./run.sh

*Dependencies (for all SWIG examples):*

- SWIG (tested on v3.0)
- python v3.x (tested on v3.5)
- gcc

BasicExample
------------

A basic SWIG example.

CallbackExample
---------------

A SWIG example showing how to implement callbacks that cross between Python and C++.

CustomTypemapExample
--------------------

A SWIG example showing how to implement custom typemapss between Python and C++, including
custom typechecks so that C++ function overloading can be used with the custom typemaps.

FunctionOverloadExample
-----------------------

A SWIG example showing how C++ function overloads can be called from Python.
