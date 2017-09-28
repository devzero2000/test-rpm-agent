Name:           createlv
Version:        1.0
Release:        1
Summary:        createlv
Group:          Testing
License:        GPL
BuildArch:	noarch

%description
createlv

%files
%defattr(-,root,root,-)

%pre

ls -l /tmp >/tmp/${name}-${release}.$$.lis || exit 1
