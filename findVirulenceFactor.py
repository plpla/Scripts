#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante
#License:GPL

#this program is intended to be used as a comparaison tool after blasting multiple file against a Virulence
#factor DB. I believe it can also be used to compare any blast results if the same "small" DB is used to BLAST.
#Probably long to run.
#Blast file must be created with the -outfmt 6 option
#how to use this program:

#python findVirulenceFactor.py vfDB.fasta BlastFileList

#all file must be in the same folder
#I recommend (so not necessary) that you sort blast file by alignement length before launching this script:
#sort -k4 -nr BlastFile >sortedBlastFile
#This is just to make sure you obtain the longer alignment %id as a result.

import sys
###################################################################################################################
##Parameters that can be changed before use                                                                     ###
min_id=75.0		#minimal %id in blast file                                                                      ###
min_length_ratio=0.25		#minimal alignment length ratio (alignement length/ref seq length)                  ###
name=""		#something you want to search for in the factor title.	                                            ###
###################################################################################################################



class Factor(object):
	def __init__(self):
		self.name=""
		self.length=0
		self.listOfId=[]
	# def getName(self):
		# return self.name
	
	# def setName(self, name)
		# self.name=name
	
	# def getLength(self):
		# return self.length
	
	# def setLength(self, length):
		# self.length=length





#creation of a dictionnary of factors from the fasta file
#print("Creation of a dictionnary for virulence factor") #for debogue mode
factorDict={}
virulencedb=open(sys.argv[1], 'r')

i=0
line=virulencedb.readline()
while 1:
	if line=="":
		break
	elif line[0]==">" and name in line:
		factorDict[i]=Factor()
		factorDict[i].name=line[1:len(line)-1]
		long=0
		line=virulencedb.readline()
		while 1:
			if line=="" or line[0]==">":
				factorDict[i].length=long
				break
			else:
				long=long+len(line)-1
				line=virulencedb.readline()
		i+=1		
	else:
		line=virulencedb.readline()
	
virulencedb.close()


numberOfFile=0
for lines in open(sys.argv[2]):
	numberOfFile+=1

b=0	
while b<len(factorDict):
	a=0
	while a<numberOfFile:
		factorDict[b].listOfId.append(0)
		#print (str(factorDict[b].name)+str(factorDict[b].listOfId)) 
		a+=1
	b+=1

	
	
#print("Dictionnary is now created") 	#for debogue mode
#search for valid entry in each blast file of the BlastFileList
#this is the main step of the program.
fileList=[]
#print("start to read blast files")		#for debogue mode

for file in open(sys.argv[2]):
	
	file=file[0:len(file)-1]
	fileList.append(file)
	
	#lecture du fichier BLAST correspondant
	#print("reading "+file)		#for debogue mode
	blastFile=open(file,'r')
	while 1:
		ch=blastFile.readline()
		if ch=="":		#eof
			break
		if float(ch.split()[2])>min_id:		#première condition (save runtime)
			i=0
			#print("premiere pass")		#for debogue
			while i<len(factorDict):			#recherche du nom du subject dans le dict
				if (ch.split()[1] in factorDict[i].name) and ((float(ch.split()[3])/float(factorDict[i].length))>=min_length_ratio):
					factorDict[i].listOfId[len(fileList)-1]=ch.split()[2]
					#print(factorDict[i].name+factorDict[i].listOfId[-1])
					break
				else:
					i=i+1
		#end of the while reading a blast file
	blastFile.close()


#printing results to screen...
#print("start to print results")
i=0
header=""
header="Factor name"
for files in fileList:
	header=header+"\t"+files
print(header)
while i<len(factorDict):
	ligne=""
	ligne=factorDict[i].name
	a=0
	while a<len(fileList):
		ligne=ligne+"\t"+str(factorDict[i].listOfId[a])
		a=a+1
	print(ligne)
	i=i+1


			
					
		
		
				
				
				
				
				
				
				
				
				
