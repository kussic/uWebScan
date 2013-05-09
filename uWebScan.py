#!/usr/bin/env python

VERSION = "1.2"

import os, sys, getopt, time, urllib2, httplib


mod_list = []
DIR = "uws"

def run_mod(dir, mod, host, ssl, port, vhost):
	""" Runs the specified module... """
	global safemode	
	global outputFile
	#print "I'll run " + mod + " on " + ssl + "://" + host + ":" + port + " using vhost: " + vhost

	if mod.strip().lower() == "scan-all":
		for m in mod_list:
			run_mod(dir, m, host, ssl, port, vhost)

	else:
		try:
			module = __import__(mod)
		except ImportError:
			print "ERROR: Module not found."
			return

		header(getattr(module, "ABOUT") + " - " + host)
		if safemode and getattr(module, "SAFE") != "SAFE":
			
			printnsave(mod + ": Marked as [" + getattr(module, "SAFE") + "] and Safe Mode is: " + str(safemode) + "\n", outputFile)
		else:
			if "vuln" in mod:
				printnsave(getattr(module, "vuln")(host, ssl, port, vhost), outputFile)
			else:
				printnsave(getattr(module, "get")(host, ssl, port, vhost), outputFile)

def enum_mod(dir):
    """ Imports the libs, returns a list of the libraries. 
    Pass in dir to scan """
    for f in os.listdir(dir):
    	module_name, ext = os.path.splitext(f) # Handles no-extension files, etc
        if ext == '.py' and module_name != '__init__': # Important, ignore .pyc/other files.
        	
        	module = __import__(module_name)
        	if getattr(module, "ABOUT") != "IGNORE":
				mod_list.append(module_name)

def list_mod(dir):
	mod_len = 0
	enum_mod(dir)
	print "\nList of Modules:\n [S] = Safe / [N] = Not Safe\n"
	
	for l in mod_list:
		if len(l) > mod_len:
			mod_len = len(l)

	for m in mod_list:	
		module = __import__(m)
		if len(m) < mod_len:
			dm = mod_len - len(m)
			m = m + dm*" "
		if getattr(module, "SAFE") == "SAFE":
			mod_safe = "S"
		else:
			mod_safe = "N"
		print " * [" + mod_safe + "] " +  m + ": " + getattr(module, "ABOUT") 
 

###############################################################################

def mainLoop(dir):


    oldPrompt = ""
    prevRes = ""
    
    global outputFile
    outputFile=""
    global safemode
    safemode = True

    while 1:
        try:
            res = raw_input("uws> ")
        except KeyboardInterrupt:
            print "Aborted."
            sys.exit(0)
        except EOFError:
            print "Exit."
            sys.exit(0)
        except:
            print "INTERNAL ERROR:",sys.exc_info()[1]

        if res.lower() == "quit" or res.lower() == "exit":
            break
        elif res.lower() == "list":
        	list_mod(dir)
        elif res.lower() == "safemode":
			if safemode:
				safemode = False
			else:
				safemode = True

			print "Safe Mode: [" + str(safemode) + "]"
        elif "run " in res.lower():
			mod = res.strip().lower().split(" ") 
			mod.remove("run")
			mod
			host = raw_input("Host: ")
			if host == "":
				host = "127.0.0.1"
			ssl = raw_input("SSL (y/N): ")
			if ssl.lower() == "y":
				ssl = "https"
				portn = "443"
			else:
				ssl = "http"
				portn = "80"
			port = raw_input("Port (" + portn + "): ")
			if port == "":
				port = portn
			vhost = raw_input("Vhost ("+host+"): ")
			if vhost == "":
				vhost = host
			
			print "\n"	
			if "scan-all" in mod:
					run_mod(dir, "scan-all", host, ssl, port, vhost)
			else:
				for m in mod:
					run_mod(dir, m, host, ssl, port, vhost)

        else:
			print "ERROR: Command not found."

def header( t ):
	global outputFile
	printnsave(len(t)*"-" + "\n" + t + "\n" + len(t)*"-" + "\n\n", outputFile)


def logo():

	print """
              __    __     _     __                 
        _   _/ / /\ \ \___| |__ / _\ ___ __ _ _ __  
       | | | \ \/  \/ / _ \ '_ \\\\ \ / __/ _` | '_ \ 
       | |_| |\  /\  /  __/ |_) |\ \ (__ (_| | | | |
        \__,_| \/  \/ \___|_.__/\__/\___\__,_|_| |_|
                       uWebScan - Version """ + VERSION  



