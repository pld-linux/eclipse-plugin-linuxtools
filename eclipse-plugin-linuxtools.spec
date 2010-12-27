%define		plugin_name	linuxtools

Summary:	Eclipse Linux Tools
Name:		eclipse-plugin-%{plugin_name}
Version:	0.6.0
Release:	0.1
License:	EPL
Group:		Development/Tools
Source0:	http://archive.eclipse.org/technology/linuxtools/S201006091041/linuxtools-Update-%{version}.zip
# Source0-md5:	a3b65284ae2c08b20006e551f571943d
URL:		http://www.eclipse.org/linuxtools/
BuildRequires:	unzip
Requires:	eclipse >= 3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/eclipse/dropins/%{plugin_name}

%description
Eclipse Linux Tools.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}/eclipse/{features,plugins}

cp -r * $RPM_BUILD_ROOT%{_plugindir}/eclipse

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_plugindir}
%dir %{_plugindir}/eclipse
%dir %{_plugindir}/eclipse/features
%{_plugindir}/eclipse/features/*.jar
%dir %{_plugindir}/eclipse/plugins
%{_plugindir}/eclipse/plugins/org.eclipse.linuxtools.*.jar
