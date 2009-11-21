%define		_class		RDF
%define		upstream_name	%{_class}
%define		pre         alpha1

Name:		php-pear-%{upstream_name}
Version:	0.1.0
Release:	%mkrel 0.%{pre}.1
Summary:	Port of the core RAP API
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/RDF
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}%{pre}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:  php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package is a port of the core components of the RDF API for PHP (aka RAP):
http://www.wiwiss.fu-berlin.de/suhl/bizer/rdfapi/.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}%{pre}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}%{pre}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}%{pre}/docs/*
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml

