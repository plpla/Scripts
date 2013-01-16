#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante
#License:GPL

#this program allows to delete header lines in a multifasta file and concatenate fasta sequences in one long sequence.
import sys

fastaFile=open(sys.argv[1], 'r')
print(">"+str(sys.argv[1]))	#new long sequence header...

while 1:
	ch=fastaFile.readline()
	if ch=="":
		break
	elif ch[0]==">":
		continue
	else:
		print(ch[0:len(ch)-1])
	
