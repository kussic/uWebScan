import sys
from urllib2 import *
import getopt
import httplib
import re

ABOUT = "Apache HTTPD Version Detection"
SAFE = "SAFE"

def apachecurrent(ver):
	h = httplib.HTTP("httpd.apache.org",80)
        h.putrequest('GET', '/download.cgi')
	h.putheader('Host', 'httpd.apache.org')
        h.endheaders()
        ec, em, hd = h.getreply()
        f = h.getfile()
	ahtml = f.read()
	#print "\n\n - HTML - \n" + ahtml
	regexp = re.compile("<h1 id=\"apache2.\">Apache HTTP Server 2\..\...")
	result = regexp.search(ahtml).group().split("Apache HTTP Server")[1].strip()
	return result
	





def get( h, s, p, v ):
	
        r = ""
	srvver = ""
        try:
                if s == "https":
                        h = httplib.HTTPS(h,int(p))
                        h.putrequest('GET', '/')
			h.putheader('Host', v)
                        h.endheaders()
                        ec, em, hd = h.getreply()
                        srvver = hd['server']
                else:
                        h = httplib.HTTP(h,int(p))
                        h.putrequest('GET', '/')
			h.putheader('Host', v)
			h.putheader('User-Agent', "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9) Gecko/2008051202 Firefox/3.0")
                        h.endheaders()
                        ec, em, hd = h.getreply()
                        srvver = hd['server']
        except KeyError, e:
		print "ERR: " + str(e)
	if "Apache" in srvver and "2.0." in srvver:
		return "Server reports: " + srvver + "\nApache.org latest: " + apachecurrent("2.0") + "\n"
	elif "Apache" in srvver and "2.2." in srvver:
		return "Server reports: " + srvver + "\nApache.org latest: " + apachecurrent("2.2") + "\n"
	elif "Apache" in srvver and "1.3." in srvver:
		return "Server reports: " + srvver + "\nApache.org considers the 1.x branch to be dead: http://httpd.apache.org/download.cgi" + "\n"
	elif "Apache" in srvver and "2.4." in srvver:
		return "Server reports: " + srvver + "\nApache.org latest: " + apachecurrent("2.4") + "\n"
	elif "Apache" in srvver:
		return "I couldn't not detect a current version of Apache running. \nServer reports: " + srvver + "\n"
	else:
		return "Not Apache HTTPD: " + srvver + "\n"


if __name__ == "__main__":

	print get("www.apache.org", "http", "80", "www.apache.org")
