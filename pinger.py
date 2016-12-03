import sys, pexpect, time, datetime
from time import localtime, strftime
import time
import thingspeak

# Channel information
channel_id = "Thingspeak channel id here"
write_key  = "thingspeak write key here"
channel = thingspeak.Channel(id=channel_id,write_key=write_key)

# WHO SHOULD WE RUN THE PING TEST AGAINST
ping_destination = 'www.google.com'

count = 0

ping_command = 'ping -c 2 ' + ping_destination

child = pexpect.spawn(ping_command)
child.timeout=1200



while 1:

    line = child.readline()

    if not line:
        break
    if line.startswith(b'ping: unknown host'):
        
        break

    if count > 0:

        ping_time = float(line[line.find(b'time=') + 5:line.find(b' ms')])
        line = str(ping_time)
        print(line)

        response = channel.update({1:line})

        break

    count += 1
