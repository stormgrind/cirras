Summary:    Management appliance helper RPM
Name:       cirras-management-appliance
Version:    1.0.0.Beta1
Release:    1
License:    LGPL
BuildArch:  noarch
Requires:   postgresql
Requires(post): /sbin/chkconfig
Requires(post): /bin/sed
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Management appliance helper RPM

%post
/sbin/chkconfig postgresql on
/sbin/service postgresql initdb
/bin/sed -i s/'host all all 127.0.0.1\/32 ident sameuser'/'host all all 127.0.0.1\/32 md5'/g /var/lib/pgsql/data/pg_hba.conf

%clean
rm -Rf $RPM_BUILD_ROOT

%files