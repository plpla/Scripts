#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys


fichier=open(sys.argv[1], 'r')
ch=fichier.readline();
total=0;
nbrligne=0;
while (1):
	ch=fichier.readline();
	if (ch==""):
		break;
	if (ch.split()[5]!=0):
		nbrligne=nbrligne+1;
		total=total+int(ch.split()[5]);
print("total="+ str(total));
print("longueur="+str(nbrligne));
print("Coverage="+str(total/nbrligne));
		

