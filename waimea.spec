Summary:	An X11 window manager designed for maximum efficiency
Summary(pl):	Zarz±dca okien zaprojektowany pod k±tem maksymalnej wydajno¶ci
Name:		waimea
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.waimea.org/files/stable/source/%{name}-%{version}.tar.gz
URL:		http://www.waimea.org/
BuildRequires:	Xft-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The design goal for waimea is to create the most efficient desktop
working environment available. To achieve this waimea is a fast and
highly customizable virtual multiple desktop window manager. It has a
very advanced style engine with features like blackbox style support,
pixmap style support and transparent textures. Text can be rendered
double buffered using both X core fonts and Xft fonts. Waimea also
includes a fast lightweight menu system with dynamic menus support.
The built in action configuration system makes waimea the most
configurable window manager available. It allows the user to set up
waimea to behave as any other window manager or in new ways never
before possible.

Features already included are:

    - Virtual desktop
    - Multiple desktops
    - Blackbox image rendering engine (blackbox style support)
    - Pixmap styles
    - Translucent textures using Xrender extension
    - Action Configuration System
    - Advanced Menu System (with dynamic menus support)
    - Standard X core fonts
    - Xft fonts (anti-aliased fonts)
    - Double buffered text
    - Dockapp handler system
    - Task switcher
    - Configurable titlebar buttons
    - KDE3/GNOME2 support

%description -l pl
Celem przy projektowaniu waimea by³o stworzenie mo¿liwie najbardziej
wydajnego ¶rodowiska pracy. Aby osi±gn±æ to, waimea jest szybkim i
wysoko konfigurowalnym zarz±dc± okien z wielokrotnymi wirtualnymi
pulpitami. Ma bardzo zaawansowany silnik stylów z mo¿liwo¶ciami takimi
jak obs³uga stylów blackboksa, pixmapowych i przezroczystych tekstur.
Tekst mo¿e byæ wy¶wietlany z podwójnym buforowaniem przy u¿yciu fontów
X i Xft. Waimea zawiera tak¿e szybki, lekki system menu z obs³ug±
dynamicznych menu. Wbudowany system konfiguracji akcji czyni waimea
najbardziej konfigurowalnym zarz±dc± okien, jaki jest dostêpny.
Pozwala u¿ytkownikowi ustawiæ, by waimea zachowywa³ siê jak dowolny
inny zarz±dca okien lub na nowe sposoby, nigdy wcze¶niej nie dostêpne.

Dostêpne mo¿liwo¶ci to:
 - wirtualne pulpity
 - wielokrotne pulpity
 - silnik wy¶wietlania obrazów Blackboksa (obs³uga stylów Blackboksa)
 - style pixmapowe
 - przezroczyste tekstury dziêki rozszerzeniu Xrender
 - system konfiguracji akcji
 - zaawansowany system menu (z obs³ug± dynamicznych menu)
 - standardowe fonty X
 - fonty Xft (z antyaliasingiem)
 - podwójnie buforowany tekst
 - system obs³ugi aplikacji dokowalnych
 - prze³±czanie zadañ
 - konfigurowalne przyciski na belkach tytu³owych
 - obs³uga KDE3/GNOME2.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/waimea/{actions,styles,scripts,backgrounds},%{_mandir}/man1}

install src/waimea		$RPM_BUILD_ROOT%{_bindir}
install data/{config,menu}	$RPM_BUILD_ROOT%{_datadir}/waimea
install data/actions/action*	$RPM_BUILD_ROOT%{_datadir}/waimea/actions
install data/backgrounds/*.png	$RPM_BUILD_ROOT%{_datadir}/waimea/backgrounds
install data/scripts/*.pl	$RPM_BUILD_ROOT%{_datadir}/waimea/scripts
install data/styles/*.style	$RPM_BUILD_ROOT%{_datadir}/waimea/styles
install doc/waimea.1		$RPM_BUILD_ROOT%{_mandir}/man1

(cd $RPM_BUILD_ROOT%{_datadir}/waimea/actions; ln -sf action.click-to-focus action)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
