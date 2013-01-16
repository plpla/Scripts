#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante
#License: GPL

# Divise un multi-fasta en simple-fasta en utilisant le header comme nom de fichier
import sys
fiSource = sys.argv[1];
fs = open(fiSource, 'r')
long=len(fiSource)
long =long-3
fd = open("temp", 'w')

detect=0;
i=0

while 1:
    ch = fs.readline()                   # lecture d'une ligne
    if ch == "":
        break                            # fin du fichier, fermeture
		
    elif  ch[0]== ">":             #Detection du debut de la sequence
        i=i+1
        fd.close()
        csplit=ch.split()[0]
        fd=open(csplit[1:]+".fasta", 'w')
        fd.write(ch)
    else:
        fd.write(ch)
		
fd.close()
fs.close()



