# spec file for cross-chroot accelerator
#
# Copyright (c) 2010  Jan-Simon Möller (jsmoeller@linuxfoundation.org)
#
Name:           cross-@TARGET_CPU@-sysroot
ExclusiveArch:  none
AutoReqProv:    0
AutoReqProv:    off
Version:        1.0+git6
Release:        1
Source101:      precheckin.sh
License:        GPL v2 or later
Group:          Development/Tools/Building
Summary:        This provides the sysroot file structure
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:  -rpmlint-Factory -rpmlint-mini -post-build-checks tar

%description
Needed for cross-build on x86 side to host the @TARGET_CPU@ cross sysroot

%prep

%build

%install
#rpm -ql filesystem is too much.
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@/sys-root
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@/sys-root/etc
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@/sys-root/dev
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@/sys-root/proc
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@/sys-root/sys
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@/sys-root/bin
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@/sys-root/lib
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@/sys-root/sbin
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@/sys-root/usr/bin
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@/sys-root/usr/lib
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@/sys-root/usr/sbin
mkdir -p %buildroot/opt/cross/@TARGET_CPU@-%{_vendor}-linux-@GNU@/sys-root/usr/include

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/opt/cross
