Summary:	Displays and switched the current keyboard layout
Summary(pl.UTF-8):	Wyświetlanie i przełączanie bieżącego układu klawiatury
Name:		xfce4-xkb-plugin
Version:	0.7.0
Release:	2
License:	BSD-like
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-xkb-plugin/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	7fbc3d8c84d6662d819dd1803f0fee34
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
BuildRequires:	garcon-devel
BuildRequires:	gettext-tools
BuildRequires:	librsvg-devel >= 2.18.0
BuildRequires:	libwnck-devel >= 2.12.0
BuildRequires:	libxklavier-devel >= 4.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.11.0
BuildRequires:	xfce4-panel-devel >= 4.11.0
Requires:	xfce4-panel >= 4.11.0
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
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-xkb-plugin
%{_datadir}/xfce4/panel-plugins/xkb-plugin.desktop
%{_datadir}/xfce4/xkb
