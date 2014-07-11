# revision 28400
# category Package
# catalog-ctan /macros/latex/contrib/apptools
# catalog-date 2012-11-29 15:27:46 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-apptools
Version:	1.0
Release:	7
Summary:	Tools for customising appendices
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/apptools
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apptools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apptools.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apptools.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an \AtAppendix command to add code to a
hook that is executed when \appendix is called by the user.
Additionally, a TeX conditional \ifappendix and a LaTeX-style
conditional \IfAppendix are provided to check if \appendix has
already been called.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/apptools/apptools.sty
%doc %{_texmfdistdir}/doc/latex/apptools/apptools-test.tex
%doc %{_texmfdistdir}/doc/latex/apptools/apptools.pdf
#- source
%doc %{_texmfdistdir}/source/latex/apptools/apptools.drv
%doc %{_texmfdistdir}/source/latex/apptools/apptools.dtx
%doc %{_texmfdistdir}/source/latex/apptools/apptools.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
