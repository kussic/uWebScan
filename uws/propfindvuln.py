import sys
from urllib2 import *
import getopt
import httplib

ABOUT = "PROPFIND (WebDAV) Vulnerability"
SAFE = "SAFE"

def vuln( h, s, p, v ):

        if s == "https":

                h = httplib.HTTPS(h,int(p))
                h.putrequest('PROPFIND', '/')
                h.putheader('Content-Length', '0')
                h.endheaders()
                h.getreply()
                f = h.getfile()
		r1 = str(f.read())
		if r1.find("<?xml",0,5) == 0:
			return r1 + "\n"
		else:
			return "Not Vulnerable to PROPFIND." + "\n" 
        else:
                h = httplib.HTTP(h,int(p))
                h.putrequest('PROPFIND', '/')
                h.putheader('Content-Length', '0')
                h.endheaders()
                errcode, errmsg, headers = h.getreply()
                f = h.getfile()
		r1 = str(f.read())
		if r1.find("<?xml",0,5) == 0:
			return r1 + "\n"
		else:
			return "Not Vulnerable to PROPFIND."  + "\n" 

