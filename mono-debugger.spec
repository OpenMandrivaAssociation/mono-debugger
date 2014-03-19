%define major 0
%define libname %mklibname monodebuggerserver %{major}
%define devname %mklibname %{name} -d

%define monodir %{_prefix}/lib/mono

Summary:	Mono Debugger
Name:		mono-debugger
Version:	2.10
Release:	3
License:	GPLv2+ and MIT
Group:		Development/Other
Url:		http://www.go-mono.com/
Source0:	http://go-mono.com/sources/mono-debugger/%{name}-%{version}.tar.bz2
Patch0:		mono-debugger-2.10-glib-includes.patch
Patch1:		mono-debugger-2.2-dllmap.patch
BuildRequires:	readline-devel
BuildRequires:	termcap-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(mono)
Requires:	mono
Requires:	%{libname} = %{EVRD}

%description
The Mono Debugger.

%files
%doc AUTHORS README NEWS ChangeLog
%{_bindir}/*
%{monodir}/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared libraries of the Mono Debugger
Group:		System/Libraries
Obsoletes:	%{_lib}mono-debugger0 < 2.10-3
Conflicts:	%{_lib}mono-debugger0 < 2.10-3

%description -n %{libname}
This contains shared libraries used by the Mono Debugger.

%files -n %{libname}
%{_libdir}/libmonodebuggerserver.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers of the Mono Debugger
Group:		Development/Other
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{_lib}mono-debugger0-devel < 2.10-3
Conflicts:	%{_lib}mono-debugger0-devel < 2.10-3

%description -n %{devname}
This contains headers and libraries of the Mono Debugger.

%files -n %{devname}
%{_libdir}/libmonodebuggerserver.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%define _disable_ld_no_undefined 1
%configure2_5x
#gw parallel build broken in 2.4.3
make

%install
%makeinstall_std
install -m 644 wrapper/mdb.exe.config %{buildroot}%{monodir}/2.0/

