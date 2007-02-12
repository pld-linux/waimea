Summary:	An X11 window manager designed for maximum efficiency
Summary(pl.UTF-8):	Zarządca okien zaprojektowany pod kątem maksymalnej wydajności
Name:		waimea
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.waimea.org/files/stable/source/%{name}-%{version}.tar.gz
# Source0-md5:	aecdf2ca8e92d8b41b1a2d795553bc12
Source1:	%{name}-xsession.desktop
URL:		http://www.waimea.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib2-devel
BuildRequires:	pkgconfig
BuildRequires:	xft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Celem przy projektowaniu waimea było stworzenie możliwie najbardziej
wydajnego środowiska pracy. Aby osiągnąć to, waimea jest szybkim i
wysoko konfigurowalnym zarządcą okien z wielokrotnymi wirtualnymi
pulpitami. Ma bardzo zaawansowany silnik stylów z możliwościami takimi
jak obsługa stylów blackboksa, pixmapowych i przezroczystych tekstur.
Tekst może być wyświetlany z podwójnym buforowaniem przy użyciu fontów
X i Xft. Waimea zawiera także szybki, lekki system menu z obsługą
dynamicznych menu. Wbudowany system konfiguracji akcji czyni waimea
najbardziej konfigurowalnym zarządcą okien, jaki jest dostępny.
Pozwala użytkownikowi ustawić, by waimea zachowywał się jak dowolny
inny zarządca okien lub na nowe sposoby, nigdy wcześniej nie dostępne.

Dostępne możliwości to:
- wirtualne pulpity
- wielokrotne pulpity
- silnik wyświetlania obrazów Blackboksa (obsługa stylów Blackboksa)
- style pixmapowe
- przezroczyste tekstury dzięki rozszerzeniu Xrender
- system konfiguracji akcji
- zaawansowany system menu (z obsługą dynamicznych menu)
- standardowe fonty X
- fonty Xft (z antyaliasingiem)
- podwójnie buforowany tekst
- system obsługi aplikacji dokowalnych
- przełączanie zadań
- konfigurowalne przyciski na belkach tytułowych
- obsługa KDE3/GNOME2.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-pixmap \
	--enable-randr \
	--enable-render \
	--enable-shape \
	--enable-xft \
	--enable-xinerama

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_datadir}/waimea/{actions,styles,scripts,backgrounds} \
	$RPM_BUILD_ROOT%{_datadir}/xsessions \
	$RPM_BUILD_ROOT%{_mandir}/man1

install src/waimea		$RPM_BUILD_ROOT%{_bindir}
install data/{config,menu}	$RPM_BUILD_ROOT%{_datadir}/waimea
install data/actions/action*	$RPM_BUILD_ROOT%{_datadir}/waimea/actions
install data/backgrounds/*.png	$RPM_BUILD_ROOT%{_datadir}/waimea/backgrounds
install data/scripts/*.pl	$RPM_BUILD_ROOT%{_datadir}/waimea/scripts
install data/styles/*.style	$RPM_BUILD_ROOT%{_datadir}/waimea/styles
install doc/waimea.1		$RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

ln -s action.click-to-focus $RPM_BUILD_ROOT%{_datadir}/waimea/actions/action

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*
