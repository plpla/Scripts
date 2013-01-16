#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante
#License: GPL

"""
This script provide automatic annotation for small genomes and contig.
An internet connection, blastx and a protein DB are required.
To use:
annotation1 ORF.gff sequence.fasta nameOfOutput.gk
You can modify some variable like the DB path at the top of the script.
We do not provide any guarantee on the quality of the results.
"""

db="/pubseq/genbank/nr-20120303/nr";
blastxOutFile="ORF.blastx";
blastxOutFileSorted="ORF.blastx.sorted"
#These step are necessary:
#1.1: extraire les ORF et les mettre dans un fichier fasta.
#1.2: blastx
#2: parse blast results
#3: load web page from ncbi or if no results seems ok, leave blank or write something like "NEED TO BE DONE MANUALLY"
#4: get title
#5: assign title and id to gene

import sys, urllib, os

#A custom class to facilitate the manipulation of the information.
class Gene(object):
	def __init__(self):
		ident="";
		note="";
		comment="";
		name="";
		length=0;
		pourcentageID=0;
		alignementLength=0;
		strand="";
		left=0;
		right=0;
	
if(len(sys.argv)!=4):
	print __doc__
	sys.exit(1)

listOfORF={};
#step 1: extract ORF and place them in a fasta file.
numberOfORF=0;
fasta=open("ORF.fasta",'w');
detect=0;
erreur=0;
tableauGene={}
for lines in open(sys.argv[1]):
	if("#" in lines.split() and "Length" in lines.split()):
		detect=1;
		print("start to read Genes")
	elif (detect==1):
		try:
			name=lines.split()[0];
			left=int(lines.split()[2]);
			right=int(lines.split()[3]);
			length=int(lines.split()[4]);
			strand=lines.split()[1];
			sequence=open(sys.argv[2]);			
			erreur=0;
			header=(">"+name+"|"+str(left)+"|"+str(right)+"\n");
			fasta.write(header);
			tableauGene[numberOfORF]=Gene();
			tableauGene[numberOfORF].name=name;
			tableauGene[numberOfORF].length=length;
			tableauGene[numberOfORF].strand=strand;
			tableauGene[numberOfORF].left=left;
			tableauGene[numberOfORF].right=right;
			tableauGene[numberOfORF].ident="";
			tableauGene[numberOfORF].note="";
			tableauGene[numberOfORF].comment="";
			tableauGene[numberOfORF].length=0;
			tableauGene[numberOfORF].pourcentageID=0;
			numberOfORF=numberOfORF+1;
		except:
			print("The following line of the .gff file has not been treated because of an unhandled character:")
			print(lines);
			print("The program will now contiue.")
			erreur=1;
		
		actualPos=0
		inSeq=0
		#print(lines.split()[0]+"\t"+lines.split()[2])
		#on va maintenant chercher la sequence dans le fasta. J'ai mis -1 dans les conditions
		#pour le caractere de fin de ligne.
		while (1 and erreur==0):
			ch=sequence.readline();
			#print(ch);
			if (ch==""):
				#print("Erreur");
				sequence.close();
				break;
			elif (ch[0]==">"):
				#print("Case >");
				continue;
			elif ((len(ch)-1+actualPos)<left and inSeq==0): #le égale va ici??
				actualPos=len(ch)+actualPos-1;
				#print("Actual Pos Increased"+"\t"+str(actualPos))
			elif ((len(ch)-1+actualPos)>=left and inSeq==0):
				ch=ch[left-actualPos-1:];
				actualPos=left;
				#print("in the seq!");
				inSeq=1;
				fasta.write(ch);
				actualPos=actualPos+len(ch)-2;
			elif (inSeq==1):
				if(len(ch)-1+actualPos<=right):
					actualPos=actualPos+len(ch)-1;
					fasta.write(ch);
				elif(len(ch)-1+actualPos>right):
					ch=ch[0:right-actualPos]+"\n";
					fasta.write(ch);
					sequence.close();
					#print("fin")
					break;
		
fasta.close();

#step 2: BLASTX!!!! probably the longest step...multithread!
command="time blastx -query ORF.fasta -db "+db+" -outfmt 6 -query_gencode 11 -num_threads 10 >"+blastxOutFile;
print("The folowing command is now executed by the system. Its long...");
print(command);
os.system(command);
print("Done");
del command;


#step 3: parse blast results
#sort -k1n -k3nr -k4nr blastxOutFile
print("Now sorting the blast output")
command2="sort -k1n -k3nr -k4nr "+blastxOutFile+" >"+blastxOutFileSorted;
os.system(command2);
print("Done");
del command2;

#step 4
#For each ORF, we must find a name and a corresponding sequence.
#That's the part where we use the internet connection because we search the information on the NCBI WebSite.
#For this, we use the blastx output file and we consider that it is parsed correcltly (most relevant result first)
print("Now getting information from the NCI website")
currentPos=0;
fileBlastx=open(blastxOutFile, 'r')
lines=fileBlastx.readline();
while (1):
	if(lines==""):
		break
	currentPos=int((lines.split()[0]).split("|")[0])-1; 	#minus 1 to acces the good position in the table;
	if(float(lines.split()[2])>50.00):	#The id% must be more than 50%. 
		tableauGene[currentPos].pourcentageID=float(lines.split()[2]);
		if (float(lines.split()[3])>(tableauGene[currentPos].length*0.5/3)): 	#The length ratio must be over 50%.
			tableauGene[currentPos].alignementLength=float(lines.split()[3]);
			try:
				entryNumber=(lines.split()[1]).split('|')[3];
				url="http://www.ncbi.nlm.nih.gov/protein/"+entryNumber;
				webPage=urllib.urlopen(url);
			except:
				entryNumber="NEED TO BE DONE MANUALLY";
		else:
			entryNumber="NEED TO BE DONE MANUALLY";
		tableauGene[currentPos].ident=entryNumber;
		if(webPage.readline()!="" or entryNumber!="NEED TO BE DONE MANUALLY"):
			for lines in webPage:
				if ("<title>" in lines):
					tableauGene[currentPos].name=(lines.split(">")[1]).split("]")[0]+"]";
					break;
			#enf of for...
		#end of if...
	while(1):
		lines=fileBlastx.readline();
		if (lines=="" or (int((lines.split()[0]).split("|")[0])!=currentPos+1)):
			break
	#end of while.
#end of while.
#It is now time to create the .gbk file!

print("done")

print("Now sending information to the output file")
gbk=open(sys.argv[3], 'w')

for entry in tableauGene:
	line="FT"+"   "+"gene"+"            ";
	if tableauGene[entry].strand=="-":
		line=line+"complement""("+str(tableauGene[entry].left)+".."+str(tableauGene[entry].right)+")"+"\n";
	else:
		line=line+str(tableauGene[entry].left)+".."+str(tableauGene[entry].right)+"\n"
	gbk.write(line);
	line="FT"+"                   "+"/note="+tableauGene[entry].name+"\n";
	gbk.write(line);
	line="FT"+"                   "+'''/id="'''+tableauGene[entry].ident+'''"'''+"\n";
	gbk.write(line);
	line="FT"+"                   "+'''/comment="'''+str(tableauGene[entry].pourcentageID)+'''"'''+"\n";
	gbk.write(line);
gbk.close();
print("Annotation is finished, I recommand you to verify all the results.")
print("Have a good day!")












