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

import argparse
from os import getenv
import sys

def get_args():
    """
    Get user args if exist;

    Arguments:

    --test: to run on test mode, do not send any notification out
    --conf: override the default path for mypublicip.conf
    --compare: compare IP and notify if has changed/renewed
    --show: show current public IP

    """
    parser = argparse.ArgumentParser(prog='mypublicip')
    parser.add_argument("--test",
                        help="run on test mode, do not \
                        send any notification",
                        default=False,
                        action="store_true")
    parser.add_argument("--conf",
                        help="full path for your mypublicip.conf file",
                        default=False,
                        action="store_true")
    parser.add_argument("--compare",
                        help="compare IP and notify if has \
                        changed/renewed",
                        default=False,
                        action="store_true")
    parser.add_argument("--show",
                        help="show current public IP",
                        default=False,
                        action="store_true")
    parser.add_argument("--verbose",
                        help="run on verbose mode (DEBUG) level",
                        default=False,
                        action="store_true")

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(1)

    return args


class Constants(object):
    MYPUBLICIP_HOME = "%s/%s" % (getenv("HOME"), ".mypublicip")
    HISTORY = "%s/%s" % (MYPUBLICIP_HOME, "history.txt")
    IP = "%s/%s" % (MYPUBLICIP_HOME, ".ip.txt")
    CONF_FILE = "mypublicip.conf"
