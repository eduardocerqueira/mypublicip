.. _release:


Build
======

From your local machine
-----------------------

 ::

	$ cd mypublicip
	$ make

	Usage: make <target> where <target> is one of

	clean     clean temp files from local workspace
	doc       generate sphinx documentation and man pages
	test      run unit tests locally
	tarball   generate tarball of project
	rpm       build source codes and generate rpm file
	srpm      generate SRPM file
	all       clean test doc rpm
	flake8    check Python style based on flake8


	$ make rpm

	#rpmdev-setuptree into project folder
	make -C docs/ html
	make[1]: Entering directory '/home/eduardo/git/mypublicip/docs'
	sphinx-build -b html -d build/doctrees   source build/html
	Running Sphinx v1.4.8
	loading pickled environment... done
	building [mo]: targets for 0 po files that are out of date
	building [html]: targets for 2 source files that are out of date
	updating environment: 1 added, 2 changed, 1 removed
	reading sources... [100%] index
	/home/eduardo/git/mypublicip/docs/source/index.rst:4: WARNING: Title underline too short.

	Welcome to mypublicip's documentation!
	===============================
	/home/eduardo/git/mypublicip/docs/source/index.rst:8: WARNING: toctree contains reference to nonexisting document u'install'
	/home/eduardo/git/mypublicip/docs/source/index.rst:8: WARNING: toctree contains reference to nonexisting document u'guide'
	looking for now-outdated files... none found
	pickling environment... done
	checking consistency... done
	preparing documents... done
	writing output... [100%] index
	generating indices... genindex
	writing additional pages... search
	copying static files... WARNING: html_static_path entry u'/home/eduardo/git/mypublicip/docs/source/_static' does not exist
	done
	copying extra files... done
	dumping search index in English (code: en) ... done
	dumping object inventory... done
	build succeeded, 4 warnings.

	Build finished. The HTML pages are in build/html.
	make[1]: Leaving directory '/home/eduardo/git/mypublicip/docs'
	make -C docs/ man
	make[1]: Entering directory '/home/eduardo/git/mypublicip/docs'
	sphinx-build -b man -d build/doctrees   source build/man
	Running Sphinx v1.4.8
	loading pickled environment... done
	building [mo]: targets for 0 po files that are out of date
	building [man]: all manpages
	updating environment: 0 added, 1 changed, 0 removed
	reading sources... [100%] index
	/home/eduardo/git/mypublicip/docs/source/index.rst:4: WARNING: Title underline too short.

	Welcome to mypublicip's documentation!
	===============================
	/home/eduardo/git/mypublicip/docs/source/index.rst:8: WARNING: toctree contains reference to nonexisting document u'install'
	/home/eduardo/git/mypublicip/docs/source/index.rst:8: WARNING: toctree contains reference to nonexisting document u'guide'
	looking for now-outdated files... none found
	pickling environment... done
	checking consistency... done
	writing... mypublicip.1 { development build }
	build succeeded, 3 warnings.

	Build finished. The manual pages are in build/man.
	make[1]: Leaving directory '/home/eduardo/git/mypublicip/docs'
	cp docs/build/man/mypublicip.1 mypublicip.1
	sed \
		-e 's/@RPM_VERSION@/0.0.1/g' \
		-e 's/@RPM_RELEASE@/1/g' \
		< mypublicip.spec.in \
		> /home/eduardo/git/mypublicip/rpmbuild/SPECS/mypublicip.spec
	git ls-files | tar --transform='s|^|mypublicip/|' \
	--files-from /proc/self/fd/0 \
	-czf /home/eduardo/git/mypublicip/rpmbuild/SOURCES/mypublicip-0.0.1.tar.gz /home/eduardo/git/mypublicip/rpmbuild/SPECS/mypublicip.spec
	tar: Removing leading `/' from member names
	rpmbuild --define="_topdir /home/eduardo/git/mypublicip/rpmbuild" --define "_specdir /home/eduardo/git/mypublicip/rpmbuild/SPECS" \
	-ts /home/eduardo/git/mypublicip/rpmbuild/SOURCES/mypublicip-0.0.1.tar.gz
	Wrote: /home/eduardo/git/mypublicip/rpmbuild/SRPMS/mypublicip-0.0.1-1.src.rpm
	rpmbuild --define="_topdir /home/eduardo/git/mypublicip/rpmbuild" --rebuild /home/eduardo/git/mypublicip/rpmbuild/SRPMS/mypublicip-0.0.1-1.src.rpm
	Installing /home/eduardo/git/mypublicip/rpmbuild/SRPMS/mypublicip-0.0.1-1.src.rpm
	Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.D7DQcZ
	+ umask 022
	+ cd /home/eduardo/git/mypublicip/rpmbuild/BUILD
	+ cd /home/eduardo/git/mypublicip/rpmbuild/BUILD
	+ rm -rf mypublicip
	+ /usr/bin/gzip -dc /home/eduardo/git/mypublicip/rpmbuild/SOURCES/mypublicip-0.0.1.tar.gz
	+ /usr/bin/tar -xof -
	+ STATUS=0
	+ '[' 0 -ne 0 ']'
	+ cd mypublicip
	+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
	+ exit 0
	Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.zEczn9
	+ umask 022
	+ cd /home/eduardo/git/mypublicip/rpmbuild/BUILD
	+ cd mypublicip
	+ /usr/bin/python setup.py build
	running build
	running build_py
	creating build
	creating build/lib
	creating build/lib/mypublicip
	copying mypublicip/__init__.py -> build/lib/mypublicip
	copying mypublicip/action.py -> build/lib/mypublicip
	creating build/lib/mypublicip/util
	copying mypublicip/util/__init__.py -> build/lib/mypublicip/util
	copying mypublicip/util/decorators.py -> build/lib/mypublicip/util
	copying mypublicip/util/logger.py -> build/lib/mypublicip/util
	creating build/lib/mypublicip/notifier
	copying mypublicip/notifier/__init__.py -> build/lib/mypublicip/notifier
	creating build/lib/mypublicip/notifier/smtp
	copying mypublicip/notifier/smtp/__init__.py -> build/lib/mypublicip/notifier/smtp
	running egg_info
	creating mypublicip.egg-info
	writing requirements to mypublicip.egg-info/requires.txt
	writing mypublicip.egg-info/PKG-INFO
	writing top-level names to mypublicip.egg-info/top_level.txt
	writing dependency_links to mypublicip.egg-info/dependency_links.txt
	writing entry points to mypublicip.egg-info/entry_points.txt
	writing manifest file 'mypublicip.egg-info/SOURCES.txt'
	reading manifest file 'mypublicip.egg-info/SOURCES.txt'
	reading manifest template 'MANIFEST.in'
	warning: no files found matching 'docs/build/man/mypublicip.1'
	warning: no previously-included files matching '*' found under directory 'tests'
	warning: no previously-included files matching '__pycache__' found under directory '*'
	warning: no previously-included files matching '*.orig' found under directory '*'
	warning: no previously-included files matching '*' found under directory 'docs'
	warning: no previously-included files matching '.pyc' found anywhere in distribution
	warning: no previously-included files matching '.pyo' found anywhere in distribution
	writing manifest file 'mypublicip.egg-info/SOURCES.txt'
	+ exit 0
	Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.rIOyjl
	+ umask 022
	+ cd /home/eduardo/git/mypublicip/rpmbuild/BUILD
	+ '[' /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64 '!=' / ']'
	+ rm -rf /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64
	++ dirname /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64
	+ mkdir -p /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT
	+ mkdir /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64
	+ cd mypublicip
	+ /usr/bin/python setup.py install -O1 --skip-build --root /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64
	running install
	running install_lib
	creating /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr
	creating /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib
	creating /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7
	creating /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages
	creating /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip
	creating /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/util
	copying build/lib/mypublicip/util/__init__.py -> /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/util
	copying build/lib/mypublicip/util/decorators.py -> /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/util
	copying build/lib/mypublicip/util/logger.py -> /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/util
	copying build/lib/mypublicip/__init__.py -> /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip
	copying build/lib/mypublicip/action.py -> /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip
	creating /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/notifier
	copying build/lib/mypublicip/notifier/__init__.py -> /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/notifier
	creating /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/notifier/smtp
	copying build/lib/mypublicip/notifier/smtp/__init__.py -> /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/notifier/smtp
	byte-compiling /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/util/__init__.py to __init__.pyc
	byte-compiling /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/util/decorators.py to decorators.pyc
	byte-compiling /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/util/logger.py to logger.pyc
	byte-compiling /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/__init__.py to __init__.pyc
	byte-compiling /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/action.py to action.pyc
	byte-compiling /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/notifier/__init__.py to __init__.pyc
	byte-compiling /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip/notifier/smtp/__init__.py to __init__.pyc
	writing byte-compilation script '/tmp/tmpn3tx9P.py'
	/usr/bin/python -O /tmp/tmpn3tx9P.py
	removing /tmp/tmpn3tx9P.py
	running install_egg_info
	running egg_info
	writing requirements to mypublicip.egg-info/requires.txt
	writing mypublicip.egg-info/PKG-INFO
	writing top-level names to mypublicip.egg-info/top_level.txt
	writing dependency_links to mypublicip.egg-info/dependency_links.txt
	writing entry points to mypublicip.egg-info/entry_points.txt
	reading manifest file 'mypublicip.egg-info/SOURCES.txt'
	reading manifest template 'MANIFEST.in'
	warning: no files found matching 'docs/build/man/mypublicip.1'
	warning: no previously-included files matching '*' found under directory 'tests'
	warning: no previously-included files matching '__pycache__' found under directory '*'
	warning: no previously-included files matching '*.orig' found under directory '*'
	warning: no previously-included files matching '*' found under directory 'docs'
	warning: no previously-included files matching '.pyc' found anywhere in distribution
	warning: no previously-included files matching '.pyo' found anywhere in distribution
	writing manifest file 'mypublicip.egg-info/SOURCES.txt'
	Copying mypublicip.egg-info to /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7/site-packages/mypublicip-0-py2.7.egg-info
	running install_scripts
	Installing mypublicip script to /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/bin
	+ mkdir -p /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64//usr/share/man/man1
	+ cp mypublicip.1 /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64//usr/share/man/man1/mypublicip.1
	+ /usr/lib/rpm/check-buildroot
	+ /usr/lib/rpm/brp-compress
	+ /usr/lib/rpm/brp-strip /usr/bin/strip
	+ /usr/lib/rpm/brp-strip-comment-note /usr/bin/strip /usr/bin/objdump
	+ /usr/lib/rpm/brp-strip-static-archive /usr/bin/strip
	+ /usr/lib/rpm/brp-python-bytecompile /usr/bin/python 1
	Bytecompiling .py files below /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/lib/python2.7 using /usr/bin/python2.7
	+ /usr/lib/rpm/brp-python-hardlink
	+ /usr/lib/rpm/redhat/brp-java-repack-jars
	Processing files: mypublicip-0.0.1-1.x86_64
	Executing(%doc): /bin/sh -e /var/tmp/rpm-tmp.g5HLOz
	+ umask 022
	+ cd /home/eduardo/git/mypublicip/rpmbuild/BUILD
	+ cd mypublicip
	+ DOCDIR=/home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/share/doc/mypublicip
	+ export DOCDIR
	+ /usr/bin/mkdir -p /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/share/doc/mypublicip
	+ cp -pr README.md /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/share/doc/mypublicip
	+ cp -pr AUTHORS /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64/usr/share/doc/mypublicip
	+ exit 0
	Provides: mypublicip = 0.0.1-1 mypublicip(x86-64) = 0.0.1-1
	Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PartialHardlinkSets) <= 4.0.4-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
	Requires: /usr/bin/python python(abi) = 2.7
	Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64
	Wrote: /home/eduardo/git/mypublicip/rpmbuild/RPMS/x86_64/mypublicip-0.0.1-1.x86_64.rpm
	Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.RZCnOO
	+ umask 022
	+ cd /home/eduardo/git/mypublicip/rpmbuild/BUILD
	+ cd mypublicip
	+ /usr/bin/rm -rf /home/eduardo/git/mypublicip/rpmbuild/BUILDROOT/mypublicip-0.0.1-1.x86_64
	+ exit 0
	Executing(--clean): /bin/sh -e /var/tmp/rpm-tmp.nUzwO3
	+ umask 022
	+ cd /home/eduardo/git/mypublicip/rpmbuild/BUILD
	+ rm -rf mypublicip
	+ exit 0


Copr
-----

 .. NOTE:: Before doing any release, make sure that you have account on both sites and also make sure that you could
  access to your fedorapeople space [#]_ and have enough permissions [#]_ to build `mypublicip` in `Copr`.

	$ make srpm

   1. copy rpmbuild/SRPMS/mypublicip-0.0.1-1.src.rpm to mypublicip/copr
   2. push mypulibip/copr to github

  `copr-cli` will be used, installed by `sudo yum/dnf install copr-cli` and configure it. [#]_

Request as `Builder` for projects `mypublicip`, wait until admin approves.

$ copr-cli build mypublicip https://github.com/eduardocerqueira/mypublicip/raw/master/copr/mypublicip-0.0.1-1.src.rpm

Go and grab a cup of tea or coffee, the release build will be come out soon ::

    # tag based builds: `https://copr.fedorainfracloud.org/coprs/eduardocerqueira/mypublicip/builds/`


.. [#] https://fedorahosted.org/copr/wiki/HowToEnableRepo
.. [#] http://fedoraproject.org/wiki/Infrastructure/fedorapeople.org#Accessing_Your_fedorapeople.org_Space
.. [#] https://fedorahosted.org/copr/wiki/UserDocs#CanIgiveaccesstomyrepotomyteammate
.. [#] https://copr.fedoraproject.org/api/
