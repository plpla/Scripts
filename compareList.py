#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante
#License:GPL

"""
This script compare 2 list of entry and output a list of the ones that are only in the second file
How to use:
python compareList file1 file2
"""

import sys

if len(sys.argv) != 3:
	print(__doc__)
	sys.exit(1);	
list1=[];
print("Debut de la cr�ation de la liste de r�f�rence")
for i in open(sys.argv[1]):
	list1.append(i)
print("Fin de la cr�ation de la liste de r�f�rence")
a=0
for entry in open(sys.argv[2]):
	if entry in list1:
		continue
	else:
		print(entry)
	

			
	

