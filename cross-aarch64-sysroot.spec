# spec file for cross-chroot accelerator
#
# Copyright (c) 2010  Jan-Simon Möller (jsmoeller@linuxfoundation.org)
#
Name:           cross-aarch64-sysroot
ExclusiveArch:  %ix86 x86_64
AutoReqProv:    0
AutoReqProv:    off
Version:        1.0+git6
Release:        1
Source101:      precheckin.sh
License:        GPL v2 or later
Group:          Development/Tools/Building
Summary:        This provides the sysroot file structure
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:  tar

%description
Needed for cross-build on x86 side to host the aarch64 cross sysroot

%prep

%build

%install
#rpm -ql filesystem is too much.
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu/sys-root
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu/sys-root/etc
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu/sys-root/dev
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu/sys-root/proc
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu/sys-root/sys
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu/sys-root/bin
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu/sys-root/lib
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu/sys-root/sbin
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu/sys-root/usr/bin
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu/sys-root/usr/lib
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu/sys-root/usr/sbin
mkdir -p %buildroot/opt/cross/aarch64-%{_vendor}-linux-gnu/sys-root/usr/include

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/opt/cross
