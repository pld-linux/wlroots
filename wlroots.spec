#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	A modular Wayland compositor library
Summary(pl.UTF-8):	Modularna biblioteka kompozytora Wayland
Name:		wlroots
Version:	0.17.4
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://gitlab.freedesktop.org/wlroots/wlroots/-/releases/%{version}/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	fe99607962a594ae15155506982cfba0
Patch0:		x32.patch
URL:		https://gitlab.freedesktop.org/wlroots/wlroots
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libgbm-devel >= 21.1.0
BuildRequires:	OpenGLESv2-devel
BuildRequires:	Vulkan-Loader-devel >= 1.2.182
BuildRequires:	glslang >= 11.0.0
BuildRequires:	hwdata >= 0.364
BuildRequires:	libdisplay-info-devel
BuildRequires:	libdrm-devel >= 2.4.114
BuildRequires:	libinput-devel >= 1.19.0
BuildRequires:	libliftoff-devel >= 0.4.0
BuildRequires:	libseat-devel >= 0.2.0
BuildRequires:	libxcb-devel
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja
BuildRequires:	pixman-devel >= 0.42.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	udev-devel
BuildRequires:	wayland-devel >= 1.22
BuildRequires:	wayland-protocols >= 1.32
BuildRequires:	xcb-util-errors-devel
BuildRequires:	xcb-util-renderutil-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xorg-xserver-Xwayland-devel
Requires:	Mesa-libgbm >= 21.1.0
Requires:	Vulkan-Loader >= 1.2.182
Requires:	libdrm >= 2.4.114
Requires:	libinput >= 1.19.0
Requires:	libliftoff >= 0.4.0
Requires:	libseat >= 0.2.0
Requires:	pixman >= 0.42.0
Requires:	wayland >= 1.22
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

%description -l pl.UTF-8
Dołączalne, składalne moduły do tworzenia kompozytora Wayland; albo
około 50000 linii kodu, który i tak trzeba by napisać. Udostępnia
m.in.:
- backendy będące abstrakcją sprzętu wyświetlającego i wejściowego - w
  tym KMS/DRM, libinput, Wayland, X11 oraz samodzielne, oraz dowolne
  inne własne backendy, które można tworzyć i niszczyć w czasie
  działania programu, i wykorzystywać wraz z innymi
- w większości samodzielne implementacje wielu interfejsów Wayland,
  zarówno z wayland.xml, jak i różnych rozszerzeń protokołu
- kilka samodzielnych, opcjonalnych narzędzi, będących implementacją
  komponentów wspólnych dla wielu kompozytorów, takich jak układanie
  wyjść w przestrzeni fizycznej
- abstrakcję Xwayland
- abstrakcję renderowania, pozwalającą pominąć pisanie bezpośrednio
  kodu GL

%package devel
Summary:	Header files for wlroots library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wlroots
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	EGL-devel
Requires:	Mesa-libgbm-devel >= 21.1.0
Requires:	OpenGLESv2-devel
Requires:	Vulkan-Loader-devel >= 1.2.182
Requires:	libdrm-devel >= 2.4.114
Requires:	libinput-devel >= 1.19.0
Requires:	libseat-devel >= 0.2.0
Requires:	libxcb-devel
Requires:	pixman-devel >= 0.42.0
Requires:	systemd-devel >= 1:237
Requires:	udev-devel
Requires:	wayland-devel >= 1.22
Requires:	wayland-protocols >= 1.27
Requires:	xcb-util-errors-devel
Requires:	xcb-util-renderutil-devel
Requires:	xcb-util-wm-devel
Requires:	xorg-lib-libxkbcommon-devel

%description devel
Header files for wlroots library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wlroots.

%package static
Summary:	Static wlroots library
Summary(pl.UTF-8):	Statyczna biblioteka wlroots
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static wlroots library.

%description static -l pl.UTF-8
Statyczna biblioteka wlroots.

%prep
%setup -q
%patch -P0 -p1

%build
%meson \
	%{!?with_static_libs:--default-library=shared} \
	-Dexamples=false \
	-Dxwayland=enabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING.md README.md
%attr(755,root,root) %{_libdir}/libwlroots.so.12

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwlroots.so
%{_includedir}/wlr
%{_pkgconfigdir}/wlroots.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libwlroots.a
%endif
