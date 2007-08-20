%define name tsid
%define version 0.9
%define release %mkrel 3

Summary: TSID: Time SID Manager
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
URL: http://tsid.sourceforge.net
Group: Sound
Source: http://prdownloads.sourceforge.net/tsid/%name-%version.tar.bz2
Patch: tsid-0.9-gcc3.4.patch
BuildRoot: %{_tmppath}/tsid-build
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
%patch -p1

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
%{_libdir}/*
%{_includedir}/%{name}/*
%dir %{_includedir}/%{name}

