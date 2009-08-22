# $Id$
# Authority: cmr

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-RewritePrefix

Summary: Perl module named String-RewritePrefix
Name: perl-String-RewritePrefix
Version: 0.004
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-RewritePrefix/

Source: http://www.cpan.org/modules/by-module/String/String-RewritePrefix-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-String-RewritePrefix is a Perl module.

%prep
%setup -n %{real_name}-%{version}

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
%doc Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/String::RewritePrefix.3pm*
%dir %{perl_vendorlib}/String/
#%{perl_vendorlib}/String/RewritePrefix/
%{perl_vendorlib}/String/RewritePrefix.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.004-1
- Initial package. (using DAR)
