#! /usr/bin/env python
# -*- coding:Utf-8 -*-


#To change Abyss fasta header to Ray (standard) fasta header. Contigs numbers are based on incrementation.
#Created to use proposeAssembly.py (GPL, Pier-Luc Plante).

import sys
i=1
for lines in open(sys.argv[1]):
	if lines=="":
		break
	if lines[0]=='>':
		print (">contig-"+str(i)+" "+lines.split()[1]+" nucleotides")
		i=i+1
	else:
		print(lines[0:len(lines)-1])
