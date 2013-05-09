A small modular web scanner written in python.

This is not meant as a replacement to Nikto or similar scanners. 

I wrote it simply because I wanted a more modular tool that provided me with more verbose and elegant output which I could then paste into a pentest report.

**Current List of Modules:**

[S] = Safe / [N] = Not Safe

* [S] apacheversion: Apache HTTPD Version Detection
* [S] bigipcookie  : F5 BIGIP Cookie IP Exposure
* [S] httpheaders  : HTTP Headers Available
* [S] httpoptions  : HTTP OPTIONS Available
* [S] httptracevuln: HTTP TRACE Vulnerability
* [S] intipvuln    : Internal IP Vulnerability
* [S] ntlmvuln     : NTLM Authentication Vulnerability
* [S] propfindvuln : PROPFIND (WebDAV) Vulnerability
* [S] robotstxtvuln: Robots.txt "Disallow" Disclosure
* [N] webr00t      : File & Directory Enumeration
* [S] webtime      : Web Server Clock Check


For example the BIP IP Cookie module looks something like this:


	--------------------------------------------
	F5 BIGIP Cookie IP Exposure - 134.154.190.15
	--------------------------------------------
	
		  
	BigIP Cookie name:  
	BigIP Cookie Value: 193501830.20480.0000; path
	Decoded IP [port]: 134.154.136.11 [80]


The NTLM Authentication Information Exposure module looks like:

	---------------------------------------------------
	NTLM Authentication Vulnerability - 194.121.129.178
	---------------------------------------------------

	Base64:
	TlRMTVNTUAACAAAACgAKADgAAAAFgoGiGKFRcmDs0FAAAAAAAAAAAH4AfgBCAAAABQLODgAAAA9KAE8AVwBBAFQAAgAKAEoATwBXAEEAVAABAAwAUwBFAFIAVgBFAFIABAAWAEoAbwB3AGEAdAAuAGwAbwBjAGEAbAADACQAUwBFAFIAVgBFAFIALgBKAG8AdwBhAHQALgBsAG8AYwBhAGwABQAWAEoAbwB3AGEAdAAuAGwAbwBjAGEAbAAAAAAA
	Decode:
	0000   4E 54 4C 4D 53 53 50 00 02 00 00 00 0A 00 0A 00    NTLMSSP.........
	0010   38 00 00 00 05 82 81 A2 18 A1 51 72 60 EC D0 50    8.........Qr`..P
	0020   00 00 00 00 00 00 00 00 7E 00 7E 00 42 00 00 00    ........~.~.B...
	0030   05 02 CE 0E 00 00 00 0F 4A 00 4F 00 57 00 41 00    ........J.O.W.A.
	0040   54 00 02 00 0A 00 4A 00 4F 00 57 00 41 00 54 00    T.....J.O.W.A.T.
	0050   01 00 0C 00 53 00 45 00 52 00 56 00 45 00 52 00    ....S.E.R.V.E.R.
	0060   04 00 16 00 4A 00 6F 00 77 00 61 00 74 00 2E 00    ....J.o.w.a.t...
	0070   6C 00 6F 00 63 00 61 00 6C 00 03 00 24 00 53 00    l.o.c.a.l...$.S.
	0080   45 00 52 00 56 00 45 00 52 00 2E 00 4A 00 6F 00    E.R.V.E.R...J.o.
	0090   77 00 61 00 74 00 2E 00 6C 00 6F 00 63 00 61 00    w.a.t...l.o.c.a.
	00A0   6C 00 05 00 16 00 4A 00 6F 00 77 00 61 00 74 00    l.....J.o.w.a.t.
	00B0   2E 00 6C 00 6F 00 63 00 61 00 6C 00 00 00 00 00    ..l.o.c.a.l.....


And the Robots.txt Analysis tool looks like:

	---------------------------------------------------
	Robots.txt "Disallow" Disclosure - www.google.co.uk
	---------------------------------------------------

  
	Found Directories:
	
	/nwshp
	/index.html?
	/?
	/?hl=*&
	/imglanding
	/custom
	[...]
	/wapsearch?
	/quality_form?
	/compressiontest/

	Redirects:

	/search
	/u/
	[...]
	/ads/preferences/
	/settings/ads/onweb/

	Not Found:
	
	/sdch
	[...]
	/evaluation/
	/webstore/search
	
	Other results:
	
	(301 Moved Permanently) /univ/
	(301 Moved Permanently) /url
	(403 Forbidden) /xml?
	(500 Internal Server Error) /gwt/
	(301 Moved Permanently) /froogle?
	(400 Bad Request) /maps/api/staticmap?