%define		_class		RDF
%define		_pearname	%{_class}
%define		pre         alpha1

Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	%mkrel 0.%{pre}.1
Summary:	Port of the core RAP API
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/RDF
Source0:	http://download.pear.php.net/package/%{_pearname}-%{version}%{pre}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package is a port of the core components of the RDF API for PHP (aka RAP):
http://www.wiwiss.fu-berlin.de/suhl/bizer/rdfapi/.

%prep
%setup -q -c
cp package.xml %{_pearname}-%{version}%{pre}

%install
rm -rf %{buildroot}

cd %{_pearname}-%{version}%{pre}
%{_bindir}/pear install --nodeps --packagingroot %{buildroot} package.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs

install -d -m 755 %{buildroot}%{_datadir}/pear/packages
install -m 644 package.xml \
    %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_pearname}-%{version}%{pre}/docs/*
%{_datadir}/pear/RDF.php
%{_datadir}/pear/RDF
%{_datadir}/pear/data/RDF
%{_datadir}/pear/packages/%{_pearname}.xml

