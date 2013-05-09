import sys
import getopt
import httplib

ABOUT = "Internal IP Vulnerability"
DIR = ("/", "/images")
SAFE = "SAFE"

def vuln( h, s, p, v ):
	host = h
	port = p
	ssl = s
	out = ""
	for d in DIR:
		if ssl == "https":
			h = httplib.HTTPS(host,int(port))
		else:
			h = httplib.HTTP(host,int(port))
		h.putrequest('GET', d)
		h.endheaders()
		ec, em, hd = h.getreply()
		try:
			out = out + " * " + d + " = " + hd['location'] + "\n"
		except:
			try:
				out = out + " * " + d + " = " + hd['content-location'] + "\n"
			except:
				out = out + " * " + d + " = " + "Not vulnerable." + "\n"
	
	return out

