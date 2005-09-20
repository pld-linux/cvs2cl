%include	/usr/lib/rpm/macros.perl
Summary:	CVS-log-message-to-ChangeLog conversion script
Summary(pl):	Skrypt do konwersji commit logów z CVS-u na ChangeLog
Name:		cvs2cl
Version:	2.59
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications
Source0:	http://www.red-bean.com/cvs2cl/cvs2cl.pl
# Source0-md5:	2267d1023719f72358d2739e41ca984c
URL:		http://www.red-bean.com/cvs2cl/
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

%description -l pl
cvs2cl to skrypt perlowy, który robi to, czego mo¿na siê po nim
spodziewaæ: tworzy plik ChangeLog w stylu GNU dla ¼róde³
przechowywanych w CVS-ie; robi to poprzez wywo³anie "cvs log" i
przetwarzanie wyj¶cia. Powtórzone commit logi s± ujednolicane we
W³a¶ciwy Sposób.

%prep
%setup -q -c -T
cp %{SOURCE0} .

# remove shell header for perl autoreqdep to work
sed -i -e '1,/^#!perl -w/d' %{name}.pl
# and add proper one
sed -i -e '1i#!%{__perl} -w' %{name}.pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name}.pl $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
