#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : oslo.log
Version  : 3.43.0
Release  : 66
URL      : https://tarballs.openstack.org/oslo.log/oslo.log-3.43.0.tar.gz
Source0  : https://tarballs.openstack.org/oslo.log/oslo.log-3.43.0.tar.gz
Source99 : https://tarballs.openstack.org/oslo.log/oslo.log-3.43.0.tar.gz.asc
Summary  : oslo.log library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.log-bin = %{version}-%{release}
Requires: oslo.log-license = %{version}-%{release}
Requires: oslo.log-python = %{version}-%{release}
Requires: oslo.log-python3 = %{version}-%{release}
Requires: debtcollector
Requires: fixtures
Requires: monotonic
Requires: oslo.config
Requires: oslo.context
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: pyinotify
Requires: python-dateutil
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/oslo.log.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package bin
Summary: bin components for the oslo.log package.
Group: Binaries
Requires: oslo.log-license = %{version}-%{release}

%description bin
bin components for the oslo.log package.


%package license
Summary: license components for the oslo.log package.
Group: Default

%description license
license components for the oslo.log package.


%package python
Summary: python components for the oslo.log package.
Group: Default
Requires: oslo.log-python3 = %{version}-%{release}

%description python
python components for the oslo.log package.


%package python3
Summary: python3 components for the oslo.log package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.log package.


%prep
%setup -q -n oslo.log-3.43.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556332141
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.log
cp LICENSE %{buildroot}/usr/share/package-licenses/oslo.log/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/convert-json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.log/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
