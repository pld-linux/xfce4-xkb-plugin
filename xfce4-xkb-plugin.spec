Summary:	Displays and switched the current keyboard layout
Summary(pl):	Wy¶wietla i prze³±cza bie¿±cy uk³ad klawiatury
Name:		xfce4-xkb-plugin
Version:	0.3.2
Release:	1
License:	BSD-like
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	b233819d685ab3b7f4a47c2da9fb6936
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.0
Requires:	xfce4-panel >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin displays and switched the current keyboard layouts. The
new version can display the layout as text label and also as an image
of the corresponding country's flag.

%description -l pl
Wtyczka wy¶wietla i prze³±cza bie¿±cy uk³ad klawiatury. Nowa wersja
portafi wy¶wietlaæ uk³ad jako etykietkê tekstow± albo jako grafikê
przedstawiaj±c± flagê narodow±.

%prep
%setup -q

%build
cp -f %{_datadir}/automake/config.sub .
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
%{_datadir}/xfce4/xkb/flags/*
