%define		_class		RDF
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	0.2.0
Release:	1
Summary:	Port of the core RAP API
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/RDF
Source0:	http://download.pear.php.net/package/RDF-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:  php-pear
BuildArch:	noarch

%description
This package is a port of the core components of the RDF API for PHP (aka RAP):
http://www.wiwiss.fu-berlin.de/suhl/bizer/rdfapi/.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-0.alpha1.4mdv2012.0
+ Revision: 742265
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-0.alpha1.3
+ Revision: 679569
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-0.alpha1.2mdv2011.0
+ Revision: 613762
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-0.alpha1.1mdv2010.1
+ Revision: 467960
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Fri Sep 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-0.alpha1.1mdv2010.0
+ Revision: 448598
- import php-pear-RDF


* Thu Sep 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-0.alpha1.1mdv2010.0
- first mdv release

