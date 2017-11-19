#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zstd
Version  : 1.3.2
Release  : 16
URL      : https://github.com/facebook/zstd/archive/v1.3.2.tar.gz
Source0  : https://github.com/facebook/zstd/archive/v1.3.2.tar.gz
Summary  : fast lossless compression algorithm library
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: zstd-bin
Requires: zstd-lib
Requires: zstd-doc
BuildRequires : cmake
BuildRequires : meson
BuildRequires : ninja
BuildRequires : python3
BuildRequires : zlib-dev

%description
This Meson project is provided with no guarantee and maintained by Dima Krasner <dima@dimakrasner.com>.

%package bin
Summary: bin components for the zstd package.
Group: Binaries

%description bin
bin components for the zstd package.


%package dev
Summary: dev components for the zstd package.
Group: Development
Requires: zstd-lib
Requires: zstd-bin
Provides: zstd-devel

%description dev
dev components for the zstd package.


%package doc
Summary: doc components for the zstd package.
Group: Documentation

%description doc
doc components for the zstd package.


%package lib
Summary: lib components for the zstd package.
Group: Libraries

%description lib
lib components for the zstd package.


%prep
%setup -q -n zstd-1.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511114901
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
make

%install
export SOURCE_DATE_EPOCH=1511114901
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/lib64
cp lib/libzstd.so.1.*  %{buildroot}/usr/lib64
ln -s libzstd.so.1.3.1   %{buildroot}/usr/lib64/libzstd.so
ln -s libzstd.so.1.3.1   %{buildroot}/usr/lib64/libzstd.so.1
mv %{buildroot}/usr/local/* %{buildroot}/usr
mv %{buildroot}/usr/lib/pkgconfig %{buildroot}/usr/lib64
rm  %{buildroot}/usr/lib/*so*
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unzstd
/usr/bin/zstd
/usr/bin/zstdcat
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/zstdmt

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libzstd.so
/usr/lib64/pkgconfig/libzstd.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libzstd.so.1
/usr/lib64/libzstd.so.1.3.2
