%define fname 	mustux
%define name 	lib%{fname}
%define version 0.20.2
%define release %mkrel 4

%define major 	0
%define libname %mklibname %fname %major
%define libnamedevel %mklibname -d %fname

Summary: 	The libraries need by protux
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{name}-%{version}.tar.gz
Patch0:     libmustux-0.20.1-cpp.patch
License: 	GPL
Group: 		System/Libraries
Url: 		https://www.nongnu.org/protux/
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	qt3-devel
BuildRequires: 	libalsa-devel
BuildRequires:  libogg-devel

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

%package -n %libnamedevel
Summary: The development files from %name
Group: Development/Other
Provides: %name-devel = %version-%release
Requires: %libname = %version-%release

%description -n %libnamedevel
The development files need to build applications which used %name

%prep
%setup -q
%patch0 -p0 -b .cppfix

%build
aclocal
libtoolize --force
automake -a
autoconf
%configure \
    --with-qt-prefix=%_prefix/lib/qt3 \
    --with-qt-lib-dir=%_prefix/lib/qt3/%_lib

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.*

%files -n %libnamedevel
%defattr(-,root,root)
%_bindir/*
%_includedir/*.h
%dir %_includedir/libmustux
%_includedir/libmustux/*
%_libdir/*.la
%_libdir/*.a
%_libdir/*.so
%_datadir/aclocal/mustux.m4
