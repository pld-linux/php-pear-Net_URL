%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	URL
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - easy parsing of URLs
Summary(pl.UTF-8):   %{_pearname} - proste parsowanie adresów
Name:		php-pear-%{_pearname}
Version:	1.0.14
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4be5ac05dc5a9bc54a33cec66d87eb0a
URL:		http://pear.php.net/package/Net_URL/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides easy parsing of URLs and their constituent parts.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pozwala na proste parsowanie adresów URL oraz ich części.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
