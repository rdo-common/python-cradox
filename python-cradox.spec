%{?python_enable_dependency_generator}
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

%global pypi_name cradox

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        7%{?dist}
Summary:        Python libraries for the Ceph librados library with use cython instead of ctypes

License:        LGPLv2
URL:            https://github.com/sileht/pycradox
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
ExcludeArch:	i686 armv7hl

%description
Python libraries for the Ceph librados library with use cython instead of ctypes

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        Python libraries for the Ceph librados library with use cython instead of ctypes
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pbr
BuildRequires:  python2-Cython
BuildRequires:  python2-jinja2
BuildRequires:  librados2-devel
BuildRequires:  gcc

Requires:  python2-Cython

%description -n python2-%{pypi_name}
Python libraries for the Ceph librados library with use cython instead of ctypes
%endif

%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        Python libraries for the Ceph librados library with use cython instead of ctypes
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-Cython
BuildRequires:  python3-jinja2
BuildRequires:  librados2-devel
BuildRequires:  gcc

Requires:  python3-Cython

%description -n python3-%{pypi_name}
Python libraries for the Ceph librados library with use cython instead of ctypes
%endif


%prep
%autosetup -n %{pypi_name}-%{version}
sed -i '/setup_requires/,+1d' setup.py

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if 0%{with python3}
%py3_install
%endif
%if %{with python2}
%py2_install
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitearch}/cradox.so
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
%exclude %{_usrsrc}/debug/*
%exclude %{_libdir}/debug/*
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitearch}/cradox.*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Javier Peña <jpena@redhat.com> - 2.1.0-5
- Exclude i686 and armv7hl arches from build, since Ceph does it too

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Javier Peña <jpena@redhat.com> - 2.1.0-3
- Removed python2 subpackage from Fedora 30+ (bz#1632335)

* Tue Aug 07 2018 Javier Peña <jpena@redhat.com> - 2.1.0-2
- Upstream 2.1.0
- Fixed for rawhide builds (bz#1605642)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.2-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Javier Peña <jpena@redhat.com> - 1.3.2-1
- Updated to upstream version 1.3.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuild for Python 3.6

* Wed Sep 28 2016 Javier Peña <jpena@redhat.com> - 1.3.0-1
- Updated to upstream version 1.3.0

* Mon Aug 1 2016 Javier Peña <jpena@redhat.com> - 1.1.8-3
- Removed gcc from BuildRequires

* Fri Jun 10 2016 jpena <jpena@redhat.com> - 1.1.8-2
- Fixed explicit lib dependencies
- Fixed license and source

* Thu Apr 21 2016 jpena <jpena@redhat.com> - 1.1.8-1
- Initial package.
