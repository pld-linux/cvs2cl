%include	/usr/lib/rpm/macros.perl
Summary:	CVS-log-message-to-ChangeLog conversion script
Summary(pl.UTF-8):	Skrypt do konwersji commit logów z CVS-u na ChangeLog
Name:		cvs2cl
Version:	2.73
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.red-bean.com/cvs2cl/%{name}.pl
# Source0-md5:	07ce09415c10753ba262923fde6e0c18
URL:		http://www.red-bean.com/cvs2cl/
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cvs2cl is Perl script that does what you think it does: it produces a
GNU-style ChangeLog for CVS-controlled sources, by running "cvs log"
and parsing the output. Duplicate log messages get unified in the
Right Way. If you don't know what any of that means, then you're doing
fine, just keep on truckin'.

%description -l pl.UTF-8
cvs2cl to skrypt perlowy, który robi to, czego można się po nim
spodziewać: tworzy plik ChangeLog w stylu GNU dla źródeł
przechowywanych w CVS-ie; robi to poprzez wywołanie "cvs log" i
przetwarzanie wyjścia. Powtórzone commit logi są ujednolicane we
Właściwy Sposób.

%prep
%setup -q -c -T
cp -p %{SOURCE0} .

# remove shell header for perl autoreqdep to work
sed -i -e '1,/^#!perl -w/d' %{name}.pl
# and add proper one
sed -i -e '1i#!%{__perl} -w' %{name}.pl

%build
pod2man %{name}.pl > %{name}.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p %{name}.pl $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -p %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cvs2cl
%{_mandir}/man1/cvs2cl.1*
