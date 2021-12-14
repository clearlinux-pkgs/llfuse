#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x243ACFA951F78E01 (tw-public@gmx.de)
#
Name     : llfuse
Version  : 1.4.1
Release  : 26
URL      : https://files.pythonhosted.org/packages/b1/d4/44443fbaac6d5b878da99e7c0948ee93c7934fa3b00e48c5363823b583d0/llfuse-1.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b1/d4/44443fbaac6d5b878da99e7c0948ee93c7934fa3b00e48c5363823b583d0/llfuse-1.4.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/b1/d4/44443fbaac6d5b878da99e7c0948ee93c7934fa3b00e48c5363823b583d0/llfuse-1.4.1.tar.gz.asc
Summary  : Python bindings for the low-level FUSE API
Group    : Development/Tools
License  : LGPL-2.0
Requires: llfuse-license = %{version}-%{release}
Requires: llfuse-python = %{version}-%{release}
Requires: llfuse-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pkgconfig(fuse)
BuildRequires : python3-dev

%description
..
NOTE: We cannot use sophisticated ReST syntax (like
e.g. :file:`foo`) here because this isn't rendered correctly
by PyPi.

%package license
Summary: license components for the llfuse package.
Group: Default

%description license
license components for the llfuse package.


%package python
Summary: python components for the llfuse package.
Group: Default
Requires: llfuse-python3 = %{version}-%{release}

%description python
python components for the llfuse package.


%package python3
Summary: python3 components for the llfuse package.
Group: Default
Requires: python3-core
Provides: pypi(llfuse)

%description python3
python3 components for the llfuse package.


%prep
%setup -q -n llfuse-1.4.1
cd %{_builddir}/llfuse-1.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635751345
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/llfuse
cp %{_builddir}/llfuse-1.4.1/LICENSE %{buildroot}/usr/share/package-licenses/llfuse/a942fd86faab764d64db3aacfdc7af285c7d15ba
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/llfuse/a942fd86faab764d64db3aacfdc7af285c7d15ba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
