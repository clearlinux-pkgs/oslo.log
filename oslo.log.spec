#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEB6CCA1483FA74EC (infra-root@openstack.org)
#
Name     : oslo.log
Version  : 3.25.0
Release  : 48
URL      : https://tarballs.openstack.org/oslo.log/oslo.log-3.25.0.tar.gz
Source0  : https://tarballs.openstack.org/oslo.log/oslo.log-3.25.0.tar.gz
Source99 : https://tarballs.openstack.org/oslo.log/oslo.log-3.25.0.tar.gz.asc
Summary  : oslo.log library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.log-bin
Requires: oslo.log-python
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
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/badges/oslo.log.svg
:target: https://governance.openstack.org/reference/tags/index.html

%package bin
Summary: bin components for the oslo.log package.
Group: Binaries

%description bin
bin components for the oslo.log package.


%package python
Summary: python components for the oslo.log package.
Group: Default

%description python
python components for the oslo.log package.


%prep
%setup -q -n oslo.log-3.25.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492457603
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1492457603
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/convert-json

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
