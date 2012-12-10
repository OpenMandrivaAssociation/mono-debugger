%define name	mono-debugger
%define version	2.10
%define release	%mkrel 2
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
Patch0: mono-debugger-2.10-glib-includes.patch
Patch1: mono-debugger-2.2-dllmap.patch
URL:		http://www.go-mono.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	mono-devel >= 2.10
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
%apply_patches

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
%{_libdir}/pkgconfig/*




%changelog
* Mon Feb 20 2012 GÃ¶tz Waschk <waschk@mandriva.org> 2.10-2mdv2012.0
+ Revision: 777953
- remove libtool archive
- fix glib includes
- rebuild

* Thu Feb 17 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.10-1
+ Revision: 638201
- new version
- bump mono dep

* Sat Nov 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.1-1mdv2011.0
+ Revision: 601733
- new version
- drop patch 2

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8-3mdv2011.0
+ Revision: 587887
- P2: security fix for CVE-2010-3369 (debian)

* Thu Oct 07 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.8-2mdv2011.0
+ Revision: 584074
- update build deps
- rebuild for new mono

* Thu Oct 07 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.8-1mdv2011.0
+ Revision: 583939
- update to new version 2.8

* Tue Mar 16 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.3-1mdv2010.1
+ Revision: 521513
- update to new version 2.6.3

* Tue Dec 15 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.6-1mdv2010.1
+ Revision: 478867
- update to new version 2.6

* Thu Dec 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.4.3-1mdv2010.1
+ Revision: 475972
- new version
- disable parallel build

* Thu Jul 09 2009 Funda Wang <fwang@mandriva.org> 2.4.2.1-1mdv2010.0
+ Revision: 393749
- New version 2.4.2.1

* Tue Jun 30 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.4.2-1mdv2010.0
+ Revision: 390913
- update to new version 2.4.2

* Fri Apr 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.4-1mdv2010.0
+ Revision: 368974
- new version

* Thu Mar 05 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.2-2mdv2009.1
+ Revision: 349356
- fix build
- update dll mapping for bug #48495

* Wed Jan 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.2-1mdv2009.1
+ Revision: 329396
- update to new version 2.2

* Sat Oct 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.0-1mdv2009.1
+ Revision: 292255
- new version
- update deps
- fix build
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.60-2mdv2008.1
+ Revision: 134332
- fix automatic deps

* Wed Dec 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.60-1mdv2008.1
+ Revision: 133870
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.50-1mdv2008.0
+ Revision: 27607
- new version
- bump deps


* Wed Nov 22 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.31-1mdv2007.0
+ Revision: 86340
- Import mono-debugger

* Wed Nov 22 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.31-1mdv2007.1
- New version 0.31

* Sat Jul 29 2006 Götz Waschk <waschk@mandriva.org> 0.30-1mdv2007.0
- source URL
- New release 0.30

* Sat Jul 08 2006 Götz Waschk <waschk@mandriva.org> 0.20-1mdv2007.0
- bump deps
- drop patches 0,2
- New release 0.20

* Mon Mar 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.12-1mdk
- New release 0.12

* Thu Feb 02 2006 Götz Waschk <waschk@mandriva.org> 0.11-2mdk
- fix build

* Tue Dec 20 2005 Götz Waschk <waschk@mandriva.org> 0.11-1mdk
- update file list
- bump deps
- update patch 1
- new version

* Tue Jun 21 2005 Götz Waschk <waschk@mandriva.org> 0.10-0.46231.1mdk
- new snapshot

* Sat Jun 18 2005 Götz Waschk <waschk@mandriva.org> 0.10-0.45941.1mdk
- bump deps
- rediff patch 2
- new snapshot

* Fri Jun 03 2005 Götz Waschk <waschk@mandriva.org> 0.9-0.45318.2mdk
- patch to fix test on x86_64
- no more excusivearch

* Fri Jun 03 2005 Götz Waschk <waschk@mandriva.org> 0.9-0.45318.1mdk
- fix buildrequires
- new snapshot

* Wed Jun 01 2005 Götz Waschk <waschk@mandriva.org> 0.9-0.44840.4mdk
- fix buildrequires

* Tue May 31 2005 Götz Waschk <waschk@mandriva.org> 0.9-0.44840.3mdk
- fix deps again

* Tue May 31 2005 Götz Waschk <waschk@mandriva.org> 0.9-0.44840.2mdk
- fix dll maps
- fix deps

* Tue May 31 2005 Götz Waschk <waschk@mandriva.org> 0.9-0.44840.1mdk
- initial mdk package

* Tue Dec 09 2003 Martin Baulig <martin@ximian.com> 0.5-1
- initial release

