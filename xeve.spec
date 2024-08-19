Name:           xeve
Version:        0.5.0
Release:        1%{?dist}
Summary:        eXtra-fast Essential Video Encoder, MPEG-5 EVC (Essential Video Coding)
License:        BSD-3-Clause
URL:            https://github.com/mpeg5/xeve

Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
#BuildRequires:  git

%description
eXtra-fast Essential Video Encoder, MPEG-5 EVC (Essential Video Coding).

%package        libs
Summary:        MPEG-5 EVC encoder %{name} libraries

%description    libs
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}. This package contains the shared libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
echo "v%{version}" > version.txt

%build
%cmake
%cmake_build

%install
%cmake_install

# Static library
rm -fr %{buildroot}%{_libdir}/%{name}

%files
%{_bindir}/%{name}_app

%files libs
%license COPYING
%doc README.md
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.5

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Aug 19 2024 Simone Caronni <negativo17@gmail.com> - 0.5.0-1
- First build.
