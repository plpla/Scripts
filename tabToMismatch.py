#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante


#the script would be better with fileOpen verification. It can still be used ...
import sys

sampleList=open(sys.argv[1], 'r')
fileList=[]
while 1:
	a=sampleList.readline()
	if a=="":
		break
	else:
		fileList.append(a.split()[0])
sampleList.close()

for files in fileList:
	tab=open(files, 'r')
	mismatch=open(files+".mismatch", 'w')
	while 1:
		b=tab.readline()
		if b=="":
			break
		elif b.split()[6] != b.split()[7]:
			mismatch.write(b)
	tab.close()
	print(files+" done\n")
	mismatch.close()

	
