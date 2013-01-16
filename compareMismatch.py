#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante


#compare mismatch tab to eliminate mismatch that are also in the WT.

#compareMismatch.py wt.mismatch BIMS1.mismatch BIMS2.mismatch ...

import sys

nombreFichier=len(sys.argv)

i=2	#compteur des fichiers. Commence au deuxième fichier (premier bim)

while i<nombreFichier:
	resultfile=open(sys.argv[i]+".compareMismatch", 'w')
	for lines in open(sys.argv[i]):
		wtfile=open(sys.argv[1])
		while 1:
			wtline=wtfile.readline()
			#eof. The bim mismatch is not present in the wt mismatch file.
			if wtline=="":
				resultfile.write(lines)
				wtfile.close()
				break
			#mismatch in both file but observed value is different.
			if wtline.split()[0]==lines.split()[0] and wtline.split()[7] != lines.split()[7]:
				resultfile.write(lines)
				wtfile.close()
				break
			if wtline.split()[0]==lines.split()[0] and wtline.split()[7] == lines.split()[7]:
				wtfile.close()
				break
	resultfile.close()
	print(sys.argv[i]+" done")
	i=i+1	
			
			