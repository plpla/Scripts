#! /usr/bin/env python
# -*- coding:Utf-8 -*-

import sys
fiSearch = sys.argv[1];
fiDict=sys.argv[2];

for lines in open(fiSearch):
	if lines=="":
		break
	fd=open(fiDict, 'r')
	detect=0
	while 1:
		ch=fd.readline()
		if lines.split()[0] in ch.split() and detect==0:
			long=len(ch)
			print ch[0:long-1]
			detect=1
		elif '>' in ch and detect==1:
			break
		elif detect==1 and ch=="":
			break
		elif detect==1:
			long=len(ch)
			print ch[0:long-1]
		elif ch=="":
			break
	fd.close()

		
		
			