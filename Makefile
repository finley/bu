#
#	$Id$
#

BIN     := ${DESTDIR}/usr/bin
TARBALL := bu-n-psg.tar.bz2

all:

install:	bu psg
	install -d -m 755 $(BIN)
	install -m 755 bu $(BIN)
	install -m 755 psg $(BIN)

.PHONY: deb
deb: tarball
	fakeroot dpkg-buildpackage

.PHONY: clean
clean:
	rm $(TARBALL)

.PHONY: tarball
tarball:
	tar -cvjf $(TARBALL) \
		bu \
		psg \
		CREDITS \
		Makefile
