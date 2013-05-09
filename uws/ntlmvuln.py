import sys
from urllib2 import *
import getopt
import httplib
import base64
import hexdump

ABOUT = "NTLM Authentication Vulnerability"
SAFE = "SAFE"

def vuln( h, s, p, v ):

                r = ""

                req = Request(s + '://' + h + ':' + p + '/')
                req.add_header('Host', v)
                req.add_header('Authorization', 'NTLM TlRMTVNTUAABAAAAB4IAoAAAAAAAAAAAAAAAAAAAAAA=')
                try:
                        f = urlopen(req)
                except HTTPError, e:
                        if str(e.code) == "401":
                                authtype = str(e.info()['WWW-Authenticate']).split()[0]
                                if authtype == "Negotiate":
                                        r = r + "\nBase64:\n" + str(e.info()['WWW-Authenticate']).split()[1]
                                        r = r + "\nDecode:\n" + hexdump.dump(base64.b64decode(str(e.info()['WWW-Authenticate'].split()[1])))
                                elif authtype == "NTLM":
                                        r = r + "\nBase64:\n" + str(e.info()['WWW-Authenticate']).split()[1]
                                        r = r + "\nDecode:\n" + hexdump.dump(base64.b64decode(str(e.info()['WWW-Authenticate'].split()[1])))
                                else:
                                        r = r + "Host is not vulnerable (" + str(e.info()['WWW-Authenticate']) +")"
                        else:
                                r = r + "No Issues"
                else:
                        r = r + "No Issues"

                return r + "\n"

