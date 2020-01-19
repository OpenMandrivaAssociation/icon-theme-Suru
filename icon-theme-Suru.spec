Name: icon-theme-Suru
Summary: The Suru icon theme
Version: 2020.01.19
Release: 1
Url: http://snwh.org/
Source0: https://github.com/snwh/suru-icon-theme/archive/master/suru-%{version}.tar.gz
Source1: https://github.com/Bonandry/suru-plus-ubuntu/archive/master/suru-plus-%{version}.tar.gz
Group: Graphical Desktop/KDE
License: GPLv3/CC-BY-SA 4.0
BuildArch: noarch
Suggests: qt-theme-kvantum
BuildRequires: meson

%description
The Suru icon theme

%prep
%autosetup -p1 -n suru-icon-theme-master -a 1
%meson

%build
%meson_build

%install
%meson_install
# We're not Ubuntu...
sed -i -e 's, Ubuntu,,g' suru-plus-ubuntu-master/Suru++-Ubuntu/index.theme
cp -a suru-plus-ubuntu-master/Suru++-Ubuntu/ %{buildroot}%{_datadir}/icons/Suru++
# And we don't have their default theme
sed -i -e 's,Humanity,breeze-dark,g' %{buildroot}%{_datadir}/icons/Suru/index.theme

%files
%{_datadir}/icons/Suru
%{_datadir}/icons/Suru++
