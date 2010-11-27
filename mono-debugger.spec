%define name	mono-debugger
%define version	2.8.1
%define release	%mkrel 1
%define major 0
%define libname %mklibname %name %major
%define monodir %_prefix/lib/mono

Summary:	Mono Debugger
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+ and MIT
Group:		Development/Other
Source0:	http://go-mono.com/sources/mono-debugger/%name-%version.tar.bz2
Patch1: mono-debugger-2.2-dllmap.patch
URL:		http://www.go-mono.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	mono-devel >= 2.0
#gw not required by mono 2.8 anymore:
BuildRequires:	glib2-devel
BuildRequires:	libreadline-devel
BuildRequires:  termcap-devel
BuildRequires:	automake1.9
Requires:	mono
Requires: %libname >= %version
%define _requires_exceptions libmonodebuggerreadline

%description
The Mono Debugger

%package -n %libname
Group: System/Libraries
Summary: Shared libraries of the Mono Debugger

%description -n %libname
This contains shared libraries used by the Mono Debugger

%package -n %libname-devel
Group: Development/Other
Summary: Headers of the Mono Debugger
Provides: lib%name-devel = %version-%release
Requires: %libname = %version
Requires: %name = %version

%description -n %libname-devel
This contains headers and libraries of the Mono Debugger.


%prep
%setup -q
%patch1 -p1 -b .dllmap

%build
%define _disable_ld_no_undefined 1
%configure2_5x
#gw parallel build broken in 2.4.3
make

%install
rm -rf %{buildroot}
%makeinstall
install -m 644 wrapper/mdb.exe.config %buildroot%monodir/2.0/

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-, root, root)
%{_bindir}/*
%monodir/*
%doc AUTHORS README NEWS ChangeLog

%files -n %libname
%defattr(-, root, root)
%_libdir/lib*.so.%{major}*

%files -n %libname-devel
%defattr(-, root, root)
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*a
%{_libdir}/pkgconfig/*


