#! /usr/bin/env python
# -*- coding:Utf-8 -*-

#Create a fasta file with the unformated output of Primer3
import sys


#ex: PRIMER_LEFT_1_SEQUENCE
fo=open(sys.argv[1], 'r')
i=0
side=""
num=0
while 1:
	ch=fo.readline()
	if ch=="":
		break
	if ch[0]=="=":	#reset!
		i=0
		side=""
		num=0
	if ch.split("=")[0]=="SEQUENCE_ID":
		id=ch.split("=")[1]
	if ch.split("=")[0]=="PRIMER_LEFT_NUM_RETURNED" and ch.split("=")[1]!="0":
		num=int(ch.split("=")[1])
		side="PRIMER_LEFT_"
	if ch.split("=")[0]=="PRIMER_RIGHT_NUM_RETURNED" and ch.split("=")[1]!="0":
		num=int(ch.split("=")[1])
		side="PRIMER_RIGHT_"
	while i<num:
		ch=fo.readline()
		if ch.split("=")[0]==(side+str(i)+"_SEQUENCE"):
			print(">"+id[0:len(id)-1]+str(i))
			print(ch.split("=")[1])
			i=i+1
		if ch[0]=="=":
			print("ERREUR")
			i=0
			side=""
			num=0
			break
fo.close()	
		
		
		

