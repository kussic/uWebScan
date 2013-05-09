from urllib2 import *
import time

#DIRS = ("/", "/images/", "/admin/")
#FILES = ('index', 'cmd', 'main', 'web', 'www', 'global', 'globals', 'upload', 'uploader', 'guestbook', 'login', 'logon')
#EXTE = ( '.js', '.htm', '.html', '.shtml', '.asp', '.asa', '.doc', '.jsp')

        
ABOUT = "File & Directory Enumeration"
SAFE = "NOT SAFE"

EXTE = ( '.js', '.htm', '.html', '.shtml', '.asp', '.asa', '.doc', '.jsp', '.jsa', '.txt', '.py', '.pl', '.plx', '.cfm', '.php', '.vbs', '.cgi', '.inc', '.tmp', '.old', '.bak', '.bakup', '.sav', '.saved', '.nsf', '.bat', '.com', '.exe', '.dll', '.reg', '.log', '.zip', '.tar', '.tar.gz', '.tgz', '.c', '.o', '.sh', '._', '.cer', '.crl', '.xhtml', '.xml', '.xml.gz', '.asmx', '.asm', '.dat', '.swf', '.inc', '.phps', '.war', '.rar', '.Z', '.7z', '.ace', '')


FILES = ('online', 'offline', 'access_log', 'alpha', 'beta', 'gamma', 'delta', 'phpThumb', 'error_log', 'imagefetch', 'fp30reg', 'index', 'cmd', 'main', 'web', 'www', 'global', 'globals', 'upload', 'uploader', 'guestbook', 'login', 'logon', 'sign', 'signin', 'mail', 'email', 'example', 'examples', 'feedback', 'update', 'test', 'readme', 'users', 'user', 'adm', 'admin', 'staff', 'client', 'clients', 'pass', 'password', 'passwords', 'passwd', 'default', 'root', 'perl', 'log', 'logs', 'logfile', 'logfiles', 'details', 'backup', 'src', 'source', 'INSTALL', 'README', 'ICA_CRL1', 'internal_ca_b64', 'internal_ca', 'sitemap', 'robots', 'SCUserService', 'ExternalOPRService', 'php-backdoor', 'asp-backdoor', 'backdoor', 'bkdr', 'backdr', 'bdoor', 'bdr', 'simple-backdoor', 'cmd', 'phpshell', 'aspshell', 'jspshell', 'shell', 'ironshell', 'NCC-Shell', 'lamashell', 'load_shell', 'matamu', 'myshell', 'mysql', 'mysql_tool', 'c99_w4cking', 'Crystal', 'ctt_sh', 'cybershell', 'Dx', 'gfs_sh', 'iMHaPFtp', 'c99_PSych0', 'c99_madnet', 'c99_locus7s', 'c99', 'backupsql', 'accept_language', 'pws', 'pwd', 'r57', 'r57_iFX', 'r57_kartal', 'kartal', 'r57_Mohajer22', 'rootshell', 'ru24_post_sh', 'pHpINJ', 'PHPJackal', 'Private-i3lue', 'PHPRemoteView', 'php-include-w-shell', 'PHANTASMA', 'nstview', 'nshell', 'NetworkFileManagerPHP', 'simple_cmd', 'Uploader', 'zacosmall', 'perlcmd', 'jsp-reverse', 'cmdjsp', 'cmd_win32', 'win32', 'JspWebshell', 'JspWebshell%201.2', 'cmdasp', 'cmd-asp-5.1', 'ntdaddy', 'cfexec', 'template', 'templates', 'access', 'error', 'security', 'tmp', 'ani2', 'anifile', 'crypt', 'crypt2', 'cryptor', 'ff', 'file', 'flush', 'fout', 'GeoIP', 'geoip', 'logincheck', 'maketable', 'mdac4', 'mdac', 'megapack1', 'megapack', 'ms06-44_w2k', 'notfound', 'o7', 'qt', 'qtl', 'settings', 'urlworks', 'xml', 'xmlrpc', 'wp-settings', 'wp-trackback', 'wp-rss2', 'wp-pass', 'wp-mail', 'wp-register', 'wp-rss', 'wp-rdf', 'wp-login', 'wp-feed', 'wp-cron', 'wp-config', 'wp-config-sample', 'pw', 'submit_config', 'template', 'favicon', 'autorun', 'zombie', 'zombies', 'bs')


