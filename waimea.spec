Summary:	An X11 window manager designed for maximum efficiency
Summary(pl):	Mened¿er okien zaprojektowany na maksymaln± wydajno¶æ
Name:		waimea
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.waimea.org/files/stable/source/%{name}-%{version}.tar.gz
URL:		www.waimea.org
BuildRequires:	imlib2-devel
BuildRequires:	Xft-devel
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
