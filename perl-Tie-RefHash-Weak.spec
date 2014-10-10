%define upstream_name    Tie-RefHash-Weak
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A Tie::RefHash subclass with weakened references in the keys
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Tie::RefHash)
BuildRequires:	perl(Variable::Magic)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 653624
- rebuild for updated spec-helper

* Thu Jul 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 563012
- import perl-Tie-RefHash-Weak


* Thu Jul 29 2010 cpan2dist 0.09-1mdv
- initial mdv release, generated with cpan2dist
