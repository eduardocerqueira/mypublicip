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

from ConfigParser import ConfigParser
from os.path import exists
import requests
from mypublicip.util.decorators import retry
from mypublicip.util import Constants
from mypublicip.util.logger import get_logger
from datetime import datetime
from notifier import Notifier


class Action(object):
    """
    Hosting methods used by mypublicip to perform some action related
    public ip
    """

    def __init__(self, args):
        """Constructor"""
        self.args = args
        self.ip = None
        self.notified = False
        self.renewed = False
        self.my_conf = None
        self.ip_file = Constants.IP
        self.history_file = Constants.HISTORY
        self.log = get_logger(__name__, args.verbose)
        # get mypublicip.conf
        self.load_my_conf()
        # running on TEST mode
        self.is_test()

    def is_test(self):
        """
        print header if running on test mode
        """
        if self.args.test:
            self.log.info("-" * 50)
            self.log.info("TEST ONLY, notifications disabled")
            self.log.info("-" * 50)

    def load_my_conf(self):
        """
        Load mypublicip.conf and return all sections
        """
        my_conf_file = None
        if self.my_conf:
            my_conf_file = self.my_conf
        else:
            my_conf_file = "%s/%s" % (Constants.MYPUBLICIP_HOME, Constants.CONF_FILE)

        if not exists(my_conf_file):
            raise IOError("%s not found" % my_conf_file)

        self.log.debug("loading %s", my_conf_file)
        my_conf = ConfigParser()
        my_conf.read(my_conf_file)
        self.my_conf = my_conf

    @retry(Exception, tries=3, delay=10)
    def get_myip(self):
        """
        HTTP Get request to ipecho.net/plain to get my Public IP
        retries 3x if not able to get IP
        """
        if self.ip:
            return self.ip

        url = "http://ipecho.net/plain"
        self.log.debug("getting your public IP from %s", url)
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        self.ip = r.content
        return r.content

    def is_renewed(self):
        """
        Get previous IP from temporally .ip.txt file if exist and compare with
        new IP returning the result of this operation as boolean
        """
        if not exists(self.ip_file):
            self.log.debug("file %s doesn't exist", self.ip_file)
            with open(self.ip_file, "w") as temp_file:
                temp_file.write(self.ip)
                self.log.debug("file %s created", self.ip_file)
            return False

        with open(self.ip_file, "r") as ip_file:
            prev_ip = ip_file.read()
        if self.ip in prev_ip:
            self.log.info("no change, same public IP!")
            return False
        else:
            self.log.info("changed, it is new public IP!")
            self.renewed = True
            # update .ipt.txt with latest IP
            with open(self.ip_file, "w") as temp_file:
                temp_file.write(self.ip + "\n")
            return True

    def save_history(self):
        """
        Persist new IP into history file
        """
        data = "%s | %s\n" % (str(datetime.now()), self.ip)
        with open(self.history_file, "a") as history:
            history.write(data)
            self.log.info("new IP saved in %s", self.history_file)

    def notify(self):
        """
        Send the notifications out
        """
        notifier = Notifier(self.args, self.my_conf, self.ip)

        if self.args.test:
            self.log.debug("running on TEST mode, skip notifications")
            return True

        if self.renewed is False:
            self.log.debug("skipping notification")
            return True

        # email notification
        if "true" in self.my_conf.get('SMTP', 'enable') and self.notified is False:
            self.notified = notifier.email.send()

    def show(self):
        """
        Show public IP at console output
        """
        my_public_ip = self.get_myip()
        self.log.info("my public IP: %s", my_public_ip)

    def compare(self):
        """
        Compare previous IP from .ip.txt with current IP and
        save history if they are diff and history is enabled in
        mypublicip.conf
        """
        self.get_myip()
        if self.is_renewed():
            if self.my_conf.get('SAVE', 'enable'):
                self.save_history()
