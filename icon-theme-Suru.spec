Name: icon-theme-Suru
Summary: The Suru icon theme
Version: 2020.01.19
Release: 2
Url: http://snwh.org/
Source0: https://github.com/snwh/suru-icon-theme/archive/master/suru-%{version}.tar.gz
Source1: https://github.com/Bonandry/suru-plus-ubuntu/archive/master/suru-plus-%{version}.tar.gz
Source2: https://dllb2.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE1NzE2MzIxODkiLCJ1IjpudWxsLCJsdCI6ImRvd25sb2FkIiwicyI6Ijg5ZTc0ZGU1Yzk0NzI3YzdlNjNlNWVjNjUyMWRjMDNmNDkyYzJlNmE4NWQ2MWFmYzYxYjc5ZjE1YjdkOTE2Y2E4YjRjZmQ0ODRkYzkyYmFiNGUzZjZiNDBhMWMwZDA2OTRlNWU1NzIyNjBiNzY4YjdjYmY5NGExYzVlYzJlODNmIiwidCI6MTU3OTQ4Mzg2OCwic3RmcCI6ImMwMzNkZTY2MjM5M2E3NWZjNWM2MmY1MDliZjE3OTY1Iiwic3RpcCI6IjQ2LjkyLjE4MC41MCJ9.jVBg2ojA7b21smb3TIK6hdSI8J_FDDbHOcmOl7F_rxY/YaruKdeDark.tar.gz
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
sed -i -e 's,Humanity,breeze-dark,g' %{buildroot}%{_datadir}/icons/*/index.theme
# Let's add a KWin decoration to make it complete
mkdir -p %{buildroot}%{_datadir}/aurorae/themes
cd %{buildroot}%{_datadir}/aurorae/themes
tar xf %{S:2}

%files
%{_datadir}/icons/Suru
%{_datadir}/icons/Suru++
%{_datadir}/aurorae/themes/YaruKdeDark
