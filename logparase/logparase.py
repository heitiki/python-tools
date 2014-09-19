#!/usr/bin/python   
#coding=utf-8 
#creat by aring 
import sys 
import os 
import re 
import json   
path = os.getcwd() 
fsp = os.sep 
lsp = os.linesep 
def searchkey(cont,rf,s): 
    for knum in range(0,len(s.keys())): 
        rkey = s.keys()[knum]   
        for num in range(0,len(s[rkey])): 
            str = s[rkey][num] 
            if re.search(str,cont,re.I): 
                rstr= rkey + "----" + str + "-----" + cont 
                rf.write(rstr) 
                echostr="Find (%s) ------ key is (%s)" % (rkey,str) 
                print echostr 
def checklog(logname): 
    #open dict file 
    dpath = path + fsp + 'dict.json' 
    f = open(dpath) 
    jsondict = json.load(f) 
    f.close 
    #write result.txt 
    rpath = path + fsp + 'result.txt' 
    rfile = open(rpath,"w") 
    #open log file 
    logop = open(logname,"r") 
    print "-----Begin Match------" 
    for linecon in logop: 
        searchkey(linecon,rfile,jsondict) 
    logop.close() 
    rfile.close() 
    print "-----End Match And Write Result.txt File------" 
if __name__ == "__main__": 
    logfile = sys.argv[1] 
    if len(sys.argv) == 2: 
        #print filename 
        if os.path.exists(logfile): 
            print "-----Open Logfile------" 
            checklog(logfile) 
        else: 
            print"File Does Not Exist" 
    else: 
        print "Format Error"