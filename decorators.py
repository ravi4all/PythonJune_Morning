Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> urllib
Help on package urllib:

NAME
    urllib

PACKAGE CONTENTS
    error
    parse
    request
    response
    robotparser

FILE
    c:\python36-32\lib\urllib\__init__.py


help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> import urllib
>>> data = urllib.request("https://www.google.co.in/?gws_rd=ssl")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    data = urllib.request("https://www.google.co.in/?gws_rd=ssl")
AttributeError: module 'urllib' has no attribute 'request'
>>> import urllib.request
>>> with urllib.request.urlopen('http://www.google.co.in/?gws_rd=ssl') as response:
   html = response.read()

   
>>> html
b'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-IN"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script>(function(){window.google={kEI:\'IBZfWaOIKcPmvgSZ9YzoDA\',kEXPI:\'1353382,1353742,1354562,1354586,3700330,3700347,3700433,3700442,4029815,4031109,4036527,4039268,4043492,4045841,4048347,4072775,4076999,4078430,4078761,4081038,4081164,4084976,4093134,4093313,4094544,4095910,4097153,4097470,4097922,4097929,4097951,4098721,4098728,4098752,4101430,4101437,4101750,4102238,4103475,4103861,4105086,4105178,4105240,4106085,4106192,4106625,4107234,4107555,4109092,4109316,4109490,4109525,4110260,4110656,4111016,4111925,4112319,4113146,4113148,4113492,4114476,4114876,4114975,4115687,4115697,4116370,4116702,4116926,4116928,4116935,4117161,4117267,4117512,4117533,4117730,4117912,4117980,4118227,4118345,4118352,4118475,4118531,4118533,4118782,4118798,4119032,4119034,4119036,4119136,4119258,4119272,4120004,4120045,4120057,4120194,4120331,4120593,4120840,4120885,10200084,16200027,19002735,19002742,19002763,19002764,19002766,19002767,19002769,41027342\',authuser:0,kscs:\'c9c918f0_24\'};google.kHL=\'en-IN\';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};google.https=function(){return"https:"==window.location.protocol};google.ml=function(){return null};google.wl=function(a,b){try{google.ml(Error(a),!1,b)}catch(c){}};google.time=function(){return(new Date).getTime()};google.log=function(a,b,c,d,g){a=google.logUrl(a,b,c,d,g);if(""!=a){b=new Image;var e=google.lc,f=google.li;e[f]=b;b.onerror=b.onload=b.onabort=function(){delete e[f]};window.google&&window.google.vel&&window.google.vel.lu&&window.google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,c,d,g){var e="",f=google.ls||"";c||-1!=b.search("&ei=")||(e="&ei="+google.getEI(d),-1==b.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));a=c||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+e+f+"&zx="+google.time();/^http:/i.test(a)&&google.https()&&(google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a};google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=String(Math.random());while(c in google.y)}google.y[c]=[a,b];return!1};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}\n</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}a.gb1,a.gb2,a.gb3,a.gb4{color:#11c !important}body{background:#fff;color:black}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}a.gb1,a.gb4{text-decoration:underline}a.gb3:hover{text-decoration:none}#ghead a.gb2:hover{color:#fff !important}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script></script><link href="/images/branding/product/ico/googleg_lodp.ico" rel="shortcut icon"></head><body bgcolor="#fff"><script>(function(){var src=\'/images/nav_logo229.png\';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}\nif (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}\n}\n})();</script><div id="mngb"> <div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href="http://www.google.co.in/imghp?hl=en&tab=wi">Images</a> <a class=gb1 href="http://maps.google.co.in/maps?hl=en&tab=wl">Maps</a> <a class=gb1 href="https://play.google.com/?hl=en&tab=w8">Play</a> <a class=gb1 href="http://www.youtube.com/?gl=IN&tab=w1">YouTube</a> <a class=gb1 href="http://news.google.co.in/nwshp?hl=en&tab=wn">News</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a> <a class=gb1 style="text-decoration:none" href="https://www.google.co.in/intl/en/options/"><u>More</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.co.in/history/optout?hl=en" class=gb4>Web History</a> | <a  href="/preferences?hl=en" class=gb4>Settings</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://www.google.co.in/%3Fgws_rd%3Dssl" class=gb4>Sign in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div> </div><center><br clear="all" id="lgpd"><div id="lga"><div style="padding:28px 0 3px"><div style="height:110px;width:276px;background:url(/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png) no-repeat" title="Google" align="left" id="hplogo" onload="window.lol&&lol()"><div style="color:#777;font-size:16px;font-weight:bold;position:relative;top:70px;left:218px" nowrap="">India</div></div></div><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="en-IN" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0"><input style="color:#000;margin:0;padding:5px 8px 0 6px;vertical-align:top" autocomplete="off" class="lst" value="" title="Google Search" maxlength="2048" name="q" size="57"></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" value="Google Search" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" value="I\'m Feeling Lucky" name="btnI" onclick="if(this.form.q.value)this.checked=1; else top.location=\'/doodles/\'" type="submit"></span></span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=en-IN&amp;authuser=0">Advanced search</a><a href="/language_tools?hl=en-IN&amp;authuser=0">Language tools</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br><div id="als"><style>#als{font-size:small;margin-bottom:24px}#_eEe{display:inline-block;line-height:28px;}#_eEe a{padding:0 3px;}._lEe{display:inline-block;margin:0 2px;white-space:nowrap}._PEe{display:inline-block;margin:0 2px}</style><div id="_eEe">Google.co.in offered in: <a href="/url?q=http://www.google.co.in/setprefs%3Fsig%3D0_sv6Ga5gLHjRI6klOH7piZg5lGSQ%253D%26hl%3Dhi%26source%3Dhomepage&amp;sa=U&amp;ved=0ahUKEwijmJC7svbUAhVDs48KHZk6A80Q2ZgBCAU&amp;usg=AFQjCNETqgkc7_8kszB7VTUlrAAd5Y7UNQ">&#2361;&#2367;&#2344;&#2381;&#2342;&#2368;</a>  <a href="/url?q=http://www.google.co.in/setprefs%3Fsig%3D0_sv6Ga5gLHjRI6klOH7piZg5lGSQ%253D%26hl%3Dbn%26source%3Dhomepage&amp;sa=U&amp;ved=0ahUKEwijmJC7svbUAhVDs48KHZk6A80Q2ZgBCAY&amp;usg=AFQjCNGpdFUKyo3PNA4PiUhO-SrzAl1YdA">&#2476;&#2494;&#2434;&#2482;&#2494;</a>  <a href="/url?q=http://www.google.co.in/setprefs%3Fsig%3D0_sv6Ga5gLHjRI6klOH7piZg5lGSQ%253D%26hl%3Dte%26source%3Dhomepage&amp;sa=U&amp;ved=0ahUKEwijmJC7svbUAhVDs48KHZk6A80Q2ZgBCAc&amp;usg=AFQjCNG5ESKAZdTlFibzXBb2mmvWppkC0A">&#3108;&#3142;&#3122;&#3137;&#3095;&#3137;</a>  <a href="/url?q=http://www.google.co.in/setprefs%3Fsig%3D0_sv6Ga5gLHjRI6klOH7piZg5lGSQ%253D%26hl%3Dmr%26source%3Dhomepage&amp;sa=U&amp;ved=0ahUKEwijmJC7svbUAhVDs48KHZk6A80Q2ZgBCAg&amp;usg=AFQjCNEmCFbu8MgHGK24v4I0ejBVk8TaRw">&#2350;&#2352;&#2366;&#2336;&#2368;</a>  <a href="/url?q=http://www.google.co.in/setprefs%3Fsig%3D0_sv6Ga5gLHjRI6klOH7piZg5lGSQ%253D%26hl%3Dta%26source%3Dhomepage&amp;sa=U&amp;ved=0ahUKEwijmJC7svbUAhVDs48KHZk6A80Q2ZgBCAk&amp;usg=AFQjCNELHqsmlj2EijS9TW2iJFiLRp2-tw">&#2980;&#2990;&#3007;&#2996;&#3021;</a>  <a href="/url?q=http://www.google.co.in/setprefs%3Fsig%3D0_sv6Ga5gLHjRI6klOH7piZg5lGSQ%253D%26hl%3Dgu%26source%3Dhomepage&amp;sa=U&amp;ved=0ahUKEwijmJC7svbUAhVDs48KHZk6A80Q2ZgBCAo&amp;usg=AFQjCNEKqYzkEAnhTfRvyLhyKa1LpqpNXw">&#2711;&#2753;&#2716;&#2736;&#2750;&#2724;&#2752;</a>  <a href="/url?q=http://www.google.co.in/setprefs%3Fsig%3D0_sv6Ga5gLHjRI6klOH7piZg5lGSQ%253D%26hl%3Dkn%26source%3Dhomepage&amp;sa=U&amp;ved=0ahUKEwijmJC7svbUAhVDs48KHZk6A80Q2ZgBCAs&amp;usg=AFQjCNERrV6GJsDGbpJptmPB_7LS_mzlsQ">&#3221;&#3240;&#3277;&#3240;&#3233;</a>  <a href="/url?q=http://www.google.co.in/setprefs%3Fsig%3D0_sv6Ga5gLHjRI6klOH7piZg5lGSQ%253D%26hl%3Dml%26source%3Dhomepage&amp;sa=U&amp;ved=0ahUKEwijmJC7svbUAhVDs48KHZk6A80Q2ZgBCAw&amp;usg=AFQjCNEsfyOL1To-b6KeLaM6Bf7i5SPfXQ">&#3374;&#3378;&#3375;&#3390;&#3379;&#3330;</a>  <a href="/url?q=http://www.google.co.in/setprefs%3Fsig%3D0_sv6Ga5gLHjRI6klOH7piZg5lGSQ%253D%26hl%3Dpa%26source%3Dhomepage&amp;sa=U&amp;ved=0ahUKEwijmJC7svbUAhVDs48KHZk6A80Q2ZgBCA0&amp;usg=AFQjCNF9HiM7W3yzq3XaR7et3M2xq_rNIA">&#2602;&#2672;&#2588;&#2622;&#2604;&#2624;</a> </div></div></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="fll"><a href="/intl/en/ads/">Advertising\xa0Programs</a><a href="http://www.google.co.in/services/">Business Solutions</a><a href="https://plus.google.com/104205742743787718296" rel="publisher">+Google</a><a href="/intl/en/about.html">About Google</a><a href="http://www.google.co.in/setprefdomain?prefdom=US&amp;sig=__wFz6pnbuQQNWTENrhG9HlWkqSq4%3D" id="fehl">Google.com</a></div></div><p style="color:#767676;font-size:8pt">&copy; 2017 - <a href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p></span></center><script>(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b)var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body,a=d.clientWidth,b=d.clientHeight;a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();</script><div id="xjsd"></div><div id="xjsi"><script>(function(){function c(b){window.setTimeout(function(){var a=document.createElement("script");a.src=b;document.getElementById("xjsd").appendChild(a)},0)}google.dljp=function(b,a){google.xjsu=b;c(a)};google.dlj=c;}).call(this);(function(){window.google.xjsrm=[];})();if(google.y)google.y.first=[];if(!google.xjs){window._=window._||{};window._DumpException=window._._DumpException=function(e){throw e};if(google.timers&&google.timers.load.t){google.timers.load.t.xjsls=new Date().getTime();}google.dljp(\'/xjs/_/js/k\\x3dxjs.hp.en_US.R7p6zJw_LYA.O/m\\x3dsb_he,d/am\\x3dADA/rt\\x3dj/d\\x3d1/t\\x3dzcms/rs\\x3dACT90oHzS09RYeR6g8dbklbf5rMSPjmKlQ\',\'/xjs/_/js/k\\x3dxjs.hp.en_US.R7p6zJw_LYA.O/m\\x3dsb_he,d/am\\x3dADA/rt\\x3dj/d\\x3d1/t\\x3dzcms/rs\\x3dACT90oHzS09RYeR6g8dbklbf5rMSPjmKlQ\');google.xjs=1;}google.pmc={"sb_he":{"agen":false,"cgen":false,"client":"heirloom-hp","dh":true,"dhqt":true,"ds":"","fl":true,"host":"google.co.in","isbh":28,"jam":0,"jsonp":true,"msgs":{"cibl":"Clear Search","dym":"Did you mean:","lcky":"I\\u0026#39;m Feeling Lucky","lml":"Learn more","oskt":"Input tools","psrc":"This search was removed from your \\u003Ca href=\\"/history\\"\\u003EWeb History\\u003C/a\\u003E","psrl":"Remove","sbit":"Search by image","srch":"Google Search"},"nds":true,"ovr":{},"pq":"","refpd":true,"rfs":[],"sbpl":24,"sbpr":24,"scd":10,"sce":5,"stok":"ZZ9WWA9fvBwwEnxH5zbWW89U56I"},"d":{},"aWiv7g":{},"YFCs/g":{}};google.y.first.push(function(){if(google.med){google.med(\'init\');google.initHistory();google.med(\'history\');}});if(google.j&&google.j.en&&google.j.xi){window.setTimeout(google.j.xi,0);}\n</script></div></body></html>'
>>> 
 RESTART: E:\Python\Python_Batches\PythonJune_Morning\14-URL_Parsing\url_parsing.py 
