%define jboss_cache_version 3.2.1.GA

Summary:        JBoss Application Server
Name:           jboss-as6
Version:        6.0.0.M1
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source0:        http://internap.dl.sourceforge.net/sourceforge/jboss/jboss-%{version}.zip
Source1:        %{name}.init
Requires:       shadow-utils
Requires:       coreutils
Requires:       java-1.6.0-openjdk
Requires:       initscripts
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define runuser %{name}
%define __jar_repack %{nil}

%description
The JBoss Application Server

%prep
%setup -n jboss-%{version}

%install

cd %{_topdir}/BUILD

install -d -m 755 $RPM_BUILD_ROOT/opt/%{name}
cp -R jboss-%{version}/* $RPM_BUILD_ROOT/opt/%{name}
rm -Rf $RPM_BUILD_ROOT/opt/%{name}/server/*/deploy/ROOT.war
rm -rf $RPM_BUILD_ROOT/opt/%{name}/bin/jboss_init_solaris.sh 

install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/%{name}

touch $RPM_BUILD_ROOT/etc/jboss-as.conf
echo 'JBOSS_GOSSIP_PORT=12001'    >> $RPM_BUILD_ROOT/etc/jboss-as.conf
echo 'JBOSS_GOSSIP_REFRESH=5000'  >> $RPM_BUILD_ROOT/etc/jboss-as.conf
echo 'JAVA_HOME=/usr/lib/jvm/jre' >> $RPM_BUILD_ROOT/etc/jboss-as.conf

%clean
rm -Rf $RPM_BUILD_ROOT

%pre
JBOSS_SHELL=/bin/bash
/usr/sbin/groupadd -r %{name} 2>/dev/null || :
/usr/sbin/useradd -c JBossAS -r -s $JBOSS_SHELL -d /opt/%{name} -g %{name} %{name} 2>/dev/null || :

%post
/bin/echo "echo JBOSS_IP=\`ifconfig eth0 | awk '/inet addr/ {split (\$2,A,\":\"); print A[2]}'\` >> /etc/jboss-as.conf" >> /etc/rc.local

%files
%defattr(-,%{name},%{name})
/

%changelog
* Thu Dec 03 2009 Marek Goldmann 6.0.0.M1-1
- Initial release