def iusage():

	logo()
	print """Commands:
  
 * run <module1> [<module2>] ...: Executes the defined modules
 * list: Replays the available list
 * safemode: Toggle Enable/Disable Safe Modules [Default: True]

 * run scan-all: Executes all available modules
 
Command-line:
	./uWebScan.py --help"""


def cusage():

	logo()
	print """
FILE PARAMETERS:
 -o | --of      : Specify output file
 -i | --if      : Specify input file

HOST PARAMETERS:
  
 -h | --host    : Specify the host to scan   
 -p | --port    : Specify the port to scan   [Default: "80"]
 -v | --vhost   : Specify vhost to use       [Default: <host>]
 -s | --ssl     : Use SSL (HTTPS)            [Default: <No SSL>]

MODULES:
 -l | --list    : List available modules
 -m | --mod     : Specify module(s) to scan  [Default: "scan-all"]
 -n | --notsafe : Disable Safe Mode          [Default: Enabled]
 
 Note: When specifying more than one module must use double quotes!!!

EXAMPLES:

 * uWebScan.py -h www.google.com -m httpoptions - Run against "www.google.com" and use one module
 * uWebScan.py -h mail.google.com -ssl -m "httpoptions httpheaders" - Run against "mail.google.com" use two modules
 """

def printnsave( t, o ):
	print str(t) + "  "
	if o != "":
		fileHandle = open ( o, 'a' )
		fileHandle.write ( t + "\n" )
		fileHandle.close()

def imain(dir):

    dir = os.path.dirname(os.path.abspath(sys.argv[0])) + "/" + dir
    if os.path.isdir(dir):
        sys.path.append(dir)
    iusage()
    list_mod(dir)
    mainLoop(dir)
        
if __name__ == "__main__":
	try:
		if sys.argv[1] :
			opts, args = getopt.getopt(sys.argv[1:], "h:v:p:slm:no:", ["of=", "notsafe", "host=", "vhost=", "port=", "ssl", "list", "help", "mod="])

			#print "Opts: " + str(opts) + " Args: " + str(args)
			
			nhost = "127.0.0.1"
			vhost = ""
			port = "80"
			ssl = "http"
			mod = "scan-all"
			inputFile = ""
			global outputFile
			outputFile = ""
			dir = os.path.dirname(os.path.abspath(sys.argv[0])) + "/" + DIR
			sys.path.append(dir)
			global safemode
			safemode = True

			for o, a in opts:
				if o == "-h" or o == "--host":
					nhost = a
					vhost = a
				if o == "-v" or o == "--vhost":
					vhost = a
				if o == "-p" or o == "--port":
					port = a
				if o == "-s" or o == "--ssl":
					ssl = "https"
					if port == "80":
						port = "443"
				if o == "-m" or o == "--mod":
					mod = a.strip().lower().split(" ")
				if o == "-n" or o == "--notsafe":
					safemode = False
				if o == "-o" or o == "--of":
					outputFile = a
					
					fileHandle = open ( a, 'a' )
                                        fileHandle.write ("#======================================================================#\n")
					fileHandle.write ("# ")
					for op in sys.argv:
						fileHandle.write (op + " ")
                                        fileHandle.write ("\n#======================================================================#")
					fileHandle.write("\n\n")
					fileHandle.close()

				if o == "--help":
					cusage()
					sys.exit(1)
				if o == "-l" or o == "--list":
					logo()
					list_mod(dir)
					sys.exit(0)
			
			logo()
			printnsave("Host: " + ssl + "://" + nhost + ":" + port + "\nVhost: " + vhost + "\nSafe Mode: " + str(safemode) + "\nDate: " + time.strftime("%a, %d %b %Y %H:%M:%S") + "\n", outputFile)

			enum_mod(dir)
			if "scan-all" in mod:
				run_mod(dir, "scan-all", nhost, ssl, port, vhost)
			else:
				for m in mod:
					run_mod(dir, m, nhost, ssl, port, vhost)


        except getopt.GetoptError:
        	cusage()
        	sys.exit(1)
        except IndexError:
        	imain(DIR)
