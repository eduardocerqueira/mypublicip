![copr build](https://copr.fedorainfracloud.org/coprs/eduardocerqueira/mypublicip/package/mypublicip/status_image/last_build.png)

# mypublicip

Goal: let you know whenever your public IP is renewed/changed.

Description: Tool to notify when your public IP is changed; **It is for personal usage only** please don't expect I am providing support for these codes; I have these scripts running in some of my servers and they notify me whenever my public IP is renewed.

Versions: There is a simplified version 0.1 just a simple python script all in a file and it worked for months in my servers, recently I decided to improve this and become the 0.2 that is more complete, runs as CLI and installed by RPM ( for now only teste don Fedora 24 ).

simplified version 0.1: https://github.com/eduardocerqueira/mypublicip/script/myip.py

version 0.2: https://github.com/eduardocerqueira/mypublicip

Info below are describing the script for version 0.2:

Useful when you use a server not in a datacenter or running behind a regular ISP router without domain or static IP.

**possible use cases:**

* You have a server not running with static IP or domain and we use this for web PROXY or for SSH Tunel or even need to access it but you dont want to be blocked when your ISP renew your IP.
* want to have a easy way to show your current public IP
* want to keep a history for your public IP changes



# For developer and contributers

This section describes how to build a new RPM for mypublicip;
I use make so it requires basic packages in your machine I recommend: python-setuptools, python-sphinx, python-devel and gcc

## RPM / Build

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

Running from your local machine, you can generate your own RPM running:

	$ make rpm

and if your environment is setup properly you should have your RPM at: /home/user/git/mypublicip/rpmbuild/RPMS/x86_64/mypublicip-0.0.1-1.x86_64.rpm

mypublicip is being built on Fedora Copr: https://copr.fedorainfracloud.org/coprs/eduardocerqueira/mypublicip/builds/

running a new build:

	$ copr-cli build mypublicip https://github.com/eduardocerqueira/mypublicip/raw/master/copr/mypublicip-0.0.1-1.src.rpm


## install

Installing from your local machine, after you build your own RPM just run:

for Fedora:
	
	$ sudo dnf install /home/user/git/mypublicip/rpmbuild/RPMS/x86_64/mypublicip-0.0.1-1.x86_64.rpm

for RHEL and CentOS:
	
	$ sudo yum install /home/user/git/mypublicip/rpmbuild/RPMS/x86_64/mypublicip-0.0.1-1.x86_64.rpm

To install from latest RPM:

**repo:** https://copr-be.cloud.fedoraproject.org/results/eduardocerqueira/mypublicip/fedora-24-x86_64/00474191-mypublicip/

	$ sudo dnf install https://copr-be.cloud.fedoraproject.org/results/eduardocerqueira/mypublicip/fedora-24-x86_64/00474191-mypublicip/mypublicip-0.0.1-1.x86_64.rpm


## User guide

1. After installed on your machine, copy file /conf/mypublicip.conf to ~/.mypublicip/mypublicip.conf and edit for correct values
the default location for this file can be override if you use the arg --conf and the full path for your file

it is a sample of this file:

	[SAVE]
	enable: true

	[EMAIL]
	subject: PUBLIC IP changed
	body: New public IP for my HOME server, same used to connect AWS VPC and GCE and Web proxy 
	from: eduardomcerqueira@gmail.com
	to: eduardomcerqueira@gmail.com

	[SMTP]
	enable: true
	name: GMAIL
	server: smtp.gmail.com
	port: 587
	username: username@gmail.com
	password: password


2. Running some commands:

Help or non args:

	[eduardo@dev ~]$ mypublicip
	usage: mypublicip [-h] [--test] [--conf] [--compare] [--show] [--verbose]

	optional arguments:
	  -h, --help  show this help message and exit
	  --test      run on test mode, do not send any notification
	  --conf      full path for your mypublicip.conf file
	  --compare   compare IP and notify if has changed/renewed
	  --show      show current public IP
	  --verbose   run on verbose mode (DEBUG) level

show ( non verbose )

	[eduardo@dev ~]$ mypublicip --show
	
	2016-11-07 23:22:24,015 INFO [mypublicip.action.show:147] my public IP: 96.252.122.123

compare ( non verbose )

	[eduardo@dev ~]$ mypublicip --compare

	2016-11-07 23:23:40,383 INFO [mypublicip.action.is_renewed:105] no change, same public IP!

compare ( non verbose ) after my IP has been renewed and email sent

	[eduardo@dev ~]$ mypublicip --compare
	
	2016-11-07 23:30:29,119 INFO [mypublicip.action.is_renewed:108] changed, it is new public IP!
	2016-11-07 23:30:29,119 INFO [mypublicip.action.save_history:122] new IP saved in /home/eduardo/.mypublicip/history.txt
	2016-11-07 23:30:31,138 INFO [mypublicip.notifier.smtp.send:56] email sent to ['eduardomcerqueira@gmail.com']

sample of an email received after my public IP was renewed:

![Preview](https://github.com/eduardocerqueira/mypublicip/raw/master/docs/source/_static/email_example.png)


3. These files will be created at your /home/user/.mypublicip

 * .ip.txt	: save your current public ip
 * history.txt	: keep the history, saving all public IP you already had.

listing history file:

        $ cat ~/.mypublicip/history.txt

        2016-11-07 17:05:12.896891 | 64.117.243.216
        2016-11-07 17:06:38.525302 | 63.117.215.88
        2016-11-07 17:07:44.854575 | 200.147.41.208
        2016-11-07 17:09:12.806098 | 151.101.128.73
        2016-11-07 17:09:42.944546 | 186.192.81.31
        2016-11-07 17:13:20.697272 | 185.53.177.30
        2016-11-07 21:42:26.657016 | 54.209.129.73
 

4. cron job

you can add mypublicip in a cron to be notified anytime your public IP is change.

	$ crontab -e
	0 */1 * * * mypublicip --compare

for troubleshooting:

	[eduardo@server .mypublicip]$ sudo cat /var/log/cron |grep mypublicip
	Nov  9 21:12:01 localhost CROND[5896]: (eduardo) CMD (mypublicip --compare)


## MORE INFO

For others topics listed below, please generate the sphinx doc in your local machine running the command:

	$ make doc

and from a browser access: file:///home/user/git/mypublicip/docs/build/html/index.html

* Install:
* Guide:
* Build:
* Development:


## Notifier

 * Email: use your email provider as SMTP;

Features to research:

 * own/cloud SMTP
 * SMS
 * IRC
 * https://www.notifymyandroid.com/
 * https://www.digitalocean.com/community/tutorials/how-to-create-a-server-to-send-push-notifications-with-gcm-to-android-devices-using-python
 * https://developers.google.com/cloud-messaging/

 ## How to contribute

 Feel free to fork and send me pacthes or messages if you think this tool can be helpful for any other scenario.

