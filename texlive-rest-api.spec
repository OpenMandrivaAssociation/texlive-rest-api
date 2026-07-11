%global tl_name rest-api
%global tl_revision 57068

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Describing a rest api
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rest-api
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rest-api.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rest-api.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rest-api.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides macros to describe rest apis for
documentation purposes. The endpoints can hold the following
information: method description path parameter request body and content
type response body, content type and status code

