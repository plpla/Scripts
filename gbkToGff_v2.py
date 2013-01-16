#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante


# Conversion of fasta to GFF (minimal GFF format)
import sys
fiGbk = sys.argv[1];
fo=open(fiGbk, 'r')

while 1:
	ligne=fo.readline()
	if ligne== "":
		exit=2
		break    #eof
	elif 'LOCUS' in ligne.split():
		sligne=ligne.split()
		nom=sligne[1]
	elif 'FEATURES' in ligne:
		exit=1
		break;
	
if exit==1:
	fd= open(fiGbk+".gff", 'w')
	fd.write('##gff-version 3\n')
	ft=open('testfile','w')
	while 1:
		line=fo.readline()
		if ('gene' in line.split()) and '..' in line:
			ft.write(line)
			long=len(line)
			i=0
			premier=''
			deuxieme=''
			detect=0
			while (i<long):
				lettre=line[i]
				if (lettre.isdigit()) and (detect==0):
					premier=premier+str(lettre)
				elif (lettre=='.'):
					detect=1
				elif (lettre.isdigit()) and (detect==1):
					deuxieme=deuxieme+str(lettre)
				i=i+1
			if 'complement' in line:
				strand='-'
			else:
				strand='+'
			line=fo.readline()
			info=line.split()[0]
			fd.write(nom+'\t.\tgene\t'+premier+'\t'+deuxieme+'\t.\t'+strand+'\t.\t'+info+'\n')
		if line=="":
			fo.close()
			ft.close()
			fd.close()
			break
		
if exit==2:
	print('GBK format does not contain features. Make sure you use a standard gbk file.')

print('done')
