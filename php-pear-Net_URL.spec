%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	URL
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - easy parsing of URLs
Summary(pl):	%{_pearname} - proste parsowanie adresów
Name:		php-pear-%{_pearname}
Version:	1.0.13
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e8ed2e4be5bb24b819be72aedb04a102
URL:		http://pear.php.net/package/Net_URL/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides easy parsing of URLs and their constituent parts.

In PEAR status of this package is: %{_status}.

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
