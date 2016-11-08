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

from mypublicip.notifier.smtp import Email


class Notifier(object):
    """
    the hub for all notifications methods available

    @attention: on this current version only EMAIL is available but the
    code is ready be expanded for others, maybe further
    """

    def __init__(self, args, my_conf, ip):
        """Constructor"""
        self.args = args
        self.my_conf = my_conf
        self.ip = ip

        self.email = Email(self.my_conf, self.ip)
