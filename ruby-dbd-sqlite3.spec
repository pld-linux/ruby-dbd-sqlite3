Summary:	Ruby Database driver for Sqlite3
Name:		ruby-dbd-sqlite3
Version:	1.2.2
Release:	1
License:	Ruby License
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/41797/dbd-sqlite3-%{version}.tar.gz
# Source0-md5:	26b117cebddae40395124ac16276dd5f
URL:		http://rubyforge.org/projects/ruby-dbi/
BuildRequires:	ruby-modules
Requires:	sqlite3-ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby Database driver for Sqlite.

%prep
%setup -q -n dbd-sqlite3-%{version}

%build
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/dbd/sqlite3
%{ruby_rubylibdir}/dbd/SQLite3.rb
