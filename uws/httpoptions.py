import sys
from urllib2 import *
import getopt
import httplib

ABOUT = "HTTP OPTIONS Available"
SAFE = "SAFE"
def get( host, ssl, port, vhost ):

	h = host
	s = ssl
	p = port
	r = ""
	try:
		if s == "https":
			h = httplib.HTTPS(h,int(p))
			h.putrequest('OPTIONS', '/')
			h.endheaders()
			ec, em, hd = h.getreply()
			r = r + "Allowed: " + hd['allow'] + "\n"
		else:
			h = httplib.HTTP(h,int(p))
			h.putrequest('OPTIONS', '/')
			h.endheaders()
			ec, em, hd = h.getreply()
			r = r + "Allowed: " + hd['allow'] + "\n"
	except KeyError, e:
		if str(e) == "\'allow\'":
			r = r + "Allowed: No 'allow' header\n"

		
	h = host
	s = ssl
	p = port

	try:
		if s == "https":
			h = httplib.HTTPS(h,int(p))
			h.putrequest('OPTIONS', '/')
			h.endheaders()
			ec, em, hd = h.getreply()
			r = r + "Public: " + hd['public'] + "\n"
		else:
			h = httplib.HTTP(h,int(p))
			h.putrequest('OPTIONS', '/')
			h.endheaders()
			ec, em, hd = h.getreply()
			r = r + "Public: " + hd['public'] + "\n"
	except KeyError, e:
		if str(e) == "\'public\'":
			r = r + "Public: No 'public' header\n"

	

	return r + "\n"
