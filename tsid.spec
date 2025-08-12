Summary:	The Time SID Manager
Name:	tsid
Version:	1.0
Release:	1
Group:	Sound
License:	GPLv2+
Url:		http://tsid.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/tsid/%{name}-%{version}.tar.gz
Patch0:	tsid-1.0-gcc4.patch
BuildRequires:	sidplay-devel

%description
A little library for collecting your time spent listening statistic about
HVSC sids from a sid player, and some programs for extracting and elaborating
these information. So, who is your best sid composer or tune? TSID probably
shows you something interesting...
This package contains the user executable programs.

%files
%doc README AUTHORS COPYING TODO doc/faq.html doc/tupdate.html
%{_bindir}/examiner
%{_bindir}/hvsctest
%{_bindir}/tupdate

#-----------------------------------------------------------------------------

%package -n %{name}-devel
Summary:	Header files for compiling apps that use libtsid
Group:	Development/C++

%description -n %{name}-devel
A little library for collecting your time spent listening statistic about
HVSC sids from a sid player, and some programs for extracting and elaborating
these information. So, who is your best sid composer or tune? TSID probably
shows you something interesting...
This is a developer package containing (only) the static library and the
header files.

%files -n %{name}-devel
%doc history/* doc/inside.html COPYING doc/thvs.txt
%{_libdir}/*.a
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

# Fix wrong perms
find  src/pgr/ -name "*.cpp" -o -name "*.h" | xargs chmod 0644
find  src/tsid/ -name "*.cpp" -o -name "*.h" | xargs chmod 0644


%build
autoreconf -vfi
%configure
%make_build


%install
%make_install
