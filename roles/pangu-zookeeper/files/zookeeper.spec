%define __jar_repack 0
%define debug_package %{nil}
%define name         zookeeper
%define _prefix      /opt
%define _conf_dir    %{_sysconfdir}/zookeeper
%define _log_dir     %{_var}/log/zookeeper

Summary: ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services.
Name: zookeeper
Version: %{version}
Release: %{build_number}
License: Apache License, Version 2.0
Group: Applications/Databases
URL: http://zookeper.apache.org/
Source: http://apache.mirrors.spacedump.net/zookeeper/zookeeper-%{version}/zookeeper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prefix: %{_prefix}
Vendor: Apache Software Foundation
Packager: zard <we_zard@163.com>
Provides: zookeeper

%description
ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications. Each time they are implemented there is a lot of work that goes into fixing the bugs and race conditions that are inevitable. Because of the difficulty of implementing these kinds of services, applications initially usually skimp on them ,which make them brittle in the presence of change and difficult to manage. Even when done correctly, different implementations of these services lead to management complexity when the applications are deployed.

%prep

%setup

%build

%install

mkdir -p $RPM_BUILD_ROOT%{_prefix}/zookeeper
cp -r $RPM_BUILD_DIR/zookeeper-3.4.6 $RPM_BUILD_ROOT%{_prefix}/
rm -rf $RPM_BUILD_ROOT%{_prefix}/zookeeper

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_prefix}

%changelog
* Sat Aug 8 2015 zard <we_zard@163.com> - 3.4.6
- initial release
