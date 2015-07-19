# revision 28921
# category Package
# catalog-ctan /macros/latex/contrib/morehype
# catalog-date 2013-01-23 12:31:43 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-morehype
Version:	20130123
Release:	9
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
%{_texmfdistdir}/tex/latex/morehype/atari_ht.fdf
%{_texmfdistdir}/tex/latex/morehype/blog.sty
%{_texmfdistdir}/tex/latex/morehype/blogdot.cfg
%{_texmfdistdir}/tex/latex/morehype/blogdot.sty
%{_texmfdistdir}/tex/latex/morehype/blogexec.sty
%{_texmfdistdir}/tex/latex/morehype/blogligs.sty
%{_texmfdistdir}/tex/latex/morehype/hypertoc.sty
%{_texmfdistdir}/tex/latex/morehype/lnavicol.sty
%{_texmfdistdir}/tex/latex/morehype/markblog.sty
%{_texmfdistdir}/tex/latex/morehype/morehype.RLS
%{_texmfdistdir}/tex/latex/morehype/texblog.fdf
%{_texmfdistdir}/tex/latex/morehype/texlinks.sty
%doc %{_texmfdistdir}/doc/latex/morehype/README
%doc %{_texmfdistdir}/doc/latex/morehype/README.pdf
%doc %{_texmfdistdir}/doc/latex/morehype/RELEASEs.txt
%doc %{_texmfdistdir}/doc/latex/morehype/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/latex/morehype/blog.pdf
%doc %{_texmfdistdir}/doc/latex/morehype/blogdemo/hellowor/hellowor.htm
%doc %{_texmfdistdir}/doc/latex/morehype/blogdemo/hellowor/hellowor.tex
%doc %{_texmfdistdir}/doc/latex/morehype/blogdemo/hellowor/mkhellow.tex
%doc %{_texmfdistdir}/doc/latex/morehype/blogdemo/writings/makehtml.tex
%doc %{_texmfdistdir}/doc/latex/morehype/blogdemo/writings/schreibt.tex
%doc %{_texmfdistdir}/doc/latex/morehype/blogdemo/writings/writings.fdf
%doc %{_texmfdistdir}/doc/latex/morehype/blogexec.pdf
%doc %{_texmfdistdir}/doc/latex/morehype/hypertoc.pdf
%doc %{_texmfdistdir}/doc/latex/morehype/markblog.htm
%doc %{_texmfdistdir}/doc/latex/morehype/ref_alts.tex
%doc %{_texmfdistdir}/doc/latex/morehype/texlinks.pdf
%doc %{_texmfdistdir}/doc/latex/morehype/wiki_mwe.pdf
%doc %{_texmfdistdir}/doc/latex/morehype/wiki_mwe.tex
#- source
%doc %{_texmfdistdir}/source/latex/morehype/README.tex
%doc %{_texmfdistdir}/source/latex/morehype/blog.tex
%doc %{_texmfdistdir}/source/latex/morehype/blogdot.css
%doc %{_texmfdistdir}/source/latex/morehype/blogexec.tex
%doc %{_texmfdistdir}/source/latex/morehype/fdatechk.tex
%doc %{_texmfdistdir}/source/latex/morehype/hypertoc.tex
%doc %{_texmfdistdir}/source/latex/morehype/markblog.tex
%doc %{_texmfdistdir}/source/latex/morehype/srcfiles.tex
%doc %{_texmfdistdir}/source/latex/morehype/texlinks.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
