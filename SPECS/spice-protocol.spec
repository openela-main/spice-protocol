Name:           spice-protocol
Version:        0.14.2
Release:        1%{?dist}
Summary:        Spice protocol header files
Group:          Development/Libraries
# Main headers are BSD, controller / foreign menu are LGPL
License:        BSD and LGPLv2+
URL:            https://www.spice-space.org/
Source0:        https://www.spice-space.org/download/releases/%{name}-%{version}.tar.xz
Source1:        https://www.spice-space.org/download/releases/%{name}-%{version}.tar.xz.sig
Source2:        victortoso-E37A484F.keyring
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  meson

%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.


%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -S git_am

%build
%meson
%meson_build

%install
%meson_install


%files
%doc COPYING README.md
%{_includedir}/spice-1
%{_datadir}/pkgconfig/spice-protocol.pc


%changelog
* Fri May 15 2020 Victor Toso <victortoso@redhat.com> - 0.14.2-1
- Update to 0.14.2
  Resolves: rhbz#1817451

* Tue May 05 2020 Victor Toso <victortoso@redhat.com> - 0.14.1-1
- Update to 0.14.1
  Resolves: rhbz#1817451

* Fri May 17 2019 Victor Toso <victortoso@redhat.com> - 0.14.0-1
- Update to 0.14.0
  Resolves: rhbz#1711253
- Add signature check to release

* Mon Jul 30 2018 Victor Toso <victortoso@redhat.com> - 0.12.14-1
- Update to 0.12.14
- Fix misaligned warnings - Resolves: rhbz#1565766

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.12.13-1
- Update to 0.12.13 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 05 2016 Christophe Fergeau <cfergeau@redhat.com> - 0.12.12-1
- Update to 0.12.12 release

* Fri Mar 11 2016 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.12.11-1
- Update to 0.12.11 release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 01 2015 Christophe Fergeau <cfergeau@redhat.com> 0.12.10-1
- Update to 0.12.10 - Add python scripts and .proto files used
  to generate spice-gtk/spice-server marshalling C code

* Wed Jul 29 2015 Christophe Fergeau <cfergeau@redhat.com> 0.12.9-1
- Update to 0.12.9 - Fixes QEMU build failures when using 0.12.8 with
  spice-server 0.12.5

* Tue Jun 30 2015 Christophe Fergeau <cfergeau@redhat.com> 0.12.8-1
- Update to 0.12.8

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Christophe Fergeau <cfergeau@redhat.com> 0.12.7-1
- Update to 0.12.7

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul  3 2013 Hans de Goede <hdegoede@redhat.com> - 0.12.6-1
- Update to 0.12.6

* Thu Mar  7 2013 Hans de Goede <hdegoede@redhat.com> - 0.12.5-1
- Update to 0.12.5

* Fri Feb  1 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.12.4-1
- Update to 0.12.4

* Thu Dec 20 2012 Hans de Goede <hdegoede@redhat.com> - 0.12.3-1
- Update to 0.12.3

* Fri Sep 28 2012 Hans de Goede <hdegoede@redhat.com> - 0.12.2-1
- Update to 0.12.2

* Thu Sep 6 2012 Soren Sandmann <ssp@redhat.com> - 0.12.1-1
- Add patch1 and patch2 to support capability bits

* Thu Sep 6 2012 Soren Sandmann <ssp@redhat.com> - 0.12.1-1
- Update to 0.12.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Hans de Goede <hdegoede@redhat.com> - 0.10.1-1
- Update to 0.10.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 13 2011 Alon Levy <alevy@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Sun Oct 23 2011 Alon Levy <alevy@redhat.com> - 0.9.1-1
- Update to 0.9.1

* Thu Aug 25 2011 Hans de Goede <hdegoede@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Mon Jul 25 2011 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.1-2
- Added spice-protocol-0.8.1-define-INLINE.patch

* Tue Jul 19 2011 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Tue Mar  1 2011 Hans de Goede <hdegoede@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Fri Feb 11 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.0-2
- Update License tag (controller and foreign menu headers are LGPL)

* Fri Dec 17 2010 Hans de Goede <hdegoede@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Mon Oct 18 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-1
- Update to 0.6.3

* Thu Sep 30 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.6.1-1
- Update to 0.6.1.

* Tue Aug 31 2010 Alexander Larsson <alexl@redhat.com> - 0.6.0-1
- Update to 0.6.0 (stable release)

* Tue Jul 20 2010 Alexander Larsson <alexl@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Mon Jul 12 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.2-2
- Fix license: It is BSD, not GPL.
- Cleanup specfile, drop bits not needed any more with
  recent rpm versions (F13+).

* Fri Jul 9 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.2-1
- initial package.

