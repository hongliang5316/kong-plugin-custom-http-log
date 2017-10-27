.PHONY: all compile

version=0.02

all: compile

build: compile
	sh rpm/pack-kong-plugin-custom-http-log $(version)
	#cp -r /root/rpmbuild/RPMS/noarch/yfcdn_api-$(version)-$(release).noarch.rpm /opt/rpms/
