Summary:	Library for accessing USB devices
Name:		libusbx
Version:	1.0.17
Release:	0.1
Source0:	http://downloads.sourceforge.net/libusbx/%{name}-%{version}.tar.bz2
# Source0-md5:	99467ca2cb81c19c4a172de9f30e7576
License:	LGPL v2+
Group:		Libraries
URL:		http://sourceforge.net/apps/mediawiki/libusbx/
BuildRequires:	doxygen
BuildRequires:	systemd-devel
BuildRequires:	udev-devel
Provides:	libusb1 = %{version}-%{release}
Obsoletes:	libusb1 <= 1.0.9

%description
This package provides a way for applications to access USB devices.

Libusbx is a fork of the original libusb, which is a fully API and ABI
compatible drop in for the libusb-1.0.9 release. The libusbx fork was
started by most of the libusb-1.0 developers, after the original
libusb project did not produce a new release for over 18 months.

Note that this library is not compatible with the original libusb-0.1
series, if you need libusb-0.1 compatibility install the libusb
package.

%package        devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libusb1-devel = %{version}-%{release}
Obsoletes:	libusb1-devel <= 1.0.9

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-silent-rules \
	--enable-examples-build \

%{__make}
%{__make} -C doc docs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%doc doc/html examples/*.c
%{_includedir}/libusb-1.0
%{_libdir}/*.so
%{_pkgconfigdir}/libusb-1.0.pc
