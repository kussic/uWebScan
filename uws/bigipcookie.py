import sys
from urllib2 import *
import getopt
import httplib
import struct

ABOUT = "F5 BIGIP Cookie IP Exposure"
SAFE = "SAFE"
def get( h, s, p, v ):
        try:
                req = Request(s + '://' + h + ':' + p + '/')
                req.add_header('Host', v)
                f = urlopen(req)
                cookies = f.info().getheader("Set-Cookie")
                bigipCookie = cookies.split("BIGipServer")[1].split("expires")[0].split("=")
                (host, port, end) = bigipCookie[1].split('.')

                (a, b, c, d) = [ord(i) for i in struct.pack("<I", int(host))]
                (v) = [ord(j) for j in struct.pack("<H", int(port))]
                p = "0x%02X%02X" % (v[0],v[1])

                return "BigIP Cookie name: %s \nBigIP Cookie Value: %s\nDecoded IP [port]: %s.%s.%s.%s [%s]\n" % (bigipCookie[0],bigipCookie[1],a,b,c,d,int(p,16))
 
        except:
                return "No BIP IP Cookie here..."

