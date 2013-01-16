#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante

import sys
a=1
while 1:
	try:		
		listeFichier[a-1]=fsys.argv[a]
		a=a+1
	except:
		break

nombreElementListe=len(listeFichier)
print('Name\tgene-start\tgene-end\tmodification-position\treference\tmodification\t
a=0
for ligneMain in open(listeFichier[a], open):
	ligneMain=ligneMain.split()
	positionModif=ligne[3]
	a=a+1
	for ligneSecond in open(listeFichier[a],open):
		if positionModif==ligneSecond.split()[3]:
			print(ligneMain[0]+'\t'+ligneMain[1]+'\t'+ligneMain[2]+'\t'+ligneMain[3]+'\t'+ligneMain[4]+'\t'+
			ligneMain[5]+'\t'+ligneSecond[5]+'\t'
	
	#to be finish or replaced by a perl script (F. Raymond)
