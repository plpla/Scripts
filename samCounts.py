#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Conversion des titres fasta par incrémentation
import sys;
fiwt = sys.argv[1];    #nom les identifiants répétés
fiko =sys.argv[2];    #nom du fichier contenant les identifiants uniques
wt = open(fiwt, 'r');
ko = open(fiko, 'r');

longwt=0;    #nbr de ligne dans le fichier
longko=0;
dicowt = {};    #dictionnaire du wild type
dicoko = {};    #dictionnaire du KO

#lecture du fichier WT
for line in open(fiwt):
    nom=line[0:(len(line)-1)];
    dicowt[nom]=0;
    dicoko[nom]=0;
    longwt=longwt+1;

#lecture du fichier KO
for line in open(fiko):
    nom=line[0:(len(line)-1)];
    dicowt[nom]=0;
    dicoko[nom]=0;
    longko=longko+1;

#Le nombre de ligne de chaque fichier est maintenant connu. Les dictionnaires sont
#identiques et contiennent tout les ID présents à une quantité de 0.
#Comptons maintenant le nombre d'occurance des ID pour KO et WT.

for line in open(fiwt):
    nom=line[0:(len(line)-1)];
    dicowt[nom]=dicowt[nom]+1;

for line in open(fiko):
    nom=line[0:(len(line)-1)];
    dicoko[nom]=dicoko[nom]+1;

#Creation des fichiers de comptage
comptewt=open(fiwt+".compte")
for clef, valeur in dicowt.items():
    comptewt.write(clef, valeur);
comptewt.close()

compteko=open(fiko+".compte")
for clef, valeur in dicoko.items():
    compteko.write(clef, valeur);
compteko.close();

#Analyse des éléments présents seulement dans un fichier ou dans l'autre et
#creation des fichiers uniqIn

uniquewt=open("uniqIn_"+fiwt[:4])
for clef in dicowt:
    if dicowt[clef]==0:
              uniquewt.write(clef)
uniquewt.close()
        
uniqueko=open("uniqIn_"+fiko[:4])
for clef in dicoko:
    if dicoko[clef]==0:
              uniqueko.write(clef);
uniqueko.close();

#Modification des quantité selon un facteur de correction du nombre de reads
#pour KO et WT. 2 nouveaux dico: dicocorrectko et dicocorrectwt.

dicocorrectko=dicoko.copy();
dicocorrectwt=dicowt.copy();
facteur=longko/longwt;
for clef in dicocorrectwt:
    dicocorrectwt[clef]=dicocorrectwt[clef]*facteur;

correctwt=open("corrected_"+fiwt[:4])
for clef in dicocorrectwt:
    correctwt.write(clef);
correctwt.close();
        
correctko=open("corrected_"+fiko[:4])
for clef in dicocorrectko:
    correctko.write(clef);
correctko.close();
               

#Analyse pour extraire les gènes dont l'expression est le double. Ecriture dans le fichier double_
#Celui ayant la plus grande valeur se trouvera dans son fichier.
#Un fichier commun est aussi créé               
double=open("double_"+fiko[:4]+fiwt[:4])
doublewt=open("double_"+fiwt[:4])
doubleko=open("double_"+fiko[:4]))
double.write("ID"+"\t"+"WT"+"\t"+"KO") 
for clef in dicocorrectwt:
    detect=0;
    if (dicocorrectwt[clef]*2 <= dicocorrectko[clef]):
        doubleko.write(clef+dicocorrectko[clef])
        detect=1
    elif (dicocorrectwt[clef] >=dicocorrectko[clef]*2):
        doublewt.write(clef+dicocorrectwt[clef])
        detect=1
    if (detect==1):
        double.write(clef+"\t"+dicocorrectwt[clef]+"\t"+dicocorrectko[clef])
double.close();
doublewt.close();
doubleko.close();

