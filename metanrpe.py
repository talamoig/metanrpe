#!/bin/env python

import re
from os import listdir
from os.path import isfile, join

checklinere="command\[(.*)\]=.*"
includere="include=(.*)"
includedirre="include_dir=(.*)"

checkpattern=re.compile(checklinere)
includepattern=re.compile(includere)
includedirpattern=re.compile(includedirre)

files=["/etc/nagios/nrpe.cfg"]

def getwithpattern(fname,pattern):
    checks=[]
    with open(fname) as f:
        lines = f.readlines()
        for l in lines:
            m=pattern.match(l)
            if m:
                checks.append(m.group(1))
    return checks


def getchecks(fname):
    global checkpattern
    return getwithpattern(fname,checkpattern)

def getincludes(fname):
    global includepattern
    return getwithpattern(fname,includepattern)

def getincludedirs(fname):
    global includedirpattern
    return getwithpattern(fname,includedirpattern)

checklist=[]
while len(files)>0:
    f=files.pop()
    checks=getchecks(f)
    for c in checks:
        checklist.append(c)
    dirs=getincludedirs(f)
    for d in dirs:
        for filename in listdir(d):
            if isfile(join(d,filename)):
                files.append(join(d,filename))
    for includefile in getincludes(f):
        files.append(includefile)

checklist=set(checklist)
for c in checklist:
    print c
