#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Conversion des titres fasta par incrémentation
import sys
fiSource = sys.argv[1];
#fiDest = input("Nom du fichier destinataire : ");
fs = open(fiSource, 'r')
long=len(fiSource)
long =long-3
fiOut=fiSource[0:long]+".fasta"
fd = open(fiOut, 'w')

detect=0;
firstline=fs.readline();
flinelen=len(firstline);
secline=fs.readline();
slinelen=len(secline);
header=">"+secline[11:slinelen]+"|"+firstline[11:flinelen]
fd.write(header);

while 1:
    ch = fs.readline()                   # lecture d'une ligne
    if ch == "":
        break                            # fin du fichier, fermeture
    if  ch[0:5]== "ORIGIN":             #Detection du debut de la sequence
        detect=1
    if detect==1:                       
        fd.write(ch)
    fd.write(ch)                         # transcription de la séquence
fd.close()    
fs.close()