DIRS=('/', '/mailer/', '/phpmailer/', '/thumbnail/', '/paweb/', '/peweb/', '/intraweb/', '/landing_pages/', '/corporate/', '/alpha/', '/beta/', '/gamma/', '/delta/', '/template/', '/templates/', '/access/', '/active/', '/adm/', '/admin/', '/_admin/', '/administrator/', '/app/', '/apps/', '/archive/', '/archives/', '/asp/', '/back/', '/backup/', '/back-up/', '/bak/', '/bakup/', '/bak-up/', '/basic/', '/bea/', '/bin/', '/binaries/', '/broken/', '/c/', '/cc/', '/ccs/', '/cache/', '/cgi/', '/cgibin/', '/cgi-bin/', '/cgi-win/', '/class/', '/classes/', '/classified/', '/classifieds/', '/code/', '/common/', '/credit/', '/creditcards/', '/cv/', '/cvs/', '/customer/', '/customers/', '/CYBERDOCS/', '/CYBERDOCS25/', '/CYBERDOCS31/', '/d/', '/data/', '/database/', '/db/', '/dbase/', '/dbm/', '/dbms/', '/demo/', '/dev/', '/devel/', '/develop/', '/development/', '/doc/', '/docs/', '/docs41/', '/docs51/', '/dms/', '/e/', '/email/', '/download', '/downloads/', '/ecommerce/', '/ebriefs/', '/error/', '/errors/', '/esales/', '/echannel/', '/esupport/', '/etc/', '/exec/', '/executable/', '/executables/', '/extra/', '/extranet/', '/examples/', '/exchange/', '/fcgi-bin/', '/feedback/', '/file/', '/files/', '/forum/', '/forums/', '/ftp/', '/graphics/', '/guestbook/', '/guests/', '/help/', '/hidden/', '/hide/', '/home/', '/homes/', '/htm/', '/html/', '/images/', '/inc/', '/incs/', '/include/', '/includes/', '/interactive/', '/internet/', '/intranet/', '/java/', '/javascript/', '/js/', '/jsp/', '/keep/', '/kept/', '/ldap/', '/lib/', '/libs/', '/libraries/', '/links/', '/log/', '/logfiles/', '/logs/', '/mail/', '/me/', '/member/', '/members/', '/mine/', '/mirror/', '/mirrors/', '/mp3/', '/mp3s/', '/ms/', '/mssql/', '/ms-sql/', '/music/', '/my/', '/new/', '/old/', '/online/', '/order/', '/orders/', '/pages/', '/_pages/', '/pass/', '/passes/', '/passwd/', '/password/', '/passwords/', '/perl/', '/personal/', '/personals/', '/php/', '/pics/', '/pl/', '/pls/', '/plx/', '/press/', '/priv/', '/private/', '/product/', '/products/', '/production/', '/pub/', '/public/', '/removed/', '/reports/', '/root/', '/sales/', '/save/', '/saved/', '/scripts/', '/secret/', '/secrets/', '/secure/', '/security/', '/servlet/', '/servlets/', '/soap/', '/soapdocs/', '/source/', '/site/', '/sites/', '/SiteServer/', '/sql/', '/src/', '/staff/', '/stats/', '/statistics/', '/stuff/', '/support/', '/temp/', '/temps/', '/test/', '/text/', '/texts/', '/tmp/', '/upload/', '/uploads/', '/user/', '/users/', '/var/', '/vb/', '/vbs/', '/vbscript/', '/vbscripts/', '/weblogic/', '/www/', '/xcache/', '/xsql/', '/zip/', '/zips/', '/~adm/', '/~admin/', '/~administrator/','/~guest/', '/~mail/', '/~operator/', '/~root/', '/~admin/', '/~sys/', '/~sysadm/', '/~sysadmin/', '/~test/', '/~user/', '/~www/', '/~webmaster/', '/W3SVC/', '/W3SVC3/', '/wp-content/', '/code/', '/wp-admin/', '/website/', '/webservices/', '/wholesale/', '/hook/', '/modules/', '/ui/', '/css/', '/autorun/' ,'/zombie/', '/zombies/')

FDIRS=[]
FFILES=[]

def get( host, ssl, port, vhost ): 
	

	print "Please wait, this might take a while..."
	errcnt = 0
	for d in DIRS:
		s = ssl
		h = host
		p = port
		v = vhost
                dfcount = 0

		if s == "https":
			h = httplib.HTTPS(h,int(p))
		else:
			h = httplib.HTTP(h,int(p))
		h.putrequest('GET', d)
		h.putheader('host', v)
		h.endheaders()
		ec, em, hd = h.getreply()
		if ec != 404:
                        print "\n\n:: Entering: " + d
			FDIRS.append(str(ec) + ": " + d)
                        everytest = FILES.__len__() * EXTE.__len__()
                        sys.stdout.write(":Test #" + "0"* len(str(everytest)) + "/" + str(everytest))
                        sys.stdout.flush()
                        loopcount = 0
			for f in FILES:
				for e in EXTE:
					#time.sleep(9)
					s = ssl
					h = host
					p = port
					v = vhost
                                        #everytest = FILES.__len__() * EXTE.__len__() 
                                        loopcount = loopcount + 1
                                        #dfcount = dfcount + 1
					df = d + f + e
                                        llc = len(str(everytest)) - len(str(loopcount))
                                        bllc = (len(str(everytest))*2) + 1
                                        sys.stdout.write("\b"*bllc + "0"*llc + str(loopcount) + "/" + str(everytest))
                                        sys.stdout.flush()
					if s == "https":
						h = httplib.HTTPS(h,int(p))
					else:
						h = httplib.HTTP(h,int(p))
					h.putrequest('GET', df)
					h.putheader('host', v)
					h.endheaders()
					try:	
						ec, em, hd = h.getreply()
					except socket.error, (value,message):
						#print "ERR: \"" + message + "\" for: " + df
						FFILES.append("ERR: \"" + message + "\" for: " + df)
						errcnt = errcnt + 1
						if errcnt == 3:
							return "Terminated - Too many exceptions..."

					if ec != 404 and ec != 500:
                                                #sys.stdout.write("!")
						FFILES.append(str(ec) + ": " + df)
	print "\n"
	out = "Found Directories:\n"
	for fd in FDIRS:
		out = out + fd + "\n"
	out = out + "\nFound Files:\n"
	for ff in FFILES:
		out = out + ff + "\n"
	return out
