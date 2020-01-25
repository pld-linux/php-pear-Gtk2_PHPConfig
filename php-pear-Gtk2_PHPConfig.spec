%define		_status		beta
%define		_pearname	Gtk2_PHPConfig
%define		subver	RC2
%define		rel	1
Summary:	%{_pearname} - GUI Interface to the php.ini file
Summary(pl.UTF-8):	%{_pearname} - graficzny interfejs do pliku php.ini
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.%{subver}.%{rel}
License:	LGPL Version 2.1
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	bb9a5d7aa2178337ee07e284389b4f67
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

install -d bin
mv .%{php_pear_dir}/data/Gtk2_PHPConfig/gtk2_phpconfig bin

# duplicate bin
rm .%{php_pear_dir}/data/Gtk2_PHPConfig/run.phpw

# junk
%{__rm} .%{php_pear_dir}/data/Gtk2_PHPConfig/releases/Gtk2_PHPConfig-1.0.0RC1.tgz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

install -p bin/gtk2_phpconfig $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/gtk2_phpconfig
%{php_pear_dir}/Gtk2/PHPConfig.php

%{php_pear_dir}/data/Gtk2_PHPConfig
