#! /usr/bin/env python
# -*- coding:Utf-8 -*-


#to parse a blast result (one file against himself)

import sys

fo=open(sys.argv[1], 'r')

while 1:
	ch=fo.readline()
	if ch=="":
		break
	if ch.split()[0]==ch.split()[1]:
		continue
	if ch.split()[2]!="100.00":
		continue
	else:
		print(ch[0:len(ch)-1])
