for f in $(seq 10)
do
cat <<EOF> agent_$f.spec
Name:           agent_$f
Version:        1.0
Release:        1
Summary:        agent_$f
Group:          Testing
License:        GPL
BuildArch:	noarch

%description
agent_$f

%install

%files
%defattr(755,root,root,-)
EOF
done
