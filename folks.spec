%define tp_glib_ver	0.13.1

Name:           folks
Epoch:          1
Version:        0.6.3.2
Release:        1%{?dist}
Summary:        GObject contact aggregation library

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/Folks
Source0:        http://download.gnome.org/sources/folks/0.6/%{name}-%{version}.tar.xz

BuildRequires:  telepathy-glib-devel >= %{tp_glib_ver}
BuildRequires:  telepathy-glib-vala
BuildRequires:  glib2-devel
BuildRequires:  vala-devel >= 0.13.0
BuildRequires:  vala-tools
BuildRequires:  libxml2-devel
BuildRequires:  gobject-introspection >= 0.9.12
BuildRequires:  GConf2-devel
BuildRequires:  evolution-data-server-devel >= 3.1.5
BuildRequires:  libsocialweb-devel >= 0.25.15
## BuildRequires: tracker-devel >= 0.10
BuildRequires:  pkgconfig(gee-1.0)


%description
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers and eventually evolution data server,
Facebook, etc.) to create meta-contacts.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       telepathy-glib-devel >= %{tp_glib_ver}
Requires:       glib2-devel
Requires:       pkgconfig
Requires:	pkgconfig(gee-1.0)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static --enable-eds-backend
make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}-import
%{_libdir}/*.so.*
%{_libdir}/folks
%{_libdir}/girepository-1.0/Folks-0.6.typelib
%{_datadir}/vala/vapi/%{name}*

%files devel
%defattr(-,root,root,-)
%{_includedir}/folks
%{_libdir}/*.so
%{_libdir}/pkgconfig/folks*.pc
%{_datadir}/gir-1.0/Folks-0.6.gir


%changelog
* Mon Sep 26 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.3.2-1
- Update to 0.6.3.2.

* Sun Sep 25 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.3.1-1
- Update to 0.6.3.1.
- Drop typelib patch. Fixed upstream.

* Wed Sep 21 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.3-2
- Fix another typelib problem

* Mon Sep 19 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.3-1
- Update to 0.6.3.
- Drop typelib patch. Fixed upstream.

* Wed Sep 14 2011 Owen Taylor <otaylor@redhat.com> - 1:0.6.2.1-2
- Really fix the typelib to embed the right .so file

* Thu Sep  8 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.2.1-1
- Really fix the reentrancy problem, by using 0.6.2.1

* Thu Sep  8 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.2-2
- Fix a reentrancy problem that causes gnome-shell to crash

* Thu Sep  8 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.2-1
- Update to 0.6.2.1

* Thu Sep  8 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.2-1
- Update to 0.6.2
- Use old libgee api.

* Wed Sep  7 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.1-4
- Try again

* Tue Sep 06 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.1-3
- Rebuld against new libcamel.

* Thu Sep  1 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.1-2
- Fix up the typelib

* Mon Aug 29 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.1-1
- Update to 0.6.1.
- Drop EDS patch. Fixed upstream.

* Mon Aug 29 2011 Milan Crha <mcrha@redhat.com> - 1:0.6.0-6
- Rebuild against newer evolution-data-server

* Fri Aug 19 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.0-4
- Try again to rebuild

* Tue Aug 16 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.0-2
- Rebuld for new eds

* Sat Aug 13 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.0-1
- Update to 0.6.0.
- Update source url.
- Add BR on eds-devel and libsocialweb-devel.

* Fri Jun 10 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.5.2-1
- Update to 0.5.2.
- Add BR on GConf2-devel.

* Wed Mar 23 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.4.2-1
- Update to 0.4.2.

* Fri Mar 18 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.4.1-1
- Update to 0.4.1.

* Thu Mar 17 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.4.0-2
- Update source url.

* Thu Mar 17 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.4.0-1
- Update to 0.4.0.

* Mon Feb 14 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.3.6-1
- Update to 0.3.6.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.3.4-1
- Update to 0.3.4.

* Tue Dec 14 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:0.3.3-1
- Update to 0.3.3.

* Sun Nov 14 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:0.3.2-1
- Update to 0.3.2.
- Update min version of tp-glib.
- Update source url.
- Drop dso linking patch. Fixed upstream.

* Fri Oct 29 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:0.2.1-1
- Update to 0.2.1.
- Add patch to fix dso linking. (fdo #633511)

* Fri Oct 29 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:0.2.0-4
- Add epoch to devel subpackage requires.

* Mon Oct 25 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:0.2.0-3
- Revert back to 0.2.x until gtk-2.92.1 or greater is in rawhide.

* Wed Oct 20 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1.
- Update source url.
- Update tp-glib version required.

* Wed Sep 29 2010 jkeating - 0.2.0-2
- Rebuilt for gcc bug 634757

* Sat Sep 25 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0.
- Add missing requires to devel subpackage.
- Drop DSO linkng patch. Fixed upstream.

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
