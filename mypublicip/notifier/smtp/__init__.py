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

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from mypublicip.util.logger import get_logger

log = get_logger(__name__)


class Email(object):
    """
    Send email based on mypublicip.conf properties
    """

    def __init__(self, my_conf, ip):
        """Constructor"""
        self.my_conf = my_conf
        self.ip = ip

    def send(self):
        """
        Send email based sections SMTP and EMAIL from configuration file
        """
        fromaddr = self.my_conf.get('EMAIL', 'from')
        mail_to = []
        for email in self.my_conf.get('EMAIL', 'to').split(","):
            mail_to.append(email)

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = str(mail_to)
        msg['Subject'] = self.my_conf.get('EMAIL', 'subject')

        body = "%s \n %s" % (self.my_conf.get('EMAIL', 'body'), self.ip)
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(self.my_conf.get('SMTP', 'server'), self.my_conf.get('SMTP', 'port'))
        server.starttls()
        server.login(self.my_conf.get('SMTP', 'username'), self.my_conf.get('SMTP', 'password'))
        text = msg.as_string()
        server.sendmail(fromaddr, mail_to, text)
        log.info("email sent to %s", mail_to)
        server.quit()
        return True
