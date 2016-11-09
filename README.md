https://copr.fedorainfracloud.org/coprs/eduardocerqueira/mypublicip/package/mypublicip/status_image/last_build.png

# mypublicip

Goal: let you know whenever your public IP is renewed/changed.

Description: Tool to notify when your public IP is changed; **It is for personal usage only** please don't expect I am providing support for these codes; I have these scripts running in some of my servers and they notify me whenever my public IP is renewed.

Versions: There is a simplified version that actually was the first version and that inspired me to build the second and more complete version
that runs on CLI and installed by RPM ( for now only teste don Fedora 24 ).

simplified: https://github.com/eduardocerqueira/mypublicip/script/myip.py

complete: https://github.com/eduardocerqueira/mypublicip

Info below are describing the script for complete version:

Useful when you use a server not in a datacenter or running behind a regular ISP router without domain or static IP.

**possible use cases:**

* running in a cron job
* running as command line whenever you want to know what is your public ip
* others


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


Access Fedora Copr at: https://copr.fedorainfracloud.org/coprs/eduardocerqueira/mypublicip/builds/

running a new build:

	$ copr-cli build mypublicip https://github.com/eduardocerqueira/mypublicip/raw/master/copr/mypublicip-0.0.1-1.src.rpm


## install

**repo:** https://copr-be.cloud.fedoraproject.org/results/eduardocerqueira/mypublicip/fedora-24-x86_64/00474191-mypublicip/

	$ sudo dnf install https://copr-be.cloud.fedoraproject.org/results/eduardocerqueira/mypublicip/fedora-24-x86_64/00474191-mypublicip/mypublicip-0.0.1-1.x86_64.rpm


## Guide

1. After installed on your machine, copy file /conf/mypublicip.conf to ~/.mypublicip/mypublicip.conf and edit for correct values
the default location for this file can be override if you use the arg --conf and the full path for your file

2. files will be generated at ~/.mypublicip/
 * .ip.txt
 * history.txt

listing content:

	$ cat ~/.mypublicip/history.txt
	2016-11-07 17:05:12.896891 | 64.117.243.216
	2016-11-07 17:06:38.525302 | 63.117.215.88
	2016-11-07 17:07:44.854575 | 200.147.41.208
	2016-11-07 17:09:12.806098 | 151.101.128.73
	2016-11-07 17:09:42.944546 | 186.192.81.31
	2016-11-07 17:13:20.697272 | 185.53.177.30
	2016-11-07 21:42:26.657016 | 54.209.129.73


Below some basic commands, just to demonstrate;

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

compare ( non verbose ) after my IP has been renewed

	[eduardo@dev ~]$ mypublicip --compare
	2016-11-07 23:30:29,119 INFO [mypublicip.action.is_renewed:108] changed, it is new public IP!
	2016-11-07 23:30:29,119 INFO [mypublicip.action.save_history:122] new IP saved in /home/eduardo/.mypublicip/history.txt
	2016-11-07 23:30:31,138 INFO [mypublicip.notifier.smtp.send:56] email sent to ['eduardomcerqueira@gmail.com']



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

