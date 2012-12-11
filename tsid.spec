%define name tsid
%define version 0.9
%define release %mkrel 9

Summary: TSID: Time SID Manager
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
URL: http://tsid.sourceforge.net
Group: Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: http://prdownloads.sourceforge.net/tsid/%name-%version.tar.bz2
Patch: tsid-0.9-gcc4.patch
BuildRequires: sidplay-devel

%description
TSID is a library for collecting your time spent listening statistic about
HVSC sids from a sid player, and some programs for extracting and elaborating
these information. So, who is your best sid composer or tune? TSID probably
shows you something interesting...
This is a package with user executable programs.

%package -n %{name}-devel
Summary: Header files for compiling apps that use libtsid
Group: Development/C++

%description -n %{name}-devel
TSID is a library for collecting your time spent listening statistic about
HVSC sids from a sid player, and some programs for extracting and elaborating
these information. So, who is your best sid composer or tune? TSID probably
shows you something interesting...
This is a developer package containing the static library and header files.

%prep
%setup -q
%patch -p1 -b .gcc4

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING TODO INSTALL doc/faq.html doc/tupdate.html
%{_bindir}/examiner
%{_bindir}/hvsctest
%{_bindir}/tupdate

%files -n %{name}-devel
%defattr(-,root,root)
%doc history/* doc/inside.html COPYING doc/thvs.txt
%{_libdir}/*.a
%{_includedir}/%{name}/*
%dir %{_includedir}/%{name}



%changelog
* Thu Dec 08 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.9-9mdv2012.0
+ Revision: 738853
- yearly rebuild

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-8mdv2011.0
+ Revision: 615275
- the mass rebuild of 2010.1 packages

* Fri Mar 12 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.9-7mdv2010.1
+ Revision: 518420
- remove debug files from the devel package

* Fri Jul 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.9-6mdv2009.0
+ Revision: 238101
- update the patch
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Wed Jan 02 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.9-5mdv2008.1
+ Revision: 140367
- patch for gcc 4

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel


* Tue Jul 05 2005 Lenny Cartier <lenny@mandriva.com> 0.9-3mdk
- rebuild

* Fri Jun 04 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9-2mdk
- patch for new g++

* Mon May 31 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9-1mdk
- fix configure call
- New release 0.9

* Wed May 26 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8-4mdk
- drop prefix
- buildrequires sidplay-devel, not to be confused with sidplay2-devel

* Wed May 26 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.8-3mdk
- rebuild
- adjust buildrequires

* Wed Mar 12 2003 Götz Waschk <waschk@linux-mandrake.com> 0.8-2mdk
- fix buildrequires

* Sat Dec 21 2002 Götz Waschk <waschk@linux-mandrake.com> 0.8-1mdk
- new version

* Fri Aug 16 2002 Götz Waschk <waschk@linux-mandrake.com> 0.7-2mdk
- rebuild with gcc 3.2-0.3mdk

* Wed Jul 31 2002 Götz Waschk <waschk@linux-mandrake.com> 0.7-1mdk
- new version

* Tue Feb 05 2002 Götz Waschk <waschk@linux-mandrake.com> 0.6-1mdk
- 0.6

* Wed Jan 02 2002 Götz Waschk <waschk@linux-mandrake.com> 0.5-1mdk
- updated URL
- 0.5

* Wed Oct 03 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4-1mdk
- updated by Götz Waschk <waschk@linux-mandrake.com> :
	- 0.4

* Wed Sep 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3-2mdk
- rebuild

* Tue Mar 27 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3-1mdk
- updated to 0.3 by  Götz Waschk <waschk@linux-mandrake.com> :
	- 0.3
	- added new programs to tsid package
	- updated %%doc section

* Tue Feb 13 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2-1mdk
- used srpm from Götz Waschk <waschk@linux-mandrake.com> :
	- adapted package by Stefano Tognon <ice00@users.sourceforge.net>

