Name: mythes-de
Summary: German thesaurus
%define upstreamid 20130206
Version: 0.%{upstreamid}
Release: 2%{?dist}
Source0: http://www.openthesaurus.de/export/Deutscher-Thesaurus.oxt
Source1: http://www.openthesaurus.de/export/Schweizer-Thesaurus.oxt
Group: Applications/Text
URL: http://www.openthesaurus.de
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python, perl
License: LGPLv2+
BuildArch: noarch
Requires: mythes

%description
German thesaurus.

%prep
%setup -q -c
rm -rf mythes-ch-%{upstreamid}
mkdir mythes-ch-%{upstreamid}
cd mythes-ch-%{upstreamid}
unzip -q %{SOURCE1}

%build
for i in README.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_de_DE_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p mythes-ch-%{upstreamid}/th_de_DE_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_de_CH_v2.idx
cp -p mythes-ch-%{upstreamid}/th_de_DE_v2.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_de_CH_v2.dat

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
de_DE_aliases="de_AT de_BE de_LI de_LU"
for lang in $de_DE_aliases; do
        ln -s th_de_DE_v2.idx "th_"$lang"_v2.idx"
        ln -s th_de_DE_v2.dat "th_"$lang"_v2.dat"
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.txt
%{_datadir}/mythes/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20130206-2
- Mass rebuild 2013-12-27

* Wed Feb 06 2013 Caolán McNamara <caolanm@redhat.com> - 0.20130206-1
- Resolves: rhbz#905994 upgrade to latest version

* Wed Sep 12 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120911-1
- upgrade to latest version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20120612-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 13 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120612-1
- upgrade to latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20111124-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Michael Stahl <mstahl@redhat.com> - 0.20111124-2
- add the de_CH variant for Swiss people and people with ß allergy

* Fri Nov 25 2011 Michael Stahl <mstahl@redhat.com> - 0.20111124-1
- upgrade to latest version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090708-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Apr 03 2010 Caolan McNamara <caolanm@redhat.com> - 0.20090708-4
- mythes now owns /usr/share/mythes

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090708-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090708-2
- tidy spec

* Wed Jul 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090708-1
- latest version

* Mon Jun 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090608-1
- latest version

* Thu Apr 02 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090402-1
- latest version

* Mon Mar 02 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090302-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 02 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090202-1
- latest version

* Tue Dec 23 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081223-1
- latest version

* Sun Nov 23 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081123-1
- latest version

* Thu Oct 16 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081016-1
- latest version

* Mon Sep 01 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080901-1
- latest version

* Thu Jul 31 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080731-1
- latest version
