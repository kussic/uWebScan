import sys
from urllib2 import *
import getopt
import httplib
import re

ABOUT = "Robots.txt \"Disallow\" Disclosure"
SAFE = "SAFE"

def vuln( h, s, p, v ):
        host = h
        port = p
        ssl = s
        vhost = v
        out = ""
        FOUND = ""
        REDIR = ""
        NOTFOUND = ""
        OTHER = ""

        
        if ssl == "https":
                h = httplib.HTTPS(host,int(port))
        else:
                h = httplib.HTTP(host,int(port))

        h.putrequest('GET', "/robots.txt")
        h.putheader('host', vhost)
        h.endheaders()
        ec, em, hd = h.getreply()
        f = h.getfile()
        ahtlm = ""
        ahtml = f.read().lower()

        if ec != 404:
                s = ahtml.split("\n")
                for a in s:
                        if "disallow:" in a:
                                if ssl == "https":
                                        h = httplib.HTTPS(host, int(port))
                                else:
                                        h = httplib.HTTP(host, int(port))

                                h.putrequest('GET', a.strip("disallow:"))
                                h.putheader('host', vhost)
                                h.endheaders()
                                ec, em, hd = h.getreply()
                                f = h.getfile().read()
                                sitevar = a.split(": ")
                                if ec == 200: 
                                        FOUND = FOUND + sitevar[1] + "\n"
                                elif ec == 302:
                                        REDIR = REDIR + sitevar[1] + "\n"
                                elif ec == 404:
                                        NOTFOUND = NOTFOUND + sitevar[1] + "\n"
                                else:
                                        OTHER = OTHER + "(" + str(ec) + " " + em + ") " + sitevar[1] + "\n"
                out = "Found Directories:\n\n" + FOUND + "\nRedirects:\n\n" + REDIR + "\nNot Found:\n\n" + NOTFOUND + "\nOther results:\n\n" + OTHER 
        else:
                out = "A \"robots.txt\" file was not found: " + str(ec) + " " + em



        return out


