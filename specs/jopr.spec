Summary:        JOPR
Name:           jopr
Version:        2.2.1
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source0:        http://softlayer.dl.sourceforge.net/project/rhq/jopr/jopr-%{version}/jopr-server-%{version}.zip
Source1:        preconfigure-jopr-agent.sh
Source2:        agent-configuration.xml
Source3:        jopr.init
Source100:	    find-external-requires.sh
Requires:       shadow-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define runuser jopr
%define __jar_repack %{nil}
%define __find_requires %{SOURCE100}
AutoProv: 0
%define _use_internal_dependency_generator 0

%description
Jopr is an enterprise management solution for JBoss middleware projects and other application technologies. This pluggable project provides administration, monitoring, alerting, operational control and configuration in an enterprise setting with fine-grained security and an advanced extension model. This system is based on and plugin-compatible with the multi-vendor RHQ management project. It provides support for monitoring base operating system information on six operating systems as well as mangement of Apache, JBoss Application Server and other related projects.

%prep
%setup -n jopr-server-%{version}
chmod +x %{SOURCE100}

%install
install -d -m 755 $RPM_BUILD_ROOT/opt/jopr
cp -R . $RPM_BUILD_ROOT/opt/jopr

chmod +x %{SOURCE1}

install -d -m 755 $RPM_BUILD_ROOT/usr/share/jopr
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/share/jopr
cp %{SOURCE2} $RPM_BUILD_ROOT/usr/share/jopr

install -d -m 755 $RPM_BUILD_ROOT/etc/sysconfig
touch $RPM_BUILD_ROOT/etc/sysconfig/jopr 

install -d -m 755 $RPM_BUILD_ROOT/etc/init.d
cp %{SOURCE3} $RPM_BUILD_ROOT/etc/init.d/jopr 

%clean
rm -Rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -r jopr 2>/dev/null || :
/usr/sbin/useradd -c "JBoss JOPR" -r -s /bin/bash -d /opt/jboss-jopr -g jopr jopr 2>/dev/null || :

%files
%defattr(-,jopr,jopr)
/

%changelog
* Sat Jul 25 2009 Marek Goldmann 2.2.1
- Initial packaging
