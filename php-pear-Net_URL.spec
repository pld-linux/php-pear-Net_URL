%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       URL
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Easy parsing of Urls
Summary(pl):	%{_class}_%{_subclass} - Proste parsowanie adresów
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides easy parsing of URLs and their constituent parts.

%description -l pl
Pozwala na proste parsowanie adresów URL oraz ich czê¶ci.

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
