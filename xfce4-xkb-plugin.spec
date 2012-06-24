Summary:	Displays and switched the current keyboard layout
Summary(pl):	Wy�wietlanie i prze��czanie bie��cego uk�adu klawiatury
Name:		xfce4-xkb-plugin
Version:	0.4.3
Release:	1
License:	BSD-like
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-xkb-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	e0375158339672f49c9e48a8b4669592
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin displays and switched the current keyboard layouts. The
new version can display the layout as text label and also as an image
of the corresponding country's flag.

%description -l pl
Ta wtyczka wy�wietla i prze��cza bie��cy uk�ad klawiatury. Nowa wersja
potrafi wy�wietla� uk�ad jako etykietk� tekstow� albo jako grafik�
przedstawiaj�c� flag� narodow�.

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

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-xkb-plugin
%{_datadir}/xfce4/panel-plugins/xkb-plugin.desktop
%{_datadir}/xfce4/xkb
