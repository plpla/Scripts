#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante

#This script compare the values contained in a row of a tab file and determine if this position
#is considered as in a gene based on a gff file (use gbkToGff.py to generate gff if needed).
#If the position is in a gene, it prints the corresponding line, gene start, gene end 

#Utilisation:
#python isPositionInGene.py file1.tab file2.gff 1
#where 1 is the row number in the tab file where the positions are(starting with 1) 

import sys
tabFile=open(sys.argv[1], 'r')
ligne=tabFile.readline()
print (ligne[0:len(ligne)-1]+"\tgene start\tgene end\tgene product")
tabFile.close()

for tabLine in open(sys.argv[1]):
	try:
		no=int(tabLine.split()[0])
		a=0
		for refLine in open(sys.argv[2]):
			if a==1 and no>=int(refLine.split()[3]) and no<=int(refLine.split()[4]):
				print (tabLine[0:len(tabLine)-1]+ "\t"+ refLine.split()[3]+ "\t"+ refLine.split()[4]+
				"\t"+(refLine.split()[8]).split("=")[1])
			a=1	#to skip the first line of the gff file.
	except:
		continue
		