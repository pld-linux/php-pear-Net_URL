%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       URL
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Easy parsing of Urls
Summary(pl):	%{_pearname} - Proste parsowanie adresów
Name:		php-pear-%{_pearname}
Version:	1.0.11
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fec1a8d55b884bd7b5ef72b9a36e474a
URL:		http://pear.php.net/package/Net_URL/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides easy parsing of URLs and their constituent parts.

This class has in PEAR status: %{_status}.

%description -l pl
Pozwala na proste parsowanie adresów URL oraz ich czê¶ci.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
