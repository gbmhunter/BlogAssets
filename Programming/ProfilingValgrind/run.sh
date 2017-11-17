#!/usr/bin/env bash

g++ profiling_test.c -o profiling_test
valgrind --tool=callgrind --dump-instr=yes --collect-jumps=yes ./profiling_test
kcachegrind