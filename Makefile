#
# Makefile

PYTHON=/usr/bin/python

DESTDIR=
PREFIX=/usr
BINDIR=$(PREFIX)/bin
CONFDIR=$(PREFIX)/etc
DATADIR=$(PREFIX)/share/toffmo

.PHONY: all install clean

all: clean src/toffmo.pyc src/toffmo

src/toffmo.pyc: src/toffmo.py
	@$(PYTHON) ./build.py && rm -f ./build.pyc

src/toffmo: src/toffmo.sh
	@sed -e "s|PYTHON=.*|PYTHON=$(PYTHON)|" \
	     -e "s|PREFIX=.*|PREFIX=$(PREFIX)|" \
	     -e "s|DATADIR=.*|DATADIR=$(DATADIR)|" \
	     src/toffmo.sh > src/toffmo
	@chmod +x src/toffmo

install: src/toffmo src/toffmo.pyc src/toffmo.conf src/toffmo.jpg
	@install -D -m 0755 src/toffmo $(DESTDIR)$(BINDIR)/toffmo
	@install -D -m 0644 src/toffmo.conf $(DESTDIR)$(DATADIR)/toffmo.conf.example
	@install -D -m 0644 src/toffmo.pyc $(DESTDIR)$(DATADIR)/toffmo.pyc
	@install -D -m 0644 src/toffmo.jpg $(DESTDIR)$(DATADIR)/toffmo.jpg
	
clean:
	@rm -f src/*.pyc src/toffmo

# End of file
