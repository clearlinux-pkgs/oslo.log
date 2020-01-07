#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4F398DEAE440091C (infra-root@openstack.org)
#
Name     : oslo.log
Version  : 3.45.2
Release  : 74
URL      : https://tarballs.openstack.org/oslo.log/oslo.log-3.45.2.tar.gz
Source0  : https://tarballs.openstack.org/oslo.log/oslo.log-3.45.2.tar.gz
Source1  : https://tarballs.openstack.org/oslo.log/oslo.log-3.45.2.tar.gz.asc
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
BuildRequires : debtcollector
BuildRequires : fixtures
BuildRequires : monotonic
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.i18n
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : pyinotify
BuildRequires : python-dateutil
BuildRequires : six

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
%setup -q -n oslo.log-3.45.2
cd %{_builddir}/oslo.log-3.45.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578326192
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.log
cp %{_builddir}/oslo.log-3.45.2/LICENSE %{buildroot}/usr/share/package-licenses/oslo.log/57aed0b0f74e63f6b85cce11bce29ba1710b422b
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
/usr/share/package-licenses/oslo.log/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
