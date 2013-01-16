#! /usr/bin/env python
# -*- coding:Utf-8 -*-

import sys
#currently in progress

fo=open(sys.argv[1])
try :
	ch1=int((fo.readline()).split()[0])
except:
	ch1=int((fo.readline()).split()[0])
while 1:
	ch3=fo.readline()
	if ch3=="":
		break
	ch2=int(ch3.split()[0])
	if (ch2-ch1)>5:
		print (str(ch1)+"\t"+str(ch2)+"\t"+str(ch2-ch1))
	ch1=ch2



	
	
	
	