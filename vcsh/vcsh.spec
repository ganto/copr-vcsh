%global commit b8bd702362a260c22df3980767460190f8a0b1c1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           vcsh
Version:        1.20151229
Release:        0.3%{?dist}
Summary:        Version Control System for $HOME
Group:          Development/Tools

License:        GPLv2+
URL:            https://github.com/RichiH/vcsh
Source0:        https://github.com/RichiH/vcsh/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildArch:      noarch
Requires:       git

BuildRequires:  git


%description
vcsh allows you to have several git repositories, all maintaining their working
trees in $HOME without clobbering each other. That, in turn, means you can have
one repository per config set (zsh, vim, ssh, etc), picking and choosing which
configs you want to use on which machine.


%prep
%setup -qn %{name}-%{commit}


%build
make %{?_smp_mflags}


%install
%{make_install} DOCDIR=%{_pkgdocdir} ZSHDIR=%{_datadir}/zsh/site-functions


%files
%doc LICENSE CONTRIBUTORS changelog
%{_bindir}/%{name}
%{_mandir}/man*/%{name}*
# RHEL 6 doesn't support %%{_docdir}
%if 0%{?rhel} && 0%{?rhel} == 6
%doc doc/README.md doc/hooks
%else
%{_docdir}/*
%endif
%{_datadir}/zsh/


%changelog
* Sat May 25 2019 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.20151229-0.2
- Fix build failure on epel-6

* Thu May 23 2019 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.20151229-0.1
- Rebuild package for enterprise linux

* Mon Feb 22 2016 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20151229-2
- Declare %%_docdir in %%files

* Wed Feb 10 2016 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20151229-1
- Bumped version to 1.20151229

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20141026-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20141026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 26 2014 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20141026-1
- Bumped version to 1.20141026

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20140508-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20140508-1
- Bumped version to 1.20140508
- Switched to a commit tarball from github

* Sun Dec 15 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20131229-1
- Bumped version to 1.20131229

* Sun Dec 15 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20131214-1
- Bumped version to 1.20131214

* Tue Oct 22 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20130909-3
- The Makefile patch has been submitted upstream

* Sat Oct 19 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20130909-2
- Switched to _pkgdocdir
- Removed unnecessary `rm -rf %%{buildroot}' in clean and install

* Sat Oct 12 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20130909-1
- Initial package
