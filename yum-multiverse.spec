%define   debug_package %{nil}

Summary:       Yum multiversion plugin
Name:          yum-plugin-multiverse
Version:       0.0.1
Release:       0
License:       Proprietary
Group:         Development/Languages
Source:        yum-multiverse.tgz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:     noarch
Requires:      yum-allowdowngrade

%description
Yum multiversion plugin allows installation of multiple packages
with the same version, if specified in the repo configuration.

%prep
%setup -q -c -n greyhound

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

mkdir -p %{buildroot}/etc/yum/pluginconf.d/
mkdir -p %{buildroot}/usr/lib/yum-plugins/

cp -avf multiverse.conf %{buildroot}/etc/yum/pluginconf.d/
cp -avf multiverse.py %{buildroot}/usr/lib/yum-plugins/

chmod a+x %{buildroot}/usr/lib/yum-plugins/multiverse.py


%files
%defattr(-, root, root, 0755)
/etc/yum/pluginconf.d/multiverse.conf
/usr/lib/yum-plugins/multiverse.py
%ghost /usr/lib/yum-plugins/*.pyc
%ghost /usr/lib/yum-plugins/*.pyo
