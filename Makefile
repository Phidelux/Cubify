# Simple Makefile to install/uninstall the Cubify Inkscape extension.
#
# By default the extension is installed into the per-user Inkscape
# extensions directory. Override EXTDIR to install elsewhere, e.g.:
#
#   make install EXTDIR=/usr/share/inkscape/extensions

EXTDIR ?= $(HOME)/.config/inkscape/extensions
FILES  := cubify.inx cubify.py

.PHONY: install uninstall

install:
	@mkdir -p "$(EXTDIR)"
	@install -m 0644 cubify.inx "$(EXTDIR)/cubify.inx"
	@install -m 0755 cubify.py  "$(EXTDIR)/cubify.py"
	@echo "Installed Cubify to $(EXTDIR)"

uninstall:
	@rm -f $(addprefix "$(EXTDIR)/",$(FILES))
	@echo "Removed Cubify from $(EXTDIR)"
