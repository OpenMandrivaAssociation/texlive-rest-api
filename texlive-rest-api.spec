Name:		texlive-rest-api
Version:	57068
Release:	2
Summary:	Describing a rest api
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rest-api
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rest-api.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rest-api.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rest-api.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides macros to describe rest apis for
documentation purposes. The endpoints can hold the following
information: method description path parameter request body and
content type response body, content type and status code

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/rest-api
%{_texmfdistdir}/tex/latex/rest-api
%doc %{_texmfdistdir}/doc/latex/rest-api

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
