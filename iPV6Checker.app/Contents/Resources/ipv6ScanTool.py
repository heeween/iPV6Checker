# -- coding: utf-8 -*-

from __future__ import print_function #line:3
import sys #line:4
import os #line:5
apppath =''#line:9
def isMachOFormat (OOO00OO0O0OO0OOO0 ):#line:10
    if not os .path .exists (OOO00OO0O0OO0OOO0 ):#line:11
        return False ;#line:12
    O0O000OOO00000OO0 =open (OOO00OO0O0OO0OOO0 ,'rb');#line:14
    if O0O000OOO00000OO0 :#line:15
        O0O00OO00OOO0O0O0 =O0O000OOO00000OO0 .read ();#line:16
        OO0O0O00OO0000O0O =O0O000OOO00000OO0 .tell ();#line:17
        O0O000OOO00000OO0 .close ();#line:18
        if OO0O0O00OO0000O0O >8 :#line:19
            OO000O0O0OOO00OO0 =O0O00OO00OOO0O0O0 [0 ].encode ('hex')#line:20
            OOO00O0O00O0O0OO0 =O0O00OO00OOO0O0O0 [1 ].encode ('hex')#line:21
            OOO0O0O0O00OO00O0 =O0O00OO00OOO0O0O0 [2 ].encode ('hex')#line:22
            OO0OOO0000OO00OOO =O0O00OO00OOO0O0O0 [3 ].encode ('hex')#line:23
            OOOOO00O0OOOO00OO =OO000O0O0OOO00OO0 +OOO00O0O00O0O0OO0 +OOO0O0O0O00OO00O0 +OO0OOO0000OO00OOO ;#line:24
            if OOOOO00O0OOOO00OO =="cafebabe":#line:25
                return True ;#line:26
    return False ;#line:27
def scanFiles (OOOOO0OO000000OOO ):#line:32
    if not os .path .exists (OOOOO0OO000000OOO ):#line:33
        eprint ("文件路径:"+OOOOO0OO000000OOO +"不存在!")#line:34
        return -1 ;#line:35
    OOOOO0OOO00OO0OO0 =OOOOO0OO000000OOO .split ("/");#line:36
    O0OO0OO00OO00OOO0 =OOOOO0OOO00OO0OO0 .pop ();#line:37
    for O00O0OO0000OOO00O ,OO0OO00OOOO000O0O ,OOOOOOOO00OO00O0O in os .walk (OOOOO0OO000000OOO ):#line:40
        for O0O000OOOOOOOOO0O in OOOOOOOO00OO00O0O :#line:41
            OO0OO000OOO0OOOO0 =os .path .join (O00O0OO0000OOO00O ,O0O000OOOOOOOOO0O );#line:43
            O0O000OOO0O00000O =isMachOFormat (OO0OO000OOO0OOOO0 )#line:44
            if O0O000OOO0O00000O and not os .path .islink (OO0OO000OOO0OOOO0 ):#line:45
                nmCheck (OO0OO000OOO0OOOO0 ,O0O000OOOOOOOOO0O ,O0OO0OO00OO00OOO0 )#line:46
def nmCheck (OO0OO0O00OOO0OOOO ,OO00OO000OO00OO00 ,O0OOO0O00OOO00OO0 ):#line:50
    OOOOO00O0O0000OO0 =["inet_addr","inet_aton","inet_lnaof","inet_makeaddr","inet_netof","inet_network","inet_ntoa","inet_ntoa_r","bindresvport","getipv4sourcefilter","setipv4sourcefilter"];#line:61
    O0OOOOOO000O0O00O =OO0OO0O00OOO0OOOO +".log";#line:62
    if os .path .exists (O0OOOOOO000O0O00O ):#line:63
        os .system ("rm -rf "+O0OOOOOO000O0O00O )#line:64
    O00OOO0000O0OO0O0 ="touch "+O0OOOOOO000O0O00O ;#line:66
    OO0O0O00OOO0OO00O =set ();#line:68
    os .system (O00OOO0000O0OO0O0 );#line:70
    for O0O0O00O0O0000000 in OOOOO00O0O0000OO0 :#line:71
        O0O0O000OO0O0O00O ="nm "+OO0OO0O00OOO0OOOO +" >> "+OO0OO0O00OOO0OOOO +".log";#line:72
        os .system (O0O0O000OO0O0O00O );#line:73
    O0OO0OO0OOOOOO0OO =open (O0OOOOOO000O0O00O );#line:75
    if O0OO0OO0OOOOOO0OO :#line:76
        OO0O00O0OOO00000O =O0OO0OO0OOOOOO0OO .read ()#line:77
        OO0O00O0OOO00000O =OO0O00O0OOO00000O .replace ("                 U _","");#line:78
        OO00OO0000OO00000 =OO0O00O0OOO00000O .split ("\n")#line:79
        for OOOO00O0OOO0O00O0 in OO00OO0000OO00000 :#line:80
            for O0O00000OOOO0OOO0 in OOOOO00O0O0000OO0 :#line:81
                if OOOO00O0OOO0O00O0 .find (O0O00000OOOO0OOO0 )!=-1 :#line:82
                    OO0O0O00OOO0OO00O .add ("warning: "+O0O00000OOOO0OOO0 )#line:83
        O0OO0OO0OOOOOO0OO .close ()#line:84
    if len (OO0O0O00OOO0OO00O )>0 :#line:86
        eprint ("application: %s"%OO00OO000OO00OO00 );#line:87
        O0000O0O000OOOO0O =OO0OO0O00OOO0OOOO .find (O0OOO0O00OOO00OO0 );#line:88
        eprint ("path: %s"%OO0OO0O00OOO0OOOO [O0000O0O000OOOO0O :]);#line:89
        eprint ("status: nopass");#line:90
        for OOOO00O0OOO0O00O0 in OO0O0O00OOO0OO00O :#line:91
            eprint (OOOO00O0OOO0O00O0 );#line:92
        eprint ("\r\n")#line:93
    else :#line:94
        eprint ("application: %s"%OO00OO000OO00OO00 );#line:95
        O0000O0O000OOOO0O =OO0OO0O00OOO0OOOO .find (O0OOO0O00OOO00OO0 );#line:96
        eprint ("path: %s"%OO0OO0O00OOO0OOOO [O0000O0O000OOOO0O :]);#line:97
        eprint ("status: pass");#line:98
    if os .path .exists (O0OOOOOO000O0O00O ):#line:100
        os .system ("rm "+O0OOOOOO000O0O00O )#line:101
def eprint (*OOOOOO00OOO0000O0 ,**OO000O000OOOOO000 ):#line:104
    print (*OOOOOO00OOO0000O0 ,file =sys .stderr ,**OO000O000OOOOO000 )#line:105
if __name__ =='__main__':#line:108
    if len (sys .argv )==1 :#line:109
        print ("usage: python ipv6_api_scan.py to_be_checked_dir")#line:110
        eprint ("usage: python ipv6_api_scan.py to_be_checked_dir >> out.log")#line:111
    else :#line:112
        scanFiles (sys .argv [1 ])
#e9015584e6a44b14988f13e2298bcbf9
