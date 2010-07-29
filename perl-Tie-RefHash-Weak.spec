%define upstream_name    Tie-RefHash-Weak
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A Tie::RefHash subclass with weakened references in the keys
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Tie::RefHash)
BuildRequires: perl(Variable::Magic)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The the Tie::RefHash manpage module can be used to access hashes by
reference. This is useful when you index by object, for example.

The problem with the Tie::RefHash manpage, and cross indexing, is that
sometimes the index should not contain strong references to the objecs. the
Tie::RefHash manpage's internal structures contain strong references to the
key, and provide no convenient means to make those references weak.

This subclass of the Tie::RefHash manpage has weak keys, instead of strong
ones. The values are left unaltered, and you'll have to make sure there are
no strong references there yourself.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


