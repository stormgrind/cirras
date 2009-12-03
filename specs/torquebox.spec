%define jboss_name jboss-as6

Summary:    TorqueBox
Name:       torquebox
Version:    1.0.0.Beta18
Release:    1
License:    LGPL
BuildArch:  noarch
Group:      Applications/System
Source0:    http://repository.torquebox.org/maven2/releases/org/torquebox/torquebox-core/%{version}/torquebox-core-%{version}-deployer.jar
Requires:   %{jboss_name}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define __jar_repack %{nil}

%description
The Torquebox deployer for AS 6

%prep
%setup -c torquebox.deployer -T

%install
## every config but minimal
configs=( all  default  standard  web )

for config in ${configs[@]} ; do
  install -d 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/${config}/deployers/
  cp %SOURCE0 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/${config}/deployers/
done

%clean
rm -Rf $RPM_BUILD_ROOT

%pre

%files
%defattr(-,%{jboss_name},%{jboss_name})
/

%changelog
* Fri Nov 20 2009 Marek Goldmann 1.0.0.Beta18
- Upgrade to version 1.0.0.Beta18

* Tue Oct 20 2009 Marek Goldmann 1.0.0.Beta16
- Upgrade to version 1.0.0.Beta16

* Tue Jun 23 2009 Marek Goldmann 1.0.0.Beta13
- Upgrade to version 1.0.0.Beta13

* Fri May 22 2009 Marek Goldmann 1.0.0.Beta11
- Update after project name change to TorqueBox

* Tue Apr 28 2009 Marek Goldmann 1.0.0.Beta6
- Upgrade to Beta6