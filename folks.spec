Name:           folks
Version:        0.1.17
Release:        1%{?dist}
Summary:        GObject contact aggregation library

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/Folks
Source0:        http://download.gnome.org/sources/folks/0.1/%{name}-%{version}.tar.bz2
# https://bugzilla.gnome.org/show_bug.cgi?id=629452
Patch0:		%{name}-%{version}-DSO_linking.patch


BuildRequires:  telepathy-glib-devel >= 0.11.11
BuildRequires:  telepathy-glib-vala
BuildRequires:  vala-devel
BuildRequires:  vala-tools
BuildRequires:  libgee-devel
BuildRequires:  libxml2-devel

%description
libfolks is a library that aggregates people from multiple sources (e.g. 
Telepathy connection managers and eventually evolution data server, 
Facebook, etc.) to create meta-contacts. 


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1 -b .dso


%build
%configure --disable-static
make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}-import
%{_libdir}/*.so.*
%{_libdir}/folks
%{_datadir}/vala/vapi/%{name}*

%files devel
%defattr(-,root,root,-)
%{_includedir}/folks
%{_libdir}/*.so
%{_libdir}/pkgconfig/folks*.pc


%changelog
* Sun Sep 12 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.17-1
- Update to 0.1.17.
- Add patch to fix DSO linking for import tool.
- Add BR on libxml2-devel so import tool is built.

* Wed Sep  1 2010 Yanko Kaneti <yaneti@declera.com> 0.1.16-1
- New upstream release.

* Thu Aug 30 2010 Yanko Kaneti <yaneti@declera.com> 0.1.15-1
- New upstream release. Drop the RPATH hacks.

* Thu Aug 19 2010 Yanko Kaneti <yaneti@declera.com> 0.1.14.1-1
- New upstream release. Requires vala >= 0.9.6

* Thu Aug 19 2010 Yanko Kaneti <yaneti@declera.com> 0.1.14-2
- Use chrpath to remove the lingering RPATH because the guidelines
  recomended sed makes libtool incapable of building the tp-lowlevel.gir.
  Better solution welcome.

* Wed Aug 18 2010 Yanko Kaneti <yaneti@declera.com> 0.1.14-1
- New upstream. Remove patch and libtool hack.

* Tue Aug 17 2010 Yanko Kaneti <yaneti@declera.com> 0.1.13-4
- Add BR: vala-tools

* Tue Aug 17 2010 Yanko Kaneti <yaneti@declera.com> 0.1.13-3
- Update for the available telepathy-glib vala packaging

* Thu Aug 12 2010 Yanko Kaneti <yaneti@declera.com> 0.1.13-2
- Add BR: libgee-devel

* Thu Aug 12 2010 Yanko Kaneti <yaneti@declera.com> 0.1.13-1
- New upstream release
- Autofoo for the new vala api versioning

* Tue Aug  3 2010 Yanko Kaneti <yaneti@declera.com> 0.1.12-1
- New upstream release

* Mon Aug  2 2010 Yanko Kaneti <yaneti@declera.com> 0.1.11-1
- Packaged for review
