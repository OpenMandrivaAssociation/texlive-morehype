%global tl_name morehype
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	r0.83
Release:	%{tl_revision}.1
Summary:	Hypertext tools for use with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/morehype
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/morehype.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/morehype.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/morehype.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides three packages: texlinks: shorthand macros for TeX-
related external hyperlinks with hyperref, the blog package in the
present bundle, etc; hypertoc: adjust the presentation of coloured
frames in hyperref tables of contents (article class only); blog: fast
generation of simple HTML by expanding LaTeX macros, using the fifinddo
package.

