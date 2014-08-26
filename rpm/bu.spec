Name:         bu
Summary:      Manage the state of specific files and packages on a system.
Version:      0.4.61
Release:      1
BuildArch:    noarch
Group:        System Environment/Applications
Requires:     tar
License:      GPLv2
URL:          http://download.systemimager.org/pub/bu/
Source:       http://download.systemimager.org/pub/bu/%{name}-%{version}.tar.bz2
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
# buildrequires:    rpm-build, tar, make, rsync

%description
Have you ever edited a file, then realized, "Oh -- I should make a
backup of that first."  So you copy /etc/hosts to /etc/hosts.date_stamp,
etc.  That's what this tool does in an easy to use, consistent and
simple way.
.
The command 'bu /etc/hosts' copies /etc/hosts to
/etc/.bu_backups/hosts__2014.08.14-22:02:59.bz2.  Conveniently date and
time stamped in a naturally sortable way.
.
The command 'bu /etc' will create a tarball of /etc named in the same
fashion: /.bu_backups/etc__2014.08.14-22:03:07.tar.bz2.
.
Multiple items can be specified at the same time: 'bu this that /the/other'
.
http://download.systemimager.org/pub/bu/


%prep
%setup -n %{name}-%{version}


%build
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/%{_prefix}/share/doc/%{name} $RPM_BUILD_ROOT/%{_prefix}/share/doc/%{name}-%{version}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/sbin/*
%{_prefix}/share/*


# Get date command:   
#
#   sh echo -n "* " ; date +'%a %b %d %Y - brian@thefinleys.com'
#
%changelog -n %{name}
* Mon Aug 25 2014 - brian@thefinleys.com
- created spec file

