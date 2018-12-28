#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD113FCAC3C4E599F (Nikolaus@rath.org)
#
Name     : llfuse
Version  : 1.3.5
Release  : 2
URL      : https://files.pythonhosted.org/packages/19/e7/26335a22c776c763d280c2985963cf2f31484b7d05b5d74a08433d08201d/llfuse-1.3.5.tar.bz2
Source0  : https://files.pythonhosted.org/packages/19/e7/26335a22c776c763d280c2985963cf2f31484b7d05b5d74a08433d08201d/llfuse-1.3.5.tar.bz2
Source99 : https://files.pythonhosted.org/packages/19/e7/26335a22c776c763d280c2985963cf2f31484b7d05b5d74a08433d08201d/llfuse-1.3.5.tar.bz2.asc
Summary  : Python bindings for the low-level FUSE API
Group    : Development/Tools
License  : LGPL-2.0
Requires: llfuse-license = %{version}-%{release}
Requires: llfuse-python = %{version}-%{release}
Requires: llfuse-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pkgconfig(fuse)

%description
..
NOTE: We cannot use sophisticated ReST syntax (like
e.g. :file:`foo`) here because this isn't rendered correctly
by PyPi and/or BitBucket.

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

%description python3
python3 components for the llfuse package.


%prep
%setup -q -n llfuse-1.3.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541106123
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/llfuse
cp LICENSE %{buildroot}/usr/share/package-licenses/llfuse/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/llfuse/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
