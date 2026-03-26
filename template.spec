# vim: filetype=spec

%define version @@@Version@@@
%define builddir %{_builddir}/python%{python3_pkgversion}-fb-ddns-%{version}

Name:           python%{python3_pkgversion}-fb-ddns
Version:        %{version}
Release:        @@@Release@@@%{?dist}
Summary:        Python scripts and modules for managing DynDNS clients.

Group:          Development/Languages/Python
License:        LGPL-3
Distribution:   Frank Brehm
URL:            https://github.com/fbrehm/fb-ddns
Source0:        fb-ddns.%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  python%{python3_pkgversion}
BuildRequires:  python%{python3_pkgversion}-babel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-fb-tools >= 3.0.0
BuildRequires:  python%{python3_pkgversion}-libs
BuildRequires:  python%{python3_pkgversion}-pyyaml
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  pyproject-rpm-macros
Requires:       python%{python3_pkgversion}
Requires:       python%{python3_pkgversion}-babel
Requires:       python%{python3_pkgversion}-dns
Requires:       python%{python3_pkgversion}-fb-tools >= 3.0.0
Requires:       python%{python3_pkgversion}-libs
Requires:       python%{python3_pkgversion}-pyyaml
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-urllib3
BuildArch:      noarch

%description
Python scripts and modules for managing DynDNS clients.

This is the Python@@@py_version_nodot@@@ version.

In this package are contained the following scripts:
 * myip
 * update-ddns

%prep
echo "Preparing '${builddir}-' ..."
echo "Pwd: $( pwd )"
%autosetup -p1 -v

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fb_ddns

echo "Whats in '%{builddir}':"
ls -lA '%{builddir}'

echo "Whats in '%{buildroot}':"
ls -lA '%{buildroot}'

%files -f %{pyproject_files}
%defattr(-,root,root,-)
%license LICENSE
%doc CHANGELOG.md LICENSE README.md pyproject.toml debian/changelog
%{_bindir}/*
%{_datadir}/*

%changelog
