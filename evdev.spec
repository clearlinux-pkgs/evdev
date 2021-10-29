#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : evdev
Version  : 1.4.0
Release  : 21
URL      : https://files.pythonhosted.org/packages/4d/ec/bb298d36ed67abd94293253e3e52bdf16732153b887bf08b8d6f269eacef/evdev-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/4d/ec/bb298d36ed67abd94293253e3e52bdf16732153b887bf08b8d6f269eacef/evdev-1.4.0.tar.gz
Summary  : Bindings to the Linux input handling subsystem
Group    : Development/Tools
License  : BSD-3-Clause
Requires: evdev-license = %{version}-%{release}
Requires: evdev-python = %{version}-%{release}
Requires: evdev-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
-------
        
        This package provides bindings to the generic input event interface in
        Linux. The *evdev* interface serves the purpose of passing events
        generated in the kernel directly to userspace through character
        devices that are typically located in ``/dev/input/``.
        
        This package also comes with bindings to *uinput*, the userspace input
        subsystem. *Uinput* allows userspace programs to create and handle
        input devices that can inject events directly into the input
        subsystem.

%package license
Summary: license components for the evdev package.
Group: Default

%description license
license components for the evdev package.


%package python
Summary: python components for the evdev package.
Group: Default
Requires: evdev-python3 = %{version}-%{release}

%description python
python components for the evdev package.


%package python3
Summary: python3 components for the evdev package.
Group: Default
Requires: python3-core
Provides: pypi(evdev)

%description python3
python3 components for the evdev package.


%prep
%setup -q -n evdev-1.4.0
cd %{_builddir}/evdev-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610995184
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
mkdir -p %{buildroot}/usr/share/package-licenses/evdev
cp %{_builddir}/evdev-1.4.0/LICENSE %{buildroot}/usr/share/package-licenses/evdev/4ab6a6236dcbd6da7e9d10d79d9c26d7975d2968
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/evdev/4ab6a6236dcbd6da7e9d10d79d9c26d7975d2968

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
