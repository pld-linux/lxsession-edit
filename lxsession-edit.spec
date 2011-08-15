#
# Conditional build:
%bcond_with		gtk3		# build GTK+3 disables GTK+2
%bcond_without		gtk2	# build with GTK+2

%if %{with gtk3}
%undefine	with_gtk2
%endif

Summary:	Tool to manage desktop session autostarts
Name:		lxsession-edit
Version:	0.2.0
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	1e763a9b7f297ba964cd41b30edfccd7
URL:		http://www.lxde.org/
BuildRequires:	gettext-devel
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxsession-edit is a tool used to manage desktop session autostarts,
especially for lxsession lite.

%prep
%setup -q

%build
%configure \
	%{?with_gtk3:--enable-gtk3}
touch po/stamp-it
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ur_PK,tt_RU}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxsession-edit
%{_desktopdir}/lxsession-edit.desktop
%{_datadir}/lxsession-edit
