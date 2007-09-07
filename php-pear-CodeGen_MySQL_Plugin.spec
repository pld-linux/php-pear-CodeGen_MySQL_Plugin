%include	/usr/lib/rpm/macros.php
%define		_class		CodeGen
%define		_subclass	MySQL_Plugin
%define		_status		alpha
%define		_pearname	CodeGen_MySQL_Plugin
Summary:	%{_pearname} - tool to generate MySQL Plugins from an XML description
Summary(pl.UTF-8):	%{_pearname} - narzędzie do generowania wtyczek do MySQL na podstawie opisu XML
Name:		php-pear-%{_pearname}
Version:	0.1.1dev
Release:	0.1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b541c550c93e0ee7bbe096c1327639ed
URL:		http://pear.php.net/package/CodeGen_MySQL_Plugin/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-CodeGen >= 1.0.3
Requires:	php-pear-PEAR >= 1.4.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CodeGen_MySQL_Plugin is a code generator for MySQL Plugins extensions
similar to PECL_Gen for PHP.

It reads in configuration options, function prototypes and code
fragments from an XML description file and generates a complete
ready-to-compile plugin project.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
CodeGen_MYSQL_plugins to generator kodu dla wtyczek MySQL podobny do
PECL_Gen dla PHP.

Pakiet ten na podstawie opcji konfiguracyjnych, prototypów funkcji i
fragmentów kodu z pliku opisu XML generuje kompletny, gotowy do
skompilowania projekt wtyczki.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
install {./,$RPM_BUILD_ROOT}%{_bindir}/mysql-plugin-gen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%attr(755,root,root) %{_bindir}/mysql-plugin-gen
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/CodeGen/MySQL/Plugin/
