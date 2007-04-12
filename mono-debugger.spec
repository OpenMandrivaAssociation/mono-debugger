%define name	mono-debugger
%define version	0.31
%define release	%mkrel 1
%define major 0
%define libname %mklibname %name %major
%define monodir %_prefix/lib/mono

Summary:	Mono Debugger
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Development/Other
Source0:	http://go-mono.com/sources/mono-debugger/%name-%version.tar.bz2
Patch1: mono-debugger-0.11-dllmap.patch
URL:		http://www.go-mono.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	mono-devel > 1.1.15
BuildRequires:	libreadline-devel
BuildRequires:  termcap-devel
BuildRequires:	automake1.9
Requires:	mono
Requires: %libname >= %version

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
aclocal-1.9
autoconf
automake-1.9 -a -c

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall
install -m 644 wrapper/mdb.exe.config %buildroot%monodir/1.0/

%clean
rm -rf %{buildroot}

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-, root, root)
%{_bindir}/*
%monodir/*
%doc AUTHORS README README.build TODO NEWS ChangeLog RELEASE-NOTES*

%files -n %libname
%defattr(-, root, root)
%_libdir/lib*.so.%{major}*

%files -n %libname-devel
%defattr(-, root, root)
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*a
%{_libdir}/pkgconfig/*


