%define __jar_repack 0
%define debug_package %{nil}
%define name         apache-storm
%define _prefix      /opt
%define _conf_dir    %{_sysconfdir}/storm
%define _log_dir     %{_var}/log/storm

Summary: Apache Storm is a free and open source distributed realtime computation system.
Name: apache-storm
Version: %{version}
Release: %{build_number}
License: Apache License, Version 2.0
Group: Applications/Databases
URL: http://apache.mirrors.hoobly.com
Source: http://apache.mirrors.hoobly.com/storm/apache-storm-0.9.4/apache-storm-0.9.4.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prefix: %{_prefix}
Vendor: Apache Software Foundation
Packager: zard <we_zard@163.com>
Provides: storm

%description
Storm has many use cases: realtime analytics, online machine learning, continuous computation, distributed RPC, ETL, and more. Storm is fast: a benchmark clocked it at over a million tuples processed per second per node. It is scalable, fault-tolerant, guarantees your data will be processed, and is easy to set up and operate.

%prep

%setup


%build

%install

mkdir -p $RPM_BUILD_ROOT%{_prefix}/storm
cp -r $RPM_BUILD_DIR/apache-storm-0.9.4 $RPM_BUILD_ROOT%{_prefix}/
rm -rf $RPM_BUILD_ROOT%{_prefix}/storm

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_prefix}

%changelog
* Sat Aug 8 2015 zard <we_zard@163.com> - 0.9.4
- initial release
