Name:		texlive-xltabular
Version:	56855
Release:	2
Summary:	Longtable support with possible X-column specifier
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xltabular
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xltabular.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xltabular.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package loads package ltablex, but keeps the current
tabularx environment as is. The new environment xltabular is a
combination of longtable and tabularx: Header/footer
definitions, X-column specifier, and with possible pagebreaks.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/xltabular
%doc %{_texmfdistdir}/doc/latex/xltabular

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
