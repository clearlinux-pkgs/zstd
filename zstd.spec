#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zstd
Version  : 1.3.8
Release  : 39
URL      : https://github.com/facebook/zstd/releases/download/v1.3.8/zstd-1.3.8.tar.gz
Source0  : https://github.com/facebook/zstd/releases/download/v1.3.8/zstd-1.3.8.tar.gz
Summary  : fast lossless compression algorithm library
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: zstd-bin = %{version}-%{release}
Requires: zstd-lib = %{version}-%{release}
Requires: zstd-license = %{version}-%{release}
Requires: zstd-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : lz4-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev
Patch1: multi-thread-default.patch

%description
<p align="center"><img src="https://raw.githubusercontent.com/facebook/zstd/dev/doc/images/zstd_logo86.png" alt="Zstandard"></p>

%package bin
Summary: bin components for the zstd package.
Group: Binaries
Requires: zstd-license = %{version}-%{release}
Requires: zstd-man = %{version}-%{release}

%description bin
bin components for the zstd package.


%package dev
Summary: dev components for the zstd package.
Group: Development
Requires: zstd-lib = %{version}-%{release}
Requires: zstd-bin = %{version}-%{release}
Provides: zstd-devel = %{version}-%{release}

%description dev
dev components for the zstd package.


%package lib
Summary: lib components for the zstd package.
Group: Libraries
Requires: zstd-license = %{version}-%{release}

%description lib
lib components for the zstd package.


%package license
Summary: license components for the zstd package.
Group: Default

%description license
license components for the zstd package.


%package man
Summary: man components for the zstd package.
Group: Default

%description man
man components for the zstd package.


%prep
%setup -q -n zstd-1.3.8
%patch1 -p1
pushd ..
cp -a zstd-1.3.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546023018
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
make PREFIX=%{_prefix} LIBDIR=%{_libdir}

pushd ../buildavx2
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
make PREFIX=%{_prefix} LIBDIR=%{_libdir}
popd

%install
export SOURCE_DATE_EPOCH=1546023018
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zstd
cp COPYING %{buildroot}/usr/share/package-licenses/zstd/COPYING
cp LICENSE %{buildroot}/usr/share/package-licenses/zstd/LICENSE
cp contrib/linux-kernel/COPYING %{buildroot}/usr/share/package-licenses/zstd/contrib_linux-kernel_COPYING
pushd ../buildavx2/
%make_install_avx2 PREFIX=%{_prefix} LIBDIR=%{_libdir}
popd
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/haswell/unzstd
/usr/bin/haswell/zstd
/usr/bin/haswell/zstdcat
/usr/bin/haswell/zstdmt
/usr/bin/unzstd
/usr/bin/zstd
/usr/bin/zstdcat
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/zstdmt

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/haswell/libzstd.so
/usr/lib64/libzstd.so
/usr/lib64/pkgconfig/libzstd.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libzstd.so.1
/usr/lib64/haswell/libzstd.so.1.3.8
/usr/lib64/libzstd.so.1
/usr/lib64/libzstd.so.1.3.8

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zstd/COPYING
/usr/share/package-licenses/zstd/LICENSE
/usr/share/package-licenses/zstd/contrib_linux-kernel_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/unzstd.1
/usr/share/man/man1/zstd.1
/usr/share/man/man1/zstdcat.1
/usr/share/man/man1/zstdgrep.1
/usr/share/man/man1/zstdless.1
