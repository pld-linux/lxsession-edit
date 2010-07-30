Summary:	Tool to manage desktop session autostarts
Name:		lxsession-edit
Version:	0.1.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	55b4553869209e0932cc73e8daefc854
URL:		http://www.lxde.org/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxsession-edit is a tool used to manage desktop session autostarts,
especially for lxsession lite.

%prep
%setup -q

%build
%configure
touch po/stamp-it
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxsession-edit
%{_desktopdir}/lxsession-edit.desktop
%{_datadir}/lxsession-edit
