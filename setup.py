#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from setuptools import setup, find_packages
from os.path import exists


def get_version():
    """Get version and release"""
    # version.txt file is copied during rpm build process from
    # rpmbuild/SOURCES/ to rpmbuild/BUILD and become root for versioning
    _version = "rpmbuild/BUILD/version.txt"
    if exists(_version):
        with open(_version, "r") as version_file:
            version = version_file.read()
            return version
    else:
        return "0"


def get_install_requires():
    requires = []
    links = []
    for line in open('requirements/production.txt', 'r'):
        line = line.strip()
        if not line.startswith('#'):
            parts = line.split('#egg=')
            if len(parts) == 2:
                links.append(line)
                requires.append(parts[1])
            else:
                requires.append(line)
    return requires, links

install_requires, dependency_links = get_install_requires()

setup(
    name='mypublicip',
    version=get_version(),
    description='notify when your public IP is renewed by your ISP',
    url='https://github.com/eduardocerqueira/mypublicip.git',
    author='Eduardo Cerqueira',
    author_email='eduardomcerqueira@gmail.com',
    platforms='Fedora >= 24',
    license='GPL',
    test_suite="nose.collector",
    tests_require="nose",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    entry_points={'console_scripts': ['mypublicip=mypublicip.__init__:main']}
)
