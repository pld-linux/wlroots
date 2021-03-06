Summary:	A modular Wayland compositor library
Name:		wlroots
Version:	0.14.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/swaywm/wlroots/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3fbe8f81d2ba59362f041940869ed1e2
Patch0:		x32.patch
URL:		https://github.com/swaywm/wlroots
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libgbm-devel >= 21.1.0
BuildRequires:	OpenGLESv2-devel
BuildRequires:	libdrm-devel >= 2.4.105
BuildRequires:	libinput-devel >= 1.14.0
BuildRequires:	libseat-devel >= 0.2.0
BuildRequires:	libxcb-devel
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	udev-devel
BuildRequires:	wayland-devel >= 1.19
BuildRequires:	wayland-protocols >= 1.21
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xorg-xserver-Xwayland-devel
Requires:	Mesa-libgbm >= 21.1.0
Requires:	libdrm >= 2.4.105
Requires:	libinput >= 1.14.0
Requires:	libseat-devel >= 0.2.0
Requires:	wayland >= 1.18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pluggable, composable, unopinionated modules for building a Wayland
compositor; or about 50,000 lines of code you were going to write
anyway.
- wlroots provides backends that abstract the underlying display and
  input hardware, including KMS/DRM, libinput, Wayland, X11, and
  headless backends, plus any custom backends you choose to write, which
  can all be created or destroyed at runtime and used in concert with
  each other.
- wlroots provides unopinionated, mostly standalone implementations of
  many Wayland interfaces, both from wayland.xml and various protocol
  extensions. We also promote the standardization of portable extensions
  across many compositors.
- wlroots provides several powerful, standalone, and optional tools
  that implement components common to many compositors, such as the
  arrangement of outputs in physical space.
- wlroots provides an Xwayland abstraction that allows you to have
  excellent Xwayland support without worrying about writing your own X11
  window manager on top of writing your compositor.
- wlroots provides a renderer abstraction that simple compositors can
  use to avoid writing GL code directly, but which steps out of the way
  when your needs demand custom rendering code.

%package devel
Summary:	Header files for wlroots library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	EGL-devel
Requires:	Mesa-libgbm-devel >= 21.1.0
Requires:	OpenGLESv2-devel
Requires:	libdrm-devel >= 2.4.105
Requires:	libinput-devel >= 1.14.0
Requires:	libxcb-devel
Requires:	pixman-devel
Requires:	systemd-devel >= 237
Requires:	udev-devel
Requires:	wayland-devel >= 1.19
Requires:	wayland-protocols >= 1.17
Requires:	xcb-util-wm-devel
Requires:	xorg-lib-libxkbcommon-devel

%description devel
Header files for wlroots library.

%package static
Summary:	Static wlroots library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static wlroots library.

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	-Dxwayland=enabled
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING.md README.md
%attr(755,root,root) %{_libdir}/libwlroots.so.9

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwlroots.so
%{_includedir}/wlr
%{_pkgconfigdir}/wlroots.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libwlroots.a
