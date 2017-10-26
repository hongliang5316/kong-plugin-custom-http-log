%define         kong_plugin_suffix     /usr/local/share/lua/5.1/kong/plugins/
%define         kong_user       nobody
%define         kong_group      nobody
%define         __os_install_post /usr/lib/rpm/brp-compress

Name:       kong-plugin-custom-http-log
Version:    %{_version}
Release:    1
Summary:    The custom-http-log plugin for kong

Group:      Development/Libraries/Luastatistics
License:    BSD
URL:        http://www.getkong.org

Source0:    kong-plugin-custom-http-log-%{version}.tar.gz

BuildArch:      noarch
BuildRoot:      %{build_root}

AutoReqProv:    no
Provides:       kong

%description
The custom-http-log plugin for kong

%prep
%setup -q -n kong-plugin-custom-http-log-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
export destdir=$RPM_BUILD_ROOT%{kong_plugin_suffix}
install -d $destdir
install -d $destdir/custom-http-log
install *.lua $destdir/custom-http-log/

%clean
rm -rf $RPM_BUILD_ROOT

%preun

#%files -f %{name}.manifest
%files
%{kong_plugin_suffix}/custom-http-log/*.lua
%defattr(-,%{kong_user},%{kong_group},-)

%changelog
* Sat Jun 04 2016 hongliang5316 <hongliang5316@gmail.com> - 0.01-1
- release 0.01-1
