#!/bin/sh

PYTHON=/usr/bin/python

PREFIX=/usr
DATADIR=$PREFIX/share/toffmo

cd $DATADIR
$PYTHON toffmo.pyc "$@"
cd - >/dev/null

# End of file
