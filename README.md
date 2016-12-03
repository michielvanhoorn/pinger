# pinger
Python ping script posting result to Thingspeak

This python script execute a single ping against a destination and post it to a Thingspeak channel.

The code is inspired on FlipperPA / Latency-tester: https://github.com/FlipperPA/latency-tester

Requirements:
pexpect: http://pexpect.readthedocs.io/en/stable/ Install using sudo pip install pexpect

thingspeak: https://pypi.python.org/pypi/thingspeak/ Install using sudo pip install thingspeak

The code executes only once running 1 ICMP ping and posting it. To run the script at an interval add it to crontab.

To run every 10 minutes add the below:
*/10 * * * * python /home/pi/pinger/pinger.py
