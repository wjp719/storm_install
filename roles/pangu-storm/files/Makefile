.PHONY: rpm clean

NAME ?= apache-storm
VERSION ?= 0.9.4
BUILD_NUMBER ?= 1
SOURCE = $(NAME)-$(VERSION).tar.gz
TOPDIR = /tmp/storm-rpm
PWD = $(shell pwd)

rpm: $(SOURCE)
	@rpmbuild -v -bb \
			--define "_sourcedir $(PWD)" \
			--define "_rpmdir $(PWD)" \
			--define "_topdir $(TOPDIR)" \
			--define "name $(NAME)" \
			--define "version $(VERSION)" \
			--define "build_number $(BUILD_NUMBER)" \
			storm.spec

$(SOURCE):
	@spectool \
			--define "name $(NAME)" \
			--define "version $(VERSION)" \
			-g storm.spec

clean:
	@rm -rf $(TOPDIR) x86_64
	@rm -f $(SOURCE)
