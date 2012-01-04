# revision 24369
# category Package
# catalog-ctan /macros/latex/contrib/morehype
# catalog-date 2011-10-23 21:21:29 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-morehype
Version:	20111023
Release:	2
Summary:	Hypertext tools for use with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/morehype
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/morehype.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/morehype.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/morehype.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides three packages: - texlinks: shorthand
macros for TeX-related external hyperlinks with hyperref, the
blog package in the present bundle, etc; - hypertoc: adjust the
presentation of coloured frames in hyperref tables of contents
(article class only); - blog: fast generation of simple HTML by
expanding LaTeX macros, using the fifinddo package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/morehype/blog.sty
%{_texmfdistdir}/tex/latex/morehype/blogdot.cfg
%{_texmfdistdir}/tex/latex/morehype/blogdot.css
%{_texmfdistdir}/tex/latex/morehype/blogdot.sty
%{_texmfdistdir}/tex/latex/morehype/hypertoc.sty
%{_texmfdistdir}/tex/latex/morehype/lang-de.fdf
%{_texmfdistdir}/tex/latex/morehype/lang-en.fdf
%{_texmfdistdir}/tex/latex/morehype/lnavicol.sty
%{_texmfdistdir}/tex/latex/morehype/texblog.fdf
%{_texmfdistdir}/tex/latex/morehype/texlinks.sty
%doc %{_texmfdistdir}/doc/latex/morehype/README
%doc %{_texmfdistdir}/doc/latex/morehype/README.pdf
%doc %{_texmfdistdir}/doc/latex/morehype/RELEASEs.txt
%doc %{_texmfdistdir}/doc/latex/morehype/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/latex/morehype/blog.pdf
%doc %{_texmfdistdir}/doc/latex/morehype/demo/texblog/makehtml.tex
%doc %{_texmfdistdir}/doc/latex/morehype/demo/texblog/texmap.tex
%doc %{_texmfdistdir}/doc/latex/morehype/demo/writings/makehtml.tex
%doc %{_texmfdistdir}/doc/latex/morehype/demo/writings/schreibt.tex
%doc %{_texmfdistdir}/doc/latex/morehype/demo/writings/writings.fdf
%doc %{_texmfdistdir}/doc/latex/morehype/hypertoc.pdf
%doc %{_texmfdistdir}/doc/latex/morehype/texlinks.pdf
#- source
%doc %{_texmfdistdir}/source/latex/morehype/README.tex
%doc %{_texmfdistdir}/source/latex/morehype/blog.tex
%doc %{_texmfdistdir}/source/latex/morehype/hypertoc.tex
%doc %{_texmfdistdir}/source/latex/morehype/srcfiles.tex
%doc %{_texmfdistdir}/source/latex/morehype/texlinks.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
