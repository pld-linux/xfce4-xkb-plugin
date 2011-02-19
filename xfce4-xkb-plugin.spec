Summary:	Displays and switched the current keyboard layout
Summary(pl.UTF-8):	Wyświetlanie i przełączanie bieżącego układu klawiatury
Name:		xfce4-xkb-plugin
Version:	0.5.3.3
Release:	7
License:	BSD-like
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-xkb-plugin/%{name}-%{version}.tar.gz
# Source0-md5:	b233cc9de1cbace075eaf6e2c9a8e685
Patch0:		%{name}-xklavier-api.patch
Patch1:		%{name}-libxklavier5.patch
Patch2:		%{name}-ui.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	librsvg-devel >= 2.18.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.12.0
BuildRequires:	libxklavier-devel >= 4.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin displays and switched the current keyboard layouts. The
new version can display the layout as text label and also as an image
of the corresponding country's flag.

%description -l pl.UTF-8
Ta wtyczka wyświetla i przełącza bieżący układ klawiatury. Nowa wersja
potrafi wyświetlać układ jako etykietkę tekstową albo jako grafikę
przedstawiającą flagę narodową.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-xkb-plugin
%{_datadir}/xfce4/panel-plugins/xkb-plugin.desktop
%{_datadir}/xfce4/xkb
