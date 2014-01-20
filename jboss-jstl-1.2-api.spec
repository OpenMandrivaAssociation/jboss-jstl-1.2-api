%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name: jboss-jstl-1.2-api
Version: 1.0.3
Release: 7.0%{?dist}
Summary: JSP Standard Template Library 1.2 API

License: CDDL or GPLv2 with exceptions
URL: http://www.jboss.org

# git clone git://github.com/jboss/jboss-jstl-api_spec.git jboss-jstl-1.2-api
# cd jboss-jstl-1.2-api/ && git archive --format=tar --prefix=jboss-jstl-1.2-api-1.0.3.Final/ jboss-jstl-api_1.2_spec-1.0.3.Final | xz > jboss-jstl-1.2-api-1.0.3.Final.tar.xz
Source0: %{name}-%{namedversion}.tar.xz

# Fix the FSF address in the license file:
Patch0: %{name}-fix-fsf-address.patch

BuildRequires: java-devel
BuildRequires: jboss-parent
BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: jboss-el-2.2-api
BuildRequires: jboss-servlet-3.0-api
BuildRequires: jboss-jsp-2.2-api
BuildRequires: xalan-j2

Requires: jpackage-utils
Requires: jboss-el-2.2-api
Requires: jboss-servlet-3.0-api
Requires: jboss-jsp-2.2-api
Requires: xalan-j2
Requires: java

BuildArch: noarch


%description
Java Server Pages Standard Template Library 1.2 API.


%package javadoc
Summary: Javadocs for %{name}

Requires: jpackage-utils


%description javadoc	
This package contains the API documentation for %{name}.


%prep

# Unpack the sources:
%setup -q -n %{name}-%{namedversion}

# Apply the patches:
%patch0 -p1


%build
mvn-rpmbuild install javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/jboss-jstl-api_1.2_spec-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE
%doc README


%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE
%doc README


%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.3-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jul 24 2012 Juan Hernandez <juan.hernandez@redhat.com> - 1.0.3-4
- Added maven-enforcer-plugin build time dependency

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 23 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.0.3-2
- Use global instead of define

* Thu Mar 22 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.0.3-1
- Update to upstream version 1.0.3
- Cleanup of the spec file

* Fri Aug 12 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging

