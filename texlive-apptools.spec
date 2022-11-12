Name:		texlive-apptools
Version:	28400
Release:	1
Summary:	Tools for customising appendices
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/apptools
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apptools.r28400.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apptools.doc.r28400.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apptools.source.r28400.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
