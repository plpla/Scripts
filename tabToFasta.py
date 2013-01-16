#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante


#the script would be better with fileOpen verification. It can still be used ....
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
	fasta=open(files+".fasta", 'w')
	fasta.write(">"+files+"\n")
	while 1:
		b=tab.readline()
		if b=="":
			fasta.write("\n")
			break
		elif b.split()[7]=='0':
			fasta.write('-')
		elif b.split()[7]=="Observed":
			continue
		elif b.split()[7]=='A' or b.split()[7]=='C' or b.split()[7]=='G' or b.split()[7]=='T' or b.split()[7]=='N': 
			fasta.write(b.split()[7])
		else:
			continue
		
	tab.close()
	fasta.close()

	
