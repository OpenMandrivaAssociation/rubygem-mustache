Name:       rubygem-mustache
Version:    1.1.1
Release:    1
Summary:    Mustache is a framework-agnostic way to render logic-free views
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/defunkt/mustache
Source0:    http://rubygems.org/gems/mustache-%{version}.gem
BuildArch:  noarch
BuildRequires:	ruby

%description
Inspired by ctemplate, Mustache is a framework-agnostic way to render
logic-free views.
As ctemplates says, "It emphasizes separating logic from presentation:
it is impossible to embed application logic in this template
language.
Think of Mustache as a replacement for your views. Instead of views
consisting of ERB or HAML with random helpers and arbitrary logic,
your views are broken into two parts: a Ruby class and an HTML
template.

%prep
%autosetup -p1 -n %{gem_name}-%{version}

%build
%gem_build

%install
%gem_install

%files
%{_bindir}/mustache
%{gem_files}
