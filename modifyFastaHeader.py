#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Conversion des titres fasta par incrémentation
import sys
fiSource = sys.argv[1];
#fiDest = input("Nom du fichier destinataire : ");
fs = open(fiSource, 'r')
long=len(fiSource)
long =long-3
fiOut=fiSource[0:long]+"_mod.fasta"
fd = open(fiOut, 'w')
i=1
while 1:
    ch = fs.readline()                   # lecture d'une ligne
    if ch == "":
        break                            # fin du fichier, fermeture
    if  ch[0]== ">":             #Detection du debut de header
        fd.write(">"+str(i)+"\n")    #Ecriture du header sans le lcl|
	i=i+1
    else:                  
        fd.write(ch)     # transcription de la séquence
fd.close()    
fs.close()



