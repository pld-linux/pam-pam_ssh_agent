%define 	modulename pam_ssh_agent
Summary:	PAM module for ssh agent auth 
Summary(pl):	Modu³ PAM uwierzytelniaj±cy u¿ytkowników poprzez agenta ssh 
Name:		pam-%{modulename}
Version:	0.2
Release:	0.1
License:	GPL
Group:		Base
Source0:	http://dl.sourceforge.net/pam-ssh-agent/%{modulename}-%{version}.tar.gz
# Source0-md5:	3514f813c6df58de28cc56c7c76566d7
URL:		http://sourceforge.net/projects/pam-ssh-agent/
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pam_ssh_agent is a PAM module that spawns an ssh-agent and adds
identities using the password supplied by the user at login. 

%description -l pl
pam_ssh_agent to modu³ PAM uruchamiaj±cy agenta ssh i dodaj±cy
to¿samo¶æ przy u¿yciu has³a podanego przez u¿ytkownika przy logowaniu.

%prep
%setup -q -n %{modulename}-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DLINUX_PAM -D_POSIX_SOURCE -Wall -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

install -D %{modulename}.so $RPM_BUILD_ROOT/%{_lib}/security/%{modulename}.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) /%{_lib}/security/%{modulename}.so
