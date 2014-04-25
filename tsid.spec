Summary: Time SID Manager

Name:    tsid
Version: 2.0.3
Release: 1
License: GPLv2+
URL: http://tsid.sourceforge.net
Group: Sound
Source: https://sourceforge.net/projects/tsid/files/TSID2/0.3/tsid2-0.3.tar.gz
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
%makeinstall

%clean

%files
%doc README AUTHORS COPYING TODO INSTALL doc/faq.html doc/tupdate.html
%{_bindir}/examiner
%{_bindir}/hvsctest
%{_bindir}/tupdate

%files -n %{name}-devel
%doc history/* doc/inside.html COPYING doc/thvs.txt
%{_libdir}/*.a
%{_includedir}/%{name}/*
%dir %{_includedir}/%{name}




