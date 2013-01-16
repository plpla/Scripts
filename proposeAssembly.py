#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante
#License: GPL

#This script is intended to propose assembly of contigs that have similarity on their extremities.
#Its objective is to complete the assembly made by Ray so that there is only one contig that contains
#the whole genome.

#The use of the script is :
#proposeAssembly.py Contigs-X Contigs Y- BlastXvsY.blastn length
#X and Y are Kmer lenght. The same length can be used. 
#The blast file must be produce with the -outfmt 6 option.
#The minimal length of the similarity (100% identity)

#You can ask the script to show the signification of the SimilarityCode by giving him the showSimilarityCode argument.
#ex: proposeAssembly.py showSimilaritycode


#There is no filter at the end to make sure the same similarity is not produce 
#2 times when using a Contigs.fasta file against itself
import sys

def showUsage():
	#Simplys show how to use the program
	print("The use of the script is : \n"+"proposeAssembly.py Contigs-X Contigs Y- BlastXvsY.blastn length \n"+
	"file X and Y are Contigs.fasta with the same or different KMER length. The same length can be used. \n"+
	"The blast file must be produce with the -outfmt 6 option. \n"+
	"The first file (X) must be the query and the second (y)the subject"+
	"The minimal length for similarity")
	print("You can ask the script to show the signification of the SimilarityCode by giving \n"+
	"him the showSimilarityCode argument.\nex: proposeAssembly.py showSimilarityCode")

def checkSimilarity(blastFileLine, length):
		#Function to check conditions for similarity. Not based on position.
		#Return TRUE if its possible.
		#Else return False
		if blastFileLine.split()[0] == blastFileLine.split()[1]:
			return 0
		elif float(blastFileLine.split()[2])<98.0:
			return 0
		elif int(blastFileLine.split()[3])<length:
			return 0
		else:
			return 1

def findContigLength(contig, file):
	#Return the length of a contig. If the contig is not in the file, return 0.
	#The file must be a Ray Contigs.fasta file.
	value=0
	for lines in open(file):
		if lines.split()[0]==(">"+contig):
			value=int(lines.split()[1])
			break
	return value

def checkFile(fileName):
	try:
		f1=open(fileName, "r")
		f1.close()
		return 1
	except:
		print("The file "+fileName+" can't be found")
		return 0



		
#MAIN		
detectShowSimilarityCode=0
try:
	if sys.argv[1]=="showSimilarityCode":
		print("code 1: \nquery            ------------>\n"+
						"subject  ----------->\n")
		print("code 2: \nquery            ------------>\n"+
						"subject   <----------\n")
		print("code 3: \nquery    ----------->\n"+
						"subject          ------------>\n")
		print("code 4: \nquery      ----------->\n"+
						"Subject           <----------\n")
		print("code 5: \nquery      ----------->\n"+
						"Subject  ----------------->\n")
		detectShowSimilarityCode=1
except:
	print("Welcome to the proposeAssembly program.")
if detectShowSimilarityCode==1:
	sys.exit()
	
if len(sys.argv)!=5:
	print("This program must be given 3 files in argument and 1 number")
	showUsage()
	sys.exit()
	
if (checkFile(sys.argv[1])==0 or checkFile(sys.argv[2])==0 or checkFile(sys.argv[3])==0):
	showUsage()
	sys.exit()


fresult=open(sys.argv[3]+"_proposeAssembly.out", "w")
fresult.write("query \t subject \t length \t qstart \t qend \t sstart \t send \t SimilarityCode\n")

	
for lines in open(sys.argv[3]):
	detectTrueSimilarity=0
	if checkSimilarity(lines, int(sys.argv[4])):
		longContig1=findContigLength(lines.split()[0], sys.argv[1])
		longContig2=findContigLength(lines.split()[1], sys.argv[2])
		qstart=int(lines.split()[6])
		qend=int(lines.split()[7])
		sstart=int(lines.split()[8])
		send=int(lines.split()[9])
		#5 cases are possible.
		#First: qstart=1 and send=longContig2
		#ex: query                  ---------------->
		#    subject       ----------->
		if qstart==1 and send==longContig2:
			detectTrueSimilarity=1
		#Second: qstart=1 and send=1
		#ex: query            ------------>
		#	subject   <----------
		if qstart==1 and send==1:
			detectTrueSimilarity=2
		#Third: qend=longContig1 and sstart=1
		#ex: query    ----------->
		#    subject         ------------>
		if qend==longContig1 and sstart==1:
			detectTrueSimilarity=3
		#Fourth: qend=longContig1 and send=longcontig2
		#ex: Query      ----------->
		#    Subject             <----------
		if qend==longContig1 and sstart==longContig2:
			detectTrueSimilarity=4
		#Fifth: qstart=1 qend=longContig1  (sstart>1 and send < longContig2) not sure
		#ex: Query           ---------->
		#    Subject     ------------------>
		if qstart==1 and qend==longContig1:
			detectSimilarity=5
			
		if detectTrueSimilarity !=0:
			fresult.write(lines.split()[0]+"\t"+lines.split()[1]+"\t"+lines.split()[3]+"\t"+
			lines.split()[6]+"\t"+lines.split()[7]+"\t"+lines.split()[8]+"\t"+lines.split()[9]+
			"\t"+str(detectTrueSimilarity)+"\n")

#end of the blast file read

fresult.close()	
			
	
	

	
	
	
	
	
	
	
	
	
	
	

