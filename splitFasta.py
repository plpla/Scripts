#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Conversion des titres fasta par incrémentation
import sys
fiSource = sys.argv[1];
#fiDest = input("Nom du fichier destinataire : ");
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
        fd=open(fiSource[o:long]+str(i)+".fasta", 'w')
        fd.write(ch)
    else:
        fd.write(ch)
  
fs.close()



