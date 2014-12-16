#!/usr/bin/env python

import requests, sys, syslog, json

script, user, passwd, caller = sys.argv
passwd = passwd.lstrip("'").rstrip("'")

api_server = "https://api-staging.packet.net:6443/sessions"
payload = { "login": user, "password": passwd }

msg = 'fradiusauth.py: Authentication attempt by user: ' + user + '\n'
syslog.syslog(msg)

headers = {'Content-type': 'application/json', "X-Consumer-Token": "365753ceb7b4f472c86da34205e3e12c3a595a9981720b5fac52baf17069ea9e"}

resp = requests.post(api_server, data=json.dumps(payload), headers=headers)

if int(resp.status_code) == 201:
	msg = 'fradiusauth.py: Authentication for %s successful.' % user
	syslog.syslog(msg)
    print "Accept"
    sys.exit(0)

msg = 'fradiusauth.py: Authentication failed for %s with API status code %s.' % (user, str(resp.status_code))
syslog.syslog(msg)
print "Reject"
sys.exit(1)

