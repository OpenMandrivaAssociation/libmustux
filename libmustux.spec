%define fname 	mustux
%define name 	lib%{fname}
%define version 0.20.1
%define release %mkrel 3

%define major 	0
%define libname %mklibname %fname %major

Summary: 	The libraries need by protux
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{name}-%{version}.tar.bz2
Patch0:     libmustux-0.20.1-cpp.patch
License: 	GPL
Group: 		System/Libraries
Url: 		http://www.nongnu.org/protux/
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	qt3-devel
BuildRequires: 	libalsa-devel

%description
The libraries need by protux

Protux aims to be the most practical and one of the most powerful
audio tools for GNU/Linux. Protux will allow you to use the power
of keyboard+mouse combination (with no clicks) to vastly speed up
the process of audio production.
This concept we call "Jog-Mouse-Board" or JMB, for short.

%package -n %libname
Summary: The libraries need by protux
Group: System/Libraries
Provides: %name = %version-%release

%description -n %libname
The libraries need by protux

Protux aims to be the most practical and one of the most powerful
audio tools for GNU/Linux. Protux will allow you to use the power
of keyboard+mouse combination (with no clicks) to vastly speed up
the process of audio production.
This concept we call "Jog-Mouse-Board" or JMB, for short.

%package -n %libname-devel
Summary: The development files from %name
Group: Development/Other
Provides: %name-devel = %version-%release
Requires: %libname = %version-%release

%description -n %libname-devel
The development files need to build applications which used %name

%prep
%setup -q
%patch0 -p0 -b .cppfix

%build
aclocal
automake -a
autoconf
%configure \
    --with-qt-prefix=%_prefix/lib/qt3 \
    --with-qt-lib-dir=%_prefix/lib/qt3/%_lib

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%_bindir/*
%_includedir/*.h
%dir %_includedir/libmustux
%_includedir/libmustux/*
%_libdir/*.la
%_libdir/*.a
%_libdir/*.so
%_datadir/aclocal/mustux.m4


* Wed Jun 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.20.1-2mdk
- reenable libtoolize
- rebuild for new g++

* Thu Apr 1 2004 Austin Acton <austin@mandrake.org> 0.20.1-1mdk
- 0.20.1

* Mon Oct 13 2003 Austin Acton <aacton@yorku.ca> 0.18.0-1mdk
- 0.18.0
- don't use configure macro

* Sat May 03 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.16.0-3mdk
- fix build

* Sat May 03 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.16.0-2mdk
- fix missing link in %%_libdir

* Sat May 03 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.16.0-1mdk
- initial mdk package 
