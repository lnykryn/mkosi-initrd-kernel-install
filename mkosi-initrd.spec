%global commit 2666ca9c864369f7803103d6744cf63a49ab8b4b
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

Name:    mkosi-initrd
Version: 0
Release: 2%{?dist}.%{shortcommit}
Summary: Create initrd with mkosi

License: Public Domain
Source0: https://github.com/systemd/mkosi-initrd/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1: 60-mkosi-initrd.install

Requires: mkosi >= 12
Requires: zstd
Requires: cpio
Requires: sed
Requires: python3-pyxattr

BuildRequires: /usr/bin/pathfix.py

%description
On kernel update create initrd by using mkosi

%prep
%setup -q -n %{name}-%{commit}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" mkosi.finalize 

%install
install -Dm0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE1}
install -Dm0644 -t %{buildroot}%{_prefix}/lib/mkosi-initrd/ fedora.mkosi
install -Dm0755 -t %{buildroot}%{_prefix}/lib/mkosi-initrd/ mkosi.finalize 

%files
%{_prefix}/lib/kernel/install.d/60-mkosi-initrd.install
%{_prefix}/lib/mkosi-initrd/

%changelog
* Fri Dec 03 2021 Lukas Nykryn <lnykryn@redhat.com> - 0-2.2666ca9
- add dependency to python3-pyxattr

* Fri Dec 03 2021 Lukas Nykryn <lnykryn@redhat.com> - 0-1.2666ca9
- new release
