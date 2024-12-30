Summary:	Displays and switched the current keyboard layout
Summary(pl.UTF-8):	Wyświetlanie i przełączanie bieżącego układu klawiatury
Name:		xfce4-xkb-plugin
Version:	0.8.5
Release:	1
License:	BSD-like
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-xkb-plugin/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	17f57a110c5f08532c33729e603fca98
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
BuildRequires:	garcon-devel >= 4.16.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	librsvg-devel >= 2.40.0
BuildRequires:	libwnck-devel >= 3.14.0
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.16.0
BuildRequires:	libxklavier-devel >= 5.3
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
BuildRequires:	xfconf-devel >= 4.16.0
Requires:	xfce4-panel >= 4.16.0
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

%build
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

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hye,ie,ur_PK,uz@Latn}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libxkb.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libxkb.so
%{_datadir}/xfce4/panel/plugins/xkb.desktop
%{_datadir}/xfce4/xkb
%{_iconsdir}/hicolor/*x*/apps/org.xfce.panel.xkb.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.panel.xkb.svg
