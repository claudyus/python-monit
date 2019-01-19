# python-monit

[![Build Status](https://travis-ci.com/claudyus/python-monit.svg?branch=master)](https://travis-ci.com/claudyus/python-monit)

Python code to talk to Monit, the system manager and monitor (http://mmonit.com/monit/)

This library just comunicates with the built-in HTTP daemon. Make sure it's enabled.

Usage example:
```
>>> mon = Monit(username='admin', password='monit')
>>> # mon is a dict:
>>> mon['openvpn'].monitored
True
>>> mon['openvpn'].running
True
>>>mon['platform']
<Platform {'name': 'Linux', 'machine': 'armv5tejl', 'version': '#1 PREEMPT Wed Nov 14 11:44:56 CST 2018', 'swap': '0', 'memory': '253872', 'release': '3.12.70', 'cpu': '1'}>
```
