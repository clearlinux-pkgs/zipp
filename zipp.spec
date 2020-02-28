#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zipp
Version  : 3.0.0
Release  : 13
URL      : https://files.pythonhosted.org/packages/42/09/bb2a28216f9572da61a2c56c6d5bf6d8c011371d8268f42a9ca5a4cbaf40/zipp-3.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/42/09/bb2a28216f9572da61a2c56c6d5bf6d8c011371d8268f42a9ca5a4cbaf40/zipp-3.0.0.tar.gz
Summary  : Backport of pathlib-compatible object wrapper for zip files
Group    : Development/Tools
License  : MIT
Requires: zipp-license = %{version}-%{release}
Requires: zipp-python = %{version}-%{release}
Requires: zipp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools_scm-python
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/zipp.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/zipp.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/zipp

.. image:: https://dev.azure.com/jaraco/zipp/_apis/build/status/jaraco.zipp?branchName=master
   :target: https://dev.azure.com/jaraco/zipp/_build/latest?definitionId=1&branchName=master

.. image:: https://img.shields.io/travis/jaraco/zipp/master.svg
   :target: https://travis-ci.org/jaraco/zipp

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. image:: https://img.shields.io/appveyor/ci/jaraco/zipp/master.svg
   :target: https://ci.appveyor.com/project/jaraco/zipp/branch/master

.. .. image:: https://readthedocs.org/projects/zipp/badge/?version=latest
..    :target: https://zipp.readthedocs.io/en/latest/?badge=latest


A pathlib-compatible Zipfile object wrapper. A backport of the
`Path object <https://docs.python.org/3.8/library/zipfile.html#path-objects>`_.

%package license
Summary: license components for the zipp package.
Group: Default

%description license
license components for the zipp package.


%package python
Summary: python components for the zipp package.
Group: Default
Requires: zipp-python3 = %{version}-%{release}

%description python
python components for the zipp package.


%package python3
Summary: python3 components for the zipp package.
Group: Default
Requires: python3-core
Provides: pypi(zipp)

%description python3
python3 components for the zipp package.


%prep
%setup -q -n zipp-3.0.0
cd %{_builddir}/zipp-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582848954
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
mkdir -p %{buildroot}/usr/share/package-licenses/zipp
cp %{_builddir}/zipp-3.0.0/LICENSE %{buildroot}/usr/share/package-licenses/zipp/8e6689d37f82d5617b7f7f7232c94024d41066d1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zipp/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
