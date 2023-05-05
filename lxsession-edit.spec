# NOTE: obsoleted by lxsession >= 0.4.9+
#
# Conditional build:
%bcond_with	gtk3	# use GTK+3 instead of GTK+2

Summary:	Tool to manage desktop session autostarts
Summary(pl.UTF-8):	Narzędzie do zarządzania automatycznym startem sesji środowiska graficznego
Name:		lxsession-edit
Version:	0.2.0
Release:	2.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	1e763a9b7f297ba964cd41b30edfccd7
URL:		http://www.lxde.org/
BuildRequires:	gettext-tools
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool
BuildRequires:	pkgconfig
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.12.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxsession-edit is a tool used to manage desktop session autostarts,
especially for lxsession lite.

%description -l pl.UTF-8
lxsession-edit to narzędzie do zarządzania automatycznym startem
sesji, w szczególności lxsession lite.

%prep
%setup -q

%build
%configure \
	%{?with_gtk3:--enable-gtk3} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unify name
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{tt_RU,tt}
# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/frp
# just a copy of ur
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxsession-edit
%{_desktopdir}/lxsession-edit.desktop
%{_datadir}/lxsession-edit
