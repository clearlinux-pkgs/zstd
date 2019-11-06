#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : zstd
Version  : 1.4.4
Release  : 54
URL      : https://github.com/facebook/zstd/releases/download/v1.4.4/zstd-1.4.4.tar.gz
Source0  : https://github.com/facebook/zstd/releases/download/v1.4.4/zstd-1.4.4.tar.gz
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
BuildRequires : util-linux
BuildRequires : xz-dev
BuildRequires : zlib-dev
Patch1: multi-thread-default.patch

%description
# Parallel Zstandard (PZstandard)
Parallel Zstandard is a Pigz-like tool for Zstandard.
It provides Zstandard format compatible compression and decompression that is able to utilize multiple cores.
It breaks the input up into equal sized chunks and compresses each chunk independently into a Zstandard frame.
It then concatenates the frames together to produce the final compressed output.
Pzstandard will write a 12 byte header for each frame that is a skippable frame in the Zstandard format, which tells PZstandard the size of the next compressed frame.
PZstandard supports parallel decompression of files compressed with PZstandard.
When decompressing files compressed with Zstandard, PZstandard does IO in one thread, and decompression in another.

%package bin
Summary: bin components for the zstd package.
Group: Binaries
Requires: zstd-license = %{version}-%{release}

%description bin
bin components for the zstd package.


%package dev
Summary: dev components for the zstd package.
Group: Development
Requires: zstd-lib = %{version}-%{release}
Requires: zstd-bin = %{version}-%{release}
Provides: zstd-devel = %{version}-%{release}
Requires: zstd = %{version}-%{release}
Requires: zstd = %{version}-%{release}

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


%package staticdev
Summary: staticdev components for the zstd package.
Group: Default
Requires: zstd-dev = %{version}-%{release}
Requires: zstd-dev = %{version}-%{release}

%description staticdev
staticdev components for the zstd package.


%prep
%setup -q -n zstd-1.4.4
%patch1 -p1
pushd ..
cp -a zstd-1.4.4 buildavx2
popd

%build
## build_prepend content
pushd build/meson
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573048435
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=haswell" CXXFLAGS="$CXXFLAGS -m64 -march=haswell " LDFLAGS="$LDFLAGS -m64 -march=haswell" meson --libdir=lib64/haswell --prefix=/usr --buildtype=plain -Ddefault_library=both  builddiravx2
ninja -v -C builddiravx2
CFLAGS="$CFLAGS -m64 -march=haswell" CXXFLAGS="$CXXFLAGS -m64 -march=haswell " LDFLAGS="$LDFLAGS -m64 -march=haswell" meson --prefix /usr --libdir=/usr/lib64/haswell --buildtype=plain -Ddefault_library=both  builddiravx2
ninja -v -C builddiravx2

%install
## install_prepend content
pushd build/meson
cp ../../COPYING .
cp ../../LICENSE .
cp -a ../../contrib .
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/zstd
cp %{_builddir}/zstd-1.4.4/COPYING %{buildroot}/usr/share/package-licenses/zstd/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
cp %{_builddir}/zstd-1.4.4/LICENSE %{buildroot}/usr/share/package-licenses/zstd/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c
cp %{_builddir}/zstd-1.4.4/contrib/linux-kernel/COPYING %{buildroot}/usr/share/package-licenses/zstd/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
DESTDIR=%{buildroot} ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
## install_append content
popd
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/haswell/pkgconfig/libzstd.pc

%files bin
%defattr(-,root,root,-)
/usr/bin/unzstd
/usr/bin/zstd
/usr/bin/zstd-frugal
/usr/bin/zstdcat
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/zstdmt

%files dev
%defattr(-,root,root,-)
/usr/include/zbuff.h
/usr/include/zdict.h
/usr/include/zstd.h
/usr/include/zstd_errors.h
/usr/lib64/haswell/libzstd.so
/usr/lib64/libzstd.so
/usr/lib64/pkgconfig/libzstd.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libzstd.so.1
/usr/lib64/haswell/libzstd.so.1.4.4
/usr/lib64/libzstd.so.1
/usr/lib64/libzstd.so.1.4.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zstd/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
/usr/share/package-licenses/zstd/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/unzstd.1
/usr/share/man/man1/zstd.1
/usr/share/man/man1/zstdcat.1
/usr/share/man/man1/zstdgrep.1
/usr/share/man/man1/zstdless.1
/usr/share/man/man1/zstdmt.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/haswell/libzstd.a
/usr/lib64/libzstd.a
