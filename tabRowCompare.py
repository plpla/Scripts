#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante


# exemple d'utilisation: python tabRowCompare.py mismatch.tab 1 4 5 6
#where 1 is the ref sequence and 4-5-6 rows that are different then 1.
#mismatch.tab file was created from a perl script by FR.

import sys

rowRef=int(sys.argv[2])
i=3
listRow=[]
while i<len(sys.argv):
	listRow.append(int(sys.argv[i]))
	i=i+1
a=1
position=int(listRow[0])
for line in open(sys.argv[1]):
	if a in listRow or a==rowRef:
		print (line[0:len(line)-1])
	elif len(line.split()) > 2:    
	#2 is used because based on the exemple file i have the n first
	#lines of the mismatch.tab lines are in 2 columns. TB changed if needed. 
	#The minimum in tab is 3(position, ref, comp1)
		if line.split()[rowRef] != line.split()[position]:
			lineToPrint=line.split()[0]+"\t"+line.split()[rowRef]+"\t"
			for b in listRow:
				lineToPrint=lineToPrint+"\t"+line.split()[b]
			if ('0' in lineToPrint.split()):
				continue
			else:
				print(lineToPrint)
	a=a+1

	
		

	

