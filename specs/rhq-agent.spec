%define agent_name rhq-enterprise-agent
%define rhq_version 1.4.0.B01

Summary:        RHQ Agent
Name:           rhq-agent
Version:        %{rhq_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Source0:        rhq-agent.init
Source1:        rhq-agent-install.sh
Group:          Applications/System
Requires:       java-1.6.0-openjdk
Requires(post): /sbin/chkconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define runuser %{name}

%description
The RHQ project is an abstraction and plug-in based systems management suite that provides extensible and integrated systems management for multiple products and platforms across a set of core features. The project is designed with layered modules that provide a flexible architecture for deployment. It delivers a core user interface that delivers audited and historical management across an entire enterprise. A Server/Agent architecture provides remote management and plugins implement all specific support for managed products. RHQ is an open source project licensed under the GPL, with some pieces individually licensed under a dual GPL/LGPL license to facilitate the integration with extended packages such as Jopr and Embedded Jopr.

%install
install -d -m 755 $RPM_BUILD_ROOT/etc/sysconfig

echo "RHQ_AGENT_VERSION=%{version}"       > $RPM_BUILD_ROOT/etc/sysconfig/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_initrddir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT/usr/share/%{name}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/usr/share/%{name}/rhq-agent-install.sh

%clean
rm -Rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -r %{name} 2>/dev/null || :
/usr/sbin/useradd -c "%{name}" -r -s /bin/bash -d /opt/%{name} -g %{name} %{name} 2>/dev/null || :

%post
/sbin/chkconfig --add %{name}
/sbin/chkconfig %{name} on

%files
%defattr(-,root,root)
/

%changelog
* Tue Dec 24 2009 Marek Goldmann 1.4.0.B01
- Upgrade to version 1.4.0.B01

* Thu Sep 24 2009 Marek Goldmann 1.3.1
- Upgrade to version 1.3.1

* Sat Jul 25 2009 Marek Goldmann 1.2.1
- Initial packaging
