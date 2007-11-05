# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-PID
%define real_version 0.000013

Summary: Perl module for getting PID info
Name: perl-Unix-PID
Version: 0.0.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-PID/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-PID-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unix-PID is a Perl module for getting PID info.

This package contains the following Perl module:

    Unix::PID

%prep
%setup -n %{real_name}-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Unix::PID.3pm*
%dir %{perl_vendorlib}/Unix/
#%{perl_vendorlib}/Unix/PID/
%{perl_vendorlib}/Unix/PID.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.0.13-1
- Initial package. (using DAR)