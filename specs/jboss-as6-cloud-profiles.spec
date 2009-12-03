%define jboss_name jboss-as6
%define jboss_version 6.0.0.M1

Summary:        The JBoss AS 6 cloud profiles (cluster and group)
Name:           jboss-as6-cloud-profiles
Version:        1.0.0.Beta1
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source0:        http://internap.dl.sourceforge.net/sourceforge/jboss/jboss-%{jboss_version}.zip
Source1:        %{jboss_name}-gossip-jvmroute.patch
Source2:        %{jboss_name}-mod_cluster.patch
Source3:        %{jboss_name}-jbossws-host.patch

Requires:       %{jboss_name}
BuildRequires:  patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The JBoss AS 6 cloud profiles (cluster and group)

%define __jar_repack %{nil}

%prep
%setup -T -b 0 -n jboss-%{jboss_version}

%install
rm -Rf $RPM_BUILD_ROOT

cd %{_topdir}/BUILD

# create directories
mkdir -p $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster
mkdir -p $RPM_BUILD_ROOT/opt/%{jboss_name}/server/group

# copy profiles
cp -R jboss-%{jboss_version}/server/default/* $RPM_BUILD_ROOT/opt/%{jboss_name}/server/group/
cp -R jboss-%{jboss_version}/server/all/* $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster/

rm -Rf $RPM_BUILD_ROOT/opt/%{jboss_name}/server/*/deploy/ROOT.war

cd $RPM_BUILD_ROOT/opt/%{jboss_name}
patch -p1 < %{SOURCE1}
patch -p1 < %{SOURCE2}
patch -p1 < %{SOURCE3}

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,%{jboss_name},%{jboss_name})
/

%changelog
* Thu Dec 03 2009 Marek Goldmann 1.0.0.Beta1-1
- Initial release