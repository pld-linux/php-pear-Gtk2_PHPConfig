%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Gtk2_PHPConfig
%define		subver	RC1
%define		rel	4
Summary:	%{_pearname} - GUI Interface to the php.ini file
Summary(pl.UTF-8):	%{_pearname} - graficzny interfejs do pliku php.ini
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.%{subver}.%{rel}
License:	LGPL Version 2.1
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	37b8af21bbe7e3e9954191c1cb99d2c6
URL:		http://pear.php.net/package/Gtk2_PHPConfig/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-gtk2
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A user friendly interface to the various configuration options
available in a php.ini file.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Przyjazny dla użytkownika interfejs do różnych opcji konfiguracyjnych
dostępnych w pliku php.ini

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
install usr/bin/gtk2_phpconfig $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%attr(755,root,root) %{_bindir}/gtk2_phpconfig
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Gtk2/PHPConfig
%{php_pear_dir}/Gtk2/PHPConfig.php
%dir %{php_pear_dir}/data/Gtk2_PHPConfig
%{php_pear_dir}/data/Gtk2_PHPConfig/phpinidefs.xml
