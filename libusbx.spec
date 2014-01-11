#
# Conditional build:
%bcond_without	static_libs	# static library
%bcond_without	udev		# udev for device enumeration and hotplug support
#
Summary:	Library for accessing USB devices
Summary(pl.UTF-8):	Biblioteka dostępu do urządzeń USB
Name:		libusbx
Version:	1.0.17
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libusbx/%{name}-%{version}.tar.bz2
# Source0-md5:	99467ca2cb81c19c4a172de9f30e7576
URL:		http://libusbx.org/
BuildRequires:	doxygen
BuildRequires:	glibc-devel >= 6:2.9
%{?with_udev:BuildRequires:	udev-devel}
Provides:	libusb = %{version}-%{release}
Obsoletes:	libusb < 1.0.10
Obsoletes:	libusb1 < 1.0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a way for applications to access USB devices.

Libusbx is a fork of the original libusb, which is a fully API and ABI
compatible drop in for the libusb-1.0.9 release. The libusbx fork was
started by most of the libusb-1.0 developers, after the original
libusb project did not produce a new release for over 18 months.

Note that this library is not compatible with the original libusb-0.1
series, if you need libusb-0.1 compatibility install the libusb-compat
package.

%description -l pl.UTF-8
Ten pakiet zapewnia aplikacjom sposób dostępu do urządzeń USB.

Libusbx to odgałęzienie oryginalnego libusb, w pełni zgodny co do API
i ABI zamiennik dla wydania libusb 1.0.9. Został utworzony przez
większość programistów libusb-1.0 po tym, jak oryginalny projekt nie
wydał nowej wersji przez ponad 18 miesięcy.

Uwaga: ta biblioteka nie jest zgodna z pierwotną serią libusb-0.1; dla
zgodności z nią należy zainstalować pakiet libusb-compat.

%package devel
Summary:	Header files for libusbx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libusbx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_udev:Requires:	udev-devel}
Provides:	libusb-devel = %{version}-%{release}
Obsoletes:	libusb-devel < 1.0.10
Obsoletes:	libusb1-devel < 1.0.10

%description devel
This package contains the header files for developing applications
that use libusbx.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do rozwijania aplikacji
wykorzystujących bibliotekę libusbx.

%package static
Summary:	Static libusbx library
Summary(pl.UTF-8):	Statyczna biblioteka libusbx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libusb-static = %{version}-%{release}
Obsoletes:	libusb-static < 1.0.10
Obsoletes:	libusb1-static < 1.0.10

%description static
Static libusbx library.

%description static -l pl.UTF-8
Statyczna biblioteka libusbx.

%prep
%setup -q

%build
%configure \
	--enable-examples-build \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	%{!?with_udev:--disable-udev}

%{__make}
%{__make} -C doc docs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libusb-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libusb-1.0.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/html examples/*.c
%attr(755,root,root) %{_libdir}/libusb-1.0.so
%{_includedir}/libusb-1.0
%{_pkgconfigdir}/libusb-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libusb-1.0.a
