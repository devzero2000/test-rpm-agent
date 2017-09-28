Name:           meta-package
Version:        1.0
Release:        1
Summary:        meta-package
Group:          Testing
License:        GPL
BuildArch:	noarch
OrderWithRequires: createlv
Requires: agent,agent_1,agent_2,agent_3,agent_4,agent_5,agent_6,agent_7,agent_8,agent_9,agent_10 

%description
meta-package

%files
%defattr(-,root,root,-)


%pre
echo "i am in pre of %{name}\n"
/usr/local/bin/agent-post-install.sh || exit 1


