from socket import *
import struct
import sys
from urllib2 import *
import getopt
import httplib
import time

TIME1970 = 2208988800L      # Thanks to F.Lundh
ABOUT = "Web Server Clock Check"
SAFE = "SAFE"

def get( h, s, p, v ):
	try:
		req = Request(s + '://' + h + ':' + p + '/')
		req.add_header('Host',v)
		f = urlopen(req)
		f.info()['date']
	except KeyError:
		return "ERR: \'Date\' Header doesn't exist." 
	except HTTPError:
		r=0


	r = "1st Run:\n"
	try:
		req = Request(s + '://' + h + ':' + p + '/')
		req.add_header('Host', v)
		f = urlopen(req)
		
		
		r = r + "Server Time: " + str(f.info()['date'])
		client = socket.socket( AF_INET, SOCK_DGRAM )
		data = '\x1b' + 47 * '\0'
		client.sendto( data, ( "time.apple.com", 123 ))
		data, address = client.recvfrom( 1024 )
		if data:
			t = struct.unpack( '!12I', data )[10]
			t -= TIME1970
			snmptime = "\nSNTP Time  : %s" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(t)) + " " + time.tzname[0]
		r = r + "\nLocal Time : " + time.strftime("%a, %d %b %Y %H:%M:%S %Z")
		r = r + snmptime

	except HTTPError, e:
		r = r + "Server Time: " + str(e.info()['date'])
		client = socket.socket( AF_INET, SOCK_DGRAM )
        data = '\x1b' + 47 * '\0'
        client.sendto( data, ( "time.apple.com", 123 ))
        data, address = client.recvfrom( 1024 )
        if data:
        	t = struct.unpack( '!12I', data )[10]
        	t -= TIME1970
        	snmptime = "\nSNTP Time  : %s" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(t)) + " " + time.tzname[0]

        r = r + "\nLocal Time : " + time.strftime("%a, %d %b %Y %H:%M:%S %Z")
        r = r + snmptime
    


	r = r + "\n\n2nd Run:\n"
	try:
		req = Request(s + '://' + h + ':' + p + '/')
		req.add_header('Host', v)
		f = urlopen(req)
		
		
		r = r + "Server Time: " + str(f.info()['date'])
		client = socket.socket( AF_INET, SOCK_DGRAM )
		data = '\x1b' + 47 * '\0'
		client.sendto( data, ( "time.apple.com", 123 ))
		data, address = client.recvfrom( 1024 )
		if data:
			t = struct.unpack( '!12I', data )[10]
			t -= TIME1970
			snmptime = "\nSNTP Time  : %s" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(t)) + " " + time.tzname[0]
		r = r + "\nLocal Time : " + time.strftime("%a, %d %b %Y %H:%M:%S %Z")
		r = r + snmptime

	except HTTPError, e:
		r = r + "Server Time: " + str(e.info()['date'])
		client = socket.socket( AF_INET, SOCK_DGRAM )
        data = '\x1b' + 47 * '\0'
        client.sendto( data, ( "time.apple.com", 123 ))
        data, address = client.recvfrom( 1024 )
        if data:
        	t = struct.unpack( '!12I', data )[10]
        	t -= TIME1970
        	snmptime = "\nSNTP Time  : %s" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(t)) + " " + time.tzname[0]

        r = r + "\nLocal Time : " + time.strftime("%a, %d %b %Y %H:%M:%S %Z") 
        r = r + snmptime

	return r + "\n"

