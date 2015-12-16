%{?scl:%scl_package nodejs-mime-types}
%{!?scl:%global pkg_name %{name}}
%global npm_name mime-types

%{?nodejs_find_provides_and_requires}

%{!?scl:%global enable_tests 0}

Name:		%{?scl_prefix}nodejs-mime-types
Version:	2.1.3
Release:	1%{?dist}
Summary:	The ultimate javascript content-type utility.
Url:		https://github.com/jshttp/mime-types
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	npm(istanbul)
BuildRequires:	npm(mocha)
%endif

%description
The ultimate javascript content-type utility.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
mocha --reporter spec test/test.js
%endif

%files
%{nodejs_sitelib}/mime-types

%doc README.md
%license LICENSE

%changelog
* Thu Jul 16 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.1.3-1
- Initial build
