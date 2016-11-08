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

from action import Action
from mypublicip.util import get_args
from mypublicip.util.logger import get_logger


def main():
    try:
        args = get_args()
        log = get_logger(__name__, args.verbose)
        action = Action(args)

        if args.show:
            action.show()

        if args.compare:
            action.compare()

        action.notify()
    except Exception as ex:
        log.error(ex)


if __name__ == '__main__':
    main()
