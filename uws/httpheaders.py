import sys
from urllib2 import *
import getopt
import httplib

ABOUT = "HTTP Headers Available"
SAFE = "SAFE"
def get( h, s, p, v ):
        try:
                req = Request(s + '://' + h + ':' + p + '/')
                req.add_header('Host', v)
                f = urlopen(req)
                return str(f.info())
        except HTTPError, e:
                return str(e.info())
        except URLError, e:
                return str(e)

