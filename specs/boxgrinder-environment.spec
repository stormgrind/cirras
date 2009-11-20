%define maven_version 2.2.1

Summary:        BoxGrinder environment
Name:           boxgrinder-environment
Version:        1.0.0.Beta1
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source0:        http://www.apache.org/dist/maven/binaries/apache-maven-2.2.1-bin.tar.gz
Source1:        %{name}-sudo-user.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       shadow-utils
Requires:       git

%description
BoxGrinder environment. Required tools and source code for building appliances.

%prep
%setup -n apache-maven-%{maven_version}

%install
rm -Rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT/opt/%{name}/tools/apache-maven-%{maven_version}
install -d -m 755 $RPM_BUILD_ROOT/opt/%{name}/patches

cp -R * $RPM_BUILD_ROOT/opt/%{name}/tools/apache-maven-%{maven_version}
cp %{SOURCE1} $RPM_BUILD_ROOT/opt/%{name}/patches/

%clean
rm -Rf $RPM_BUILD_ROOT

%post

/usr/sbin/useradd -m -p '$1$LxTRJ/$WIyjiQ5521QRECVt9Ded90' boxgrinder
/bin/chown boxgrinder:boxgrinder /opt/%{name} -R

patch -s /etc/sudoers < /opt/%{name}/patches/%{name}-sudo-user.patch

/bin/echo "### BoxGrinder vars, do not modify these lines! ###" >> /home/boxgrinder/.bashrc
/bin/echo "export PATH=$PATH:/opt/%{name}/tools/apache-maven-%{maven_version}/bin:/usr/local/bin" >> /home/boxgrinder/.bashrc
/bin/echo "export JAVA_HOME=/usr/lib/jvm/java-openjdk" >> /home/boxgrinder/.bashrc

%preun

patch -sR /etc/sudoers < /opt/%{name}/patches/%{name}-sudo-user.patch

%files
%defattr(-,root,root)
/

%changelog
* Wed May 13 2009 Marek Goldmann 1.0.0.Beta4-1
- Removed hardcoded gems

* Fri Apr 03 2009 Marek Goldmann 1.0.0.Beta3-1
- Maven version upgrade to 2.1.0

* Mon Mar 02 2009 Marek Goldmann 1.0.0.Beta3
- Maven version upgrade