Traceback (most recent call last):
  File "E:\Python\Python_Batches\PythonJune_Morning\14-URL_Parsing\url_parsing.py", line 9, in <module>
    wr.write(html)
TypeError: write() argument must be str, not bytes
>>> 
 RESTART: E:\Python\Python_Batches\PythonJune_Morning\14-URL_Parsing\url_parsing.py 
>>> a = [2,4,5,1,2,7,8,9,5,4,2,4,76]
>>> sorted(a)
[1, 2, 2, 2, 4, 4, 4, 5, 5, 7, 8, 9, 76]
>>> sorted(a,reverse=True)
[76, 9, 8, 7, 5, 5, 4, 4, 4, 2, 2, 2, 1]
>>> a = ['Ram','Shyam','Amit','Akash','Ravi','Deepak','Pooja','Zayn']
>>> sorted(a)
['Akash', 'Amit', 'Deepak', 'Pooja', 'Ram', 'Ravi', 'Shyam', 'Zayn']
>>> a = [{"Name":"Ram","Salary":12000},{"Name":"Amit","Salary":23000,"Name":"Zayn","Salary":15000}]
>>> a = [{"Name":"Ram","Salary":12000},{"Name":"Amit","Salary":23000},{"Name":"Zayn","Salary":15000}]
>>> a
[{'Name': 'Ram', 'Salary': 12000}, {'Name': 'Amit', 'Salary': 23000}, {'Name': 'Zayn', 'Salary': 15000}]
>>> sorted(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    sorted(a)
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> a['Name']
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a['Name']
TypeError: list indices must be integers or slices, not str
>>> sum = lambda x,y : x + y
>>> sum(1,2)
3
>>> def a():
	def b():
		print("Inside B")
	print("Inside A")

>>> a()
Inside A
>>> b()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b()
NameError: name 'b' is not defined
>>> def a():
	def b():
		print("Inside B")
	print("Inside A")
	b()

>>> a()
Inside A
Inside B
>>> def x():
	print("Hello X")

>>> x_1 = x
>>> x_1
<function x at 0x03C8A8E8>
>>> x_1()
Hello X
>>> def x(g):
	print("Hello X")
	def g():
		print("Hello G")

	
>>> x()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    x()
TypeError: x() missing 1 required positional argument: 'g'
>>> x("Hi")
Hello X
>>> def x(g):
	print("Hello X")

>>> def g():
	print("Hello G")

>>> x(g)
Hello X
>>> x(g())
Hello G
Hello X
>>> a = [{"Name":"Ram","Salary":12000},{"Name":"Amit","Salary":23000},{"Name":"Zayn","Salary":15000}]
>>> newlist = sorted(a, key=lambda k: k['Name'])
>>> newlist
[{'Name': 'Amit', 'Salary': 23000}, {'Name': 'Ram', 'Salary': 12000}, {'Name': 'Zayn', 'Salary': 15000}]
>>> newlist = sorted(a, key=lambda k: k['Salary'])
>>> newlist
[{'Name': 'Ram', 'Salary': 12000}, {'Name': 'Zayn', 'Salary': 15000}, {'Name': 'Amit', 'Salary': 23000}]
>>> 
