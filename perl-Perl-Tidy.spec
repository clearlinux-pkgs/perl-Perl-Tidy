#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Perl-Tidy
Version  : 20210625
Release  : 36
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHANCOCK/Perl-Tidy-20210625.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHANCOCK/Perl-Tidy-20210625.tar.gz
Summary  : 'indent and reformat perl scripts'
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Perl-Tidy-bin = %{version}-%{release}
Requires: perl-Perl-Tidy-license = %{version}-%{release}
Requires: perl-Perl-Tidy-man = %{version}-%{release}
Requires: perl-Perl-Tidy-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
These are some files to test and illustrate Perl::Tidy
testfa.t - test with input from file and output to array
testff.t - test with input from file and output to file

%package bin
Summary: bin components for the perl-Perl-Tidy package.
Group: Binaries
Requires: perl-Perl-Tidy-license = %{version}-%{release}

%description bin
bin components for the perl-Perl-Tidy package.


%package dev
Summary: dev components for the perl-Perl-Tidy package.
Group: Development
Requires: perl-Perl-Tidy-bin = %{version}-%{release}
Provides: perl-Perl-Tidy-devel = %{version}-%{release}
Requires: perl-Perl-Tidy = %{version}-%{release}

%description dev
dev components for the perl-Perl-Tidy package.


%package license
Summary: license components for the perl-Perl-Tidy package.
Group: Default

%description license
license components for the perl-Perl-Tidy package.


%package man
Summary: man components for the perl-Perl-Tidy package.
Group: Default

%description man
man components for the perl-Perl-Tidy package.


%package perl
Summary: perl components for the perl-Perl-Tidy package.
Group: Default
Requires: perl-Perl-Tidy = %{version}-%{release}

%description perl
perl components for the perl-Perl-Tidy package.


%prep
%setup -q -n Perl-Tidy-20210625
cd %{_builddir}/Perl-Tidy-20210625

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Perl-Tidy
cp %{_builddir}/Perl-Tidy-20210625/COPYING %{buildroot}/usr/share/package-licenses/perl-Perl-Tidy/4cc77b90af91e615a64ae04893fdffa7939db84c
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/perltidy

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Perl::Tidy.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Perl-Tidy/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/perltidy.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy.pod
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/Debugger.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/DevNull.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/Diagnostics.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/FileWriter.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/Formatter.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/HtmlWriter.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/IOScalar.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/IOScalarArray.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/IndentationItem.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/LineBuffer.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/LineSink.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/LineSource.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/Logger.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/Tokenizer.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/VerticalAligner.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/VerticalAligner/Alignment.pm
/usr/lib/perl5/vendor_perl/5.34.0/Perl/Tidy/VerticalAligner/Line.pm
