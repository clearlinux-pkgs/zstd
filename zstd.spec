#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEF8FE99528B52FFD (signing@zstd.net)
#
%define keepstatic 1
Name     : zstd
Version  : 1.5.0
Release  : 81
URL      : https://github.com/facebook/zstd/releases/download/v1.5.0/zstd-1.5.0.tar.gz
Source0  : https://github.com/facebook/zstd/releases/download/v1.5.0/zstd-1.5.0.tar.gz
Source1  : https://github.com/facebook/zstd/releases/download/v1.5.0/zstd-1.5.0.tar.gz.sig
Summary  : Fast lossless compression algorithm library and tools
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: zstd-filemap = %{version}-%{release}
Requires: zstd-lib = %{version}-%{release}
Requires: zstd-license = %{version}-%{release}
Requires: zstd-bin
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : lz4-dev
BuildRequires : lz4-dev32
BuildRequires : xz-dev
BuildRequires : xz-dev32
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
Patch1: multi-thread-default.patch
Patch2: notrace.patch
Patch3: fopen-use-m.patch
Patch4: allowpgo.patch

%description
Zstandard, or zstd as short version, is a fast lossless compression algorithm,
targeting real-time compression scenarios at zlib-level and better compression
ratios. It's backed by a very fast entropy stage, provided by Huff0 and FSE
library. The project is provided as an open-source dual BSD and GPLv2 licensed
C library, and a command line utility producing and decoding .zst, .gz, .xz and
.lz4 files.

%package dev
Summary: dev components for the zstd package.
Group: Development
Requires: zstd-lib = %{version}-%{release}
Provides: zstd-devel = %{version}-%{release}
Requires: zstd = %{version}-%{release}

%description dev
dev components for the zstd package.


%package dev32
Summary: dev32 components for the zstd package.
Group: Default
Requires: zstd-lib32 = %{version}-%{release}
Requires: zstd-dev = %{version}-%{release}

%description dev32
dev32 components for the zstd package.


%package filemap
Summary: filemap components for the zstd package.
Group: Default

%description filemap
filemap components for the zstd package.


%package lib
Summary: lib components for the zstd package.
Group: Libraries
Requires: zstd-license = %{version}-%{release}
Requires: zstd-filemap = %{version}-%{release}

%description lib
lib components for the zstd package.


%package lib32
Summary: lib32 components for the zstd package.
Group: Default
Requires: zstd-license = %{version}-%{release}

%description lib32
lib32 components for the zstd package.


%package license
Summary: license components for the zstd package.
Group: Default

%description license
license components for the zstd package.


%package staticdev
Summary: staticdev components for the zstd package.
Group: Default
Requires: zstd-dev = %{version}-%{release}

%description staticdev
staticdev components for the zstd package.


%package staticdev32
Summary: staticdev32 components for the zstd package.
Group: Default
Requires: zstd-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the zstd package.


%prep
%setup -q -n zstd-1.5.0
cd %{_builddir}/zstd-1.5.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
pushd ..
cp -a zstd-1.5.0 build32
popd
pushd ..
cp -a zstd-1.5.0 buildavx2
popd
pushd ..
cp -a zstd-1.5.0 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633976779
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
pushd build/meson
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both \
-Dbin_programs=false  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both \
-Dbin_programs=false  builddiravx2
ninja -v -C builddiravx2
CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both \
-Dbin_programs=false  builddiravx512
ninja -v -C builddiravx512
popd
pushd ../build32/build/meson
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Ddefault_library=both \
-Dbin_programs=false  builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/package-licenses/zstd
cp %{_builddir}/zstd-1.5.0/COPYING %{buildroot}/usr/share/package-licenses/zstd/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
cp %{_builddir}/zstd-1.5.0/LICENSE %{buildroot}/usr/share/package-licenses/zstd/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c
pushd ../build32/build/meson
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd build/meson
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
DESTDIR=%{buildroot}-v4 ninja -C builddiravx512 install
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
DESTDIR=%{buildroot} ninja -C builddir install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/zdict.h
/usr/include/zstd.h
/usr/include/zstd_errors.h
/usr/lib64/libzstd.so
/usr/lib64/pkgconfig/libzstd.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libzstd.so
/usr/lib32/pkgconfig/32libzstd.pc
/usr/lib32/pkgconfig/libzstd.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-zstd

%files lib
%defattr(-,root,root,-)
/usr/lib64/libzstd.so.1
/usr/lib64/libzstd.so.1.5.0
/usr/share/clear/optimized-elf/lib*

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libzstd.so.1
/usr/lib32/libzstd.so.1.5.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zstd/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
/usr/share/package-licenses/zstd/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libzstd.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libzstd.a
