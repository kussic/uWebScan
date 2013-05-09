import sys
from urllib2 import *
import getopt
import httplib

ABOUT = "HTTP TRACE Vulnerability"
SAFE = "SAFE"

def vuln( h, s, p, v ):

        if s == "https":

                h = httplib.HTTPS(h,int(p))
                h.putrequest('TRACE', '/unknown<script>alert("XSS")</script>.html')
                #h.putheader('X-Test', 'testing')
                h.endheaders()
                h.getreply()
                f = h.getfile()
                r1 = str(f.read())
                if "unknown<script>alert(\"XSS\")</script>" in r1:
                        out = "Vulnerable to TRACE Cross-Site Scripting.\n\n-OUTPUT:\n" + r1
                else:
                        out = "Not vulnerable to TRACE Cross-Site Scripting.\n"
                return out
        else:
                h = httplib.HTTP(h,int(p))
                h.putrequest('TRACE', '/unknown<script>alert("XSS")</script>.html')
                #h.putheader('X-Test', 'testing')
                h.endheaders()
                h.getreply()
                f = h.getfile()
                r1 = str(f.read())
                if "unknown<script>alert(\"XSS\")</script>" in r1:
                        out = "Vulnerable to TRACE Cross-Site Scripting.\n\n-OUTPUT:\n" + r1
                else:
                        out = "Not vulnerable to TRACE Cross-Site Scripting.\n"
                return out

