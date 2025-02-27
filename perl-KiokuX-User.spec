%define upstream_name    KiokuX-User
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	A role for users
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/KiokuX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Crypt::Rijndael)
BuildRequires:	perl(KiokuDB)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildRequires:	perl(MooseX::Types::Authen::Passphrase)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
This role provides a fairly trivial set of attributes and methods designed
to ease the storage of objects representing users in a KiokuDB database.

It consumes the KiokuX::User::ID manpage which provides the 'id' attribute
and the KiokuDB::Role::ID manpage integration, and the
KiokuX::User::Password manpage which provides an the Authen::Passphrase
manpage based 'password' attribute and a 'check_password' method.

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
%{_mandir}/man3/*
%{perl_vendorlib}/*
