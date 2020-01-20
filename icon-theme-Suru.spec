Name: icon-theme-Suru
Summary: The Suru icon theme
Version: 2020.01.19
Release: 3
Url: http://snwh.org/
Source0: https://github.com/snwh/suru-icon-theme/archive/master/suru-%{version}.tar.gz
Source1: https://github.com/Bonandry/suru-plus-ubuntu/archive/master/suru-plus-%{version}.tar.gz
# https://store.kde.org/p/1331950/
Source2: https://dllb2.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE1NzE2MzIxODkiLCJ1IjpudWxsLCJsdCI6ImRvd25sb2FkIiwicyI6Ijg5ZTc0ZGU1Yzk0NzI3YzdlNjNlNWVjNjUyMWRjMDNmNDkyYzJlNmE4NWQ2MWFmYzYxYjc5ZjE1YjdkOTE2Y2E4YjRjZmQ0ODRkYzkyYmFiNGUzZjZiNDBhMWMwZDA2OTRlNWU1NzIyNjBiNzY4YjdjYmY5NGExYzVlYzJlODNmIiwidCI6MTU3OTQ4Mzg2OCwic3RmcCI6ImMwMzNkZTY2MjM5M2E3NWZjNWM2MmY1MDliZjE3OTY1Iiwic3RpcCI6IjQ2LjkyLjE4MC41MCJ9.jVBg2ojA7b21smb3TIK6hdSI8J_FDDbHOcmOl7F_rxY/YaruKdeDark.tar.gz
# https://store.kde.org/p/1167950/
Source3: https://dllb2.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE1MjM1NDIyOTQiLCJ1IjpudWxsLCJsdCI6ImRvd25sb2FkIiwicyI6IjM4ZGQ2N2NhYjVlNjA3OWFjNzI5MTA1YWJlNGNkZjNiMzUwMDExMzM4YmE3ODlkOWZjMmVmNDM0ZWM3OGZlYjYxOTI1ZjNmM2YyMzk5MzE1NTgyODQ2MGRjNTkwMGY0OWFkYzU1ODUwNmM1OWZmMTY3ZjIyOTViMzY2YmUxNDBlIiwidCI6MTU3OTU1NTk5Nywic3RmcCI6ImMwMzNkZTY2MjM5M2E3NWZjNWM2MmY1MDliZjE3OTY1Iiwic3RpcCI6IjQ2LjkyLjE4MC41MCJ9.u1ZtfPIJ3Mpe2uyo7Wr454dfd6GnzK9_bm44ijjTt5w/United.tar.gz
# https://store.kde.org/p/998797
Source4: https://dllb2.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE0Nzc5NTg1MTUiLCJ1IjpudWxsLCJsdCI6ImRvd25sb2FkIiwicyI6IjJjZjg0NThhYzI5MmJjYWNmZGZiNmE0N2QxYzYwY2MyYjk1MzJiOTNhNTE4MWJlZjNlY2U3MTUzNDM5NWQ5M2Y4Y2ZiYWE2Zjk0M2FlOTllZTI4MDE0ODk0ZDVkNTlkYjZlMDQ3YWExNjkwOWIwNWI5NjJiNzRjMjU0NzU2NGZlIiwidCI6MTU3OTU1NjM1Mywic3RmcCI6ImMwMzNkZTY2MjM5M2E3NWZjNWM2MmY1MDliZjE3OTY1Iiwic3RpcCI6IjQ2LjkyLjE4MC41MCJ9.o00ouezVq3nsaLPjYxgGgKFwe9XnqnpY2c5kpLFD19s/UnityAmbiance.tar.gz
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
mkdir -p %{buildroot}%{_datadir}/plasma/look-and-feel
cd %{buildroot}%{_datadir}/plasma/look-and-feel
tar xf %{S:3}
mkdir -p %{buildroot}%{_datadir}/plasma/desktoptheme
cd %{buildroot}%{_datadir}/plasma/desktoptheme
tar xf %{S:4}

%files
%{_datadir}/icons/Suru
%{_datadir}/icons/Suru++
%{_datadir}/aurorae/themes/YaruKdeDark
%{_datadir}/plasma/look-and-feel/United
%{_datadir}/plasma/desktoptheme/UnityAmbiance
