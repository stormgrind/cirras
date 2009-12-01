Summary:        CirrAS management for appliances
Name:           cirras-management
Version:        1.0.0.Beta1
Release:        1
License:        LGPL
Requires:       git
Requires:       shadow-utils
Requires:       ruby
Requires:       rubygems
Requires:       initscripts
Requires:       sed
Requires:       sudo
Requires:       ruby-devel
#Source0:        thin-ruby-env.patch
BuildRequires:  ruby
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        http://gems.rubyforge.org/gems/daemons-1.0.10.gem
Source1:        http://gems.rubyforge.org/gems/eventmachine-0.12.8.gem
Source2:        http://gems.rubyforge.org/gems/rack-1.0.0.gem
Source3:        http://gems.rubyforge.org/gems/thin-1.2.2.gem
Source4:        http://rubyforge.org/frs/download.php/52464/xml-simple-1.0.12.gem
BuildArch:      noarch

%description
CirrAS management for appliances.

%install
rm -rf $RPM_BUILD_ROOT

/usr/bin/git clone git://github.com/stormgrind/cirras-management.git $RPM_BUILD_ROOT/usr/share/%{name}

pushd $RPM_BUILD_ROOT/usr/share/%{name}
/usr/bin/git submodule init
/usr/bin/git submodule update

popd

install -d -m 755 $RPM_BUILD_ROOT/usr/share/%{name}-gems

cp %{SOURCE0} $RPM_BUILD_ROOT/usr/share/%{name}-gems
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/share/%{name}-gems
cp %{SOURCE2} $RPM_BUILD_ROOT/usr/share/%{name}-gems
cp %{SOURCE3} $RPM_BUILD_ROOT/usr/share/%{name}-gems
cp %{SOURCE4} $RPM_BUILD_ROOT/usr/share/%{name}-gems

%clean
rm -rf $RPM_BUILD_ROOT

%pre
#/bin/ln -s /usr/bin/ruby /usr/local/bin/ruby
/usr/sbin/groupadd -r thin 2>/dev/null || :
/usr/sbin/useradd -m -r -g thin thin 2>/dev/null || :

%post
/bin/mkdir -p /var/log/%{name}
/bin/chown thin:thin /var/log/%{name}
echo "sh /usr/share/%{name}/src/network-setup.sh" >> /etc/rc.local
echo -e "thin ALL = NOPASSWD: ALL\n" >> /etc/sudoers
/bin/sed -i s/"Defaults    requiretty"/"#Defaults    requiretty"/ /etc/sudoers

/usr/bin/gem install -ql /usr/share/%{name}-gems/*.gem

%files
%defattr(-,root,root)
/

%changelog
* Sat Nov 21 2009 Marek Goldmann 1.0.0.Beta1-1
- Initial release
