# Required due to circular dependencies in lt_libraries
%define _disable_ld_no_undefined	1

%define name	cbc
%define major	0
%define libname	%mklibname %{name} %{major}

Name:		%{name}
Group:		Sciences/Mathematics
License:	CPL
Summary:	An open-source mixed integer programming solver
Version:	2.4.0
Release:	%mkrel 1
URL:		http://www.coin-or.org/
Source0:	http://www.coin-or.org/download/source/Cbc/Cbc-%{version}.tgz
# wget http://netlib.sandia.gov/cgi-bin/netlib/netlibfiles.tar?filename=netlib/ampl/solvers
Source1:	solvers.tar
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	blas-devel
BuildRequires:	glpk-devel
BuildRequires:	lapack-devel
BuildRequires:	readline-devel

Patch0:		Cbc-2.4.0-format.patch

%description
Cbc (Coin-or branch and cut) is an open-source mixed integer programming
solver written in C++. It is primarily meant to be used as a callable library,
but a basic, stand-alone executable version is also available. Cbc is a branch
and cut code working with the LP solver Clp, and possibly dylp. 

%package	-n %{libname}
Group:		System/Libraries
License:	CPL
Summary:	An open-source mixed integer programming solver
Provides:	lib%{name} = %{version}-%{release}

%description	-n %{libname}
Cbc (Coin-or branch and cut) is an open-source mixed integer programming
solver written in C++. It is primarily meant to be used as a callable library,
but a basic, stand-alone executable version is also available. Cbc is a branch
and cut code working with the LP solver Clp, and possibly dylp. 

%package	-n lib%{name}-devel
Group:		Development/C
License:	CPL
Summary:	An open-source mixed integer programming solver
Requires:	lib%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n lib%{name}-devel
Cbc (Coin-or branch and cut) is an open-source mixed integer programming
solver written in C++. It is primarily meant to be used as a callable library,
but a basic, stand-alone executable version is also available. Cbc is a branch
and cut code working with the LP solver Clp, and possibly dylp. 

%prep
%setup -q -n Cbc-%{version}

pushd ThirdParty/ASL
    tar xf %{SOURCE1}
    gunzip -fr solvers
popd

%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/cbc
%{_bindir}/clp

%files		-n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files		-n lib%{name}-devel
%defattr(-,root,root)
%dir %{_includedir}/coin
%{_includedir}/coin/*
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%dir %{_docdir}/coin
%{_docdir}/coin/*
