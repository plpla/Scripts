#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Conversion des titres fasta par incrémentation
import sys
fiSearch = sys.argv[1];
fiDict=sys.argv[2];
fd= open(fiSearch+"-result", 'w')

detect=0;

for line in open(fiSearch):
    line = line[0:(len(line)-2)]
    #print("long line mod1=")
    #print(len(line))
    print(line)
    if line == "":
        break                            # fin du fichier, fermeture
    else:             #Recherche de la séquence
	long=len(line)
        #print("val long")
        #print(long)
        ff=open(fiDict, 'r')
	while 1:
	    ligne=ff.readline()
	    if detect==0 and ligne == "":
                print("fin du fichier atteint sans rien trouver")
	        fe=open("error.log", 'a')
                fe.write(fiSearch)
                fe.write(line)
                fe.write("not found")
                ff.close()
	        fe.close()
		break
	    if detect==1 and ligne[0]!=">":
	        fd.write(ligne)
	    if detect==1 and ligne[0]==">":
                print("atteint la fin de la sequence")
	        ff.close()
	        detect=0
	        break
	    if detect==1 and ligne == "":
                print("atteint la fin de la sequence par la fin du fichier")
	        ff.close()
	        detect=0
	        break
	    if ligne [1:(long+1)]==line:
                print("header trouve")
	        fd.write(ligne)
	        detect=1
            #if ligne[0]==">":
            #    print("len ligne")
		#print(len(ligne [1:(long+1)]))                
fd.close()




