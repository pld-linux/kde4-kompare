#
# TODO:
# - add man files
#
%define		orgname		kompare
%define		_state		stable
%define		qtver		4.8.1

Summary:	Kompare - a program to view the differences between files
Summary(pl.UTF-8):	Kompare - program służący do porównywania zmian między plikami
Name:		kde4-%{orgname}
Version:	4.12.2
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	0f4c455d0a7137f797e5496120b88a0b
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	db-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	kde4-libkomparediff2-devel >= %{version}
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-mime-info
BuildRequires:	utempter-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXtst-devel
Obsoletes:	kde4-kdesdk-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kompare is a program to view the differences between files. Features
include:

  - comparison of files or directories via a graphical interface
  - bezier-based connection widget lets you see both source and
    destination as they really appear
  - graphical viewing of patch files in normal, context, unified and
    diff formats
  - interactive application of differences
  - full network transparency
  - ability to view plain-text diff output in embedded viewer
  - easy navigation of multiple-file diffs with dockable navigation tree
  - graphical interface to commonly used diff command line options
  - switch source and destination with one command
  - diff statistics

%description -l pl.UTF-8
Kompare to program służący do porównywania zmian między plikami.
Aktualnie dostępne funkcje:
  - porównanie plików lub katalogów poprzez graficzny interfejs
  - przedstawienie źródła i celu za pomocą krzywej Beziera
  - graficzne przeglądanie łat w formatach diff, unidiff, context i
    zwykłym
  - interaktywne wprowadzanie zmian
  - przezroczystość sieciowa
  - możliwość oglądania wyjścia diff w wewnętrznej przeglądarce
  - łatwa nawigacja między wieloplikowymi diffami wraz z dokowalnym
    drzewem
  - zamiana źródła i celu za pomocą pojedynczej komendy
  - statystyki diffów

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang	%{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kompare
%attr(755,root,root) %ghost %{_libdir}/libkompareinterface.so.?
%attr(755,root,root) %{_libdir}/libkompareinterface.so.*.*.*
%attr(755,root,root) %{_libdir}/libkompareinterface.so
%attr(755,root,root) %ghost %{_libdir}/libkomparedialogpages.so.?
%attr(755,root,root) %{_libdir}/libkomparedialogpages.so.*.*.*
%attr(755,root,root) %{_libdir}/libkomparedialogpages.so
%attr(755,root,root) %{_libdir}/kde4/komparenavtreepart.so
%attr(755,root,root) %{_libdir}/kde4/komparepart.so
%{_datadir}/apps/kompare*
%{_datadir}/kde4/services/kompare*.desktop
%{_datadir}/kde4/servicetypes/kompare*.desktop
%{_desktopdir}/kde4/kompare.desktop
%{_iconsdir}/*/*/*/kompare.*
%{_includedir}/kompare
