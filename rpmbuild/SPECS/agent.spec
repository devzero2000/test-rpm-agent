Name:           agent
Version:        1.0
Release:        1
Summary:        agent
Group:          Testing
License:        GPL
BuildArch:	noarch

%description
agent

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin

cat <<'EOF' > $RPM_BUILD_ROOT/usr/local/bin/agent-post-install.sh
#!/bin/sh
echo "I am in agent postinstall!!!!"
EOF

%files
%defattr(755,root,root,-)
/usr/local/bin/agent-post-install.sh

