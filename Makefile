#
# Makefile

DESTDIR=

.PHONY: all install clean

toffmo: src/toffmo.py
	ln -s src/toffmo.py toffmo

all: toffmo

install:
	install -D -m 0755 toffmo $(DESTDIR)/usr/bin/toffmo

clean:
	rm -f toffmo

# End of file
