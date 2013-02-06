cert_checker.py
===============
Simple script to check when ssl certs expire. Put into your logging system to alert when your certs, or certs you rely on, are about to expire.

People forget, calendar reminders get lost. Don't be that guy.

## Example
```
$ python cert_checker.py www.google.com 443
2013-02-05 22:41:38|server='www.google.com:443'|ssl_expires='Jun  7 19:43:27 2013 GMT'
```

## Requires
* M2Crypto

## Todo
* tests
* more/dynamic attributes about certs?, though KISS.
