#!/usr/bin/env python

import requests, sys, syslog, json, re

script, user, token, caller = sys.argv

# Split the token into the OTP and password
token = token.lstrip("'").rstrip("'")
pattern = re.compile('(\d{6,6})(.*)')

# Now, search for the OTP and password
match = pattern.search(token)
if match:
    otp = match.group(1)
    passwd = match.group(2)

    api_server = "https://api/auth"
    payload = { "login": user, "password": passwd }

    msg = 'Authentication attempt by user: ' + user + '\n'
    syslog.syslog(msg)

    headers = {'Content-type': 'application/json', "X-Consumer-Token": "365753ceb7b4f472c86da34205e3e12c3a595a9981720b5fac52baf17069ea9e", "X-OTP-Token": otp}

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

# token/password pattern failed, so reject the attempt
msg = 'fradiusauth.py: Authentication failed for %s due to a bad password or token' % user
syslog.syslog(msg)
print "Reject"
sys.exit(1)
