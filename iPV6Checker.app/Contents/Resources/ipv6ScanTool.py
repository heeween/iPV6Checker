# -- coding: utf-8 -*-
from __future__ import print_function #line:3
import sys #line:4
import os #line:5
apppath =''#line:9
def isMachOFormat (O00O00O000O00O0O0 ):#line:12
    if not os .path .exists (O00O00O000O00O0O0 ):#line:13
        return False ;#line:14
    O000OO000OO00O000 =open (O00O00O000O00O0O0 ,'rb');#line:16
    if O000OO000OO00O000 :#line:17
        O00O00OOO0O0000O0 =O000OO000OO00O000 .read ();#line:18
        O00O000OO0OO0000O =O000OO000OO00O000 .tell ();#line:19
        O000OO000OO00O000 .close ();#line:20
        if O00O000OO0OO0000O >8 :#line:21
            O0OOO000O0OO0OOO0 =O00O00OOO0O0000O0 [0 ].encode ('hex')#line:22
            O0OOOO0000O0OO00O =O00O00OOO0O0000O0 [1 ].encode ('hex')#line:23
            OOOO0O0OOOOOOO000 =O00O00OOO0O0000O0 [2 ].encode ('hex')#line:24
            OOO0O000O0000OOO0 =O00O00OOO0O0000O0 [3 ].encode ('hex')#line:25
            OO00OO0O00O000000 =O0OOO000O0OO0OOO0 +O0OOOO0000O0OO00O +OOOO0O0OOOOOOO000 +OOO0O000O0000OOO0 ;#line:26
            if OO00OO0O00O000000 =="cafebabe"or "cffaedfe"==OO00OO0O00O000000 or "feedface"==OO00OO0O00O000000 or "feedfacf"==OO00OO0O00O000000 :#line:27
                return True ;#line:28
    return False ;#line:29
def scanFiles (O0O00OO000O0O0OO0 ):#line:34
    if not os .path .exists (O0O00OO000O0O0OO0 ):#line:35
        eprint ("文件路径:"+O0O00OO000O0O0OO0 +"不存在!")#line:36
        return -1 ;#line:37
    OOOO00OOO00O00000 =O0O00OO000O0O0OO0 .split ("/");#line:38
    OO0O00OO0O0O00O00 =OOOO00OOO00O00000 .pop ();#line:39
    for OOOOO0000OO00000O ,OO0OO00O0000OOO0O ,O0OOOO0OO0OO00000 in os .walk (O0O00OO000O0O0OO0 ):#line:42
        for O00O00OO0O000O0O0 in O0OOOO0OO0OO00000 :#line:43
            OOO0OO0OOO00O0O0O =os .path .join (OOOOO0000OO00000O ,O00O00OO0O000O0O0 )#line:45
            O0O0O00OOO0O00OO0 =isMachOFormat (OOO0OO0OOO00O0O0O )#line:46
            if O0O0O00OOO0O00OO0 and not os .path .islink (OOO0OO0OOO00O0O0O ):#line:47
                nmCheck (OOO0OO0OOO00O0O0O ,O00O00OO0O000O0O0 ,OO0O00OO0O0O00O00 )#line:48
def nmCheck (OO00O00O0OO00O0O0 ,OOO00O0OOOO00OO0O ,O00O00O00000O0O00 ):#line:52
    OOOO00OOOO0OOO0OO =["inet_addr","inet_aton","inet_lnaof","inet_makeaddr","inet_netof","inet_network","inet_ntoa","inet_ntoa_r","bindresvport","getipv4sourcefilter","setipv4sourcefilter"];#line:63
    OOOOOO0000OO0OO0O =OO00O00O0OO00O0O0 +".log";#line:64
    if os .path .exists (OOOOOO0000OO0OO0O ):#line:65
        os .system ("rm -rf "+OOOOOO0000OO0OO0O )#line:66
    O0O00O0O00000OOO0 ="touch "+OOOOOO0000OO0OO0O ;#line:68
    O0O0O00OOO000OOO0 =set ();#line:70
    os .system (O0O00O0O00000OOO0 );#line:72
    for O0OOO0O000OOO0000 in OOOO00OOOO0OOO0OO :#line:73
        OOO0O00O00OOO0OOO ="nm "+OO00O00O0OO00O0O0 +" >> "+OO00O00O0OO00O0O0 +".log";#line:74
        os .system (OOO0O00O00OOO0OOO );#line:75
    OOOO000OO0OOOOO00 =open (OOOOOO0000OO0OO0O );#line:77
    if OOOO000OO0OOOOO00 :#line:78
        OO0O0OOO0O0O0O0OO =OOOO000OO0OOOOO00 .read ()#line:79
        OO0O0OOO0O0O0O0OO =OO0O0OOO0O0O0O0OO .replace ("                 U _","");#line:80
        O00O0OOOO00O0O0OO =OO0O0OOO0O0O0O0OO .split ("\n")#line:81
        for OOO00O0O0O000O00O in O00O0OOOO00O0O0OO :#line:82
            for O0O0OOOOOO0O00O0O in OOOO00OOOO0OOO0OO :#line:83
                if OOO00O0O0O000O00O .find (O0O0OOOOOO0O00O0O )!=-1 :#line:84
                    O0O0O00OOO000OOO0 .add ("warning: "+O0O0OOOOOO0O00O0O )#line:85
        OOOO000OO0OOOOO00 .close ()#line:86
    if len (O0O0O00OOO000OOO0 )>0 :#line:88
        eprint ("application: %s"%OOO00O0OOOO00OO0O );#line:89
        O0000O00OOO0OOO0O =OO00O00O0OO00O0O0 .find (O00O00O00000O0O00 );#line:90
        eprint ("path: %s"%OO00O00O0OO00O0O0 [O0000O00OOO0OOO0O :]);#line:91
        eprint ("status: nopass");#line:92
        for OOO00O0O0O000O00O in O0O0O00OOO000OOO0 :#line:93
            eprint (OOO00O0O0O000O00O );#line:94
        eprint ("\r\n")#line:95
    else :#line:96
        eprint ("application: %s"%OOO00O0OOOO00OO0O );#line:97
        O0000O00OOO0OOO0O =OO00O00O0OO00O0O0 .find (O00O00O00000O0O00 );#line:98
        eprint ("path: %s"%OO00O00O0OO00O0O0 [O0000O00OOO0OOO0O :]);#line:99
        eprint ("status: pass");#line:100
    if os .path .exists (OOOOOO0000OO0OO0O ):#line:102
        os .system ("rm "+OOOOOO0000OO0OO0O )#line:103
def eprint (*OOOO00OOOOO0O00OO ,**O0000O0O0OOO0O0O0 ):#line:106
    print (*OOOO00OOOOO0O00OO ,file =sys .stderr ,**O0000O0O0OOO0O0O0 )#line:107
if __name__ =='__main__':#line:110
    if len (sys .argv )==1 :#line:111
        print ("usage: python ipv6_api_scan.py to_be_checked_dir")#line:112
        eprint ("usage: python ipv6_api_scan.py to_be_checked_dir >> out.log")#line:113
    else :#line:114
        scanFiles (sys .argv [1 ])#line:115

