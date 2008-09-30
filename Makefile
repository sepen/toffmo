#
# Makefile

DESTDIR=
BINDIR=/usr/local/bin
CONFDIR=/usr/local/etc
DATADIR=/usr/local/share/toffmo

.PHONY: all install clean

src/toffmo: src/toffmo.py
	@sed -e "s|CONFIG_DIR=''|CONFIG_DIR='$(CONFDIR)/'|" \
	    -e "s|DATA_DIR=''|DATA_DIR='$(DATADIR)/'|" \
	    src/toffmo.py > src/toffmo

all: src/toffmo

install: src/toffmo src/toffmo.conf src/earn.jpg
	@install -D -m 0755 src/toffmo $(DESTDIR)$(BINDIR)/toffmo
	@install -D -m 0644 src/toffmo.conf $(DESTDIR)$(CONFDIR)/toffmo.conf
	@install -D -m 0644 src/earn.jpg $(DESTDIR)$(DATADIR)/earn.jpg
	
clean:
	@rm -f src/toffmo

# End of file
