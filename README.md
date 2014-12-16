fradiusauth
===========

Authentication scripts for FreeRADIUS using the Packet API

Setup and testing
=================

Copy files into appropriate places
----------------------------------

0. ```cp fradiusauth.py /usr/local/bin```
1. ```chmod 0755 /usr/local/bin/fradiusauth.py```
2. ```cp users /etc/freeradius```
3. ```cp clients.conf /etc/freeradius```
4. ```service freeradius restart```

Testing
-------

0. ```git clone https://github.com/chasemp/py-radius.git```
1. ```cd py-radius; python setup.py install```
2. ```cd fradiusauth; python libradclient.py <RADIUS host> <RADIUS secret> <username> <password>```

TODO
====

1. Need better error handling for scenarios where the API server isn't available, isn't responding, etc...
2. Need to handle 2-factor authentication.
