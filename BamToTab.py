#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante
#License:GPL

###########################
# This program is created to be part of SNPs detection pipeline.
# It is created to replace the original perl script by FR.
# Since i don't know Perl, it's easier to create my own version 
# and adapt it to my needs.
#
# Usage: samtools view file1.bam |python BamToTab.py Reference.fasta >file1.tab
#
###########################

import sys
from time import localtime, strftime


#Minimum value of coverage to pass from uncertain to Observed or Variant
cut_Off_Uncertainty=5
#Class created to be part of the dictionnary. Only an assembly of int, str and char.
class LineOfTab(object):
	position=0		
	numA=0
	numT=0
	numG=0
	numC=0
	total=0
	ref=''
	now=''
	type=""
	




################################################################################
### first step: calculate lenght of ref to create a dict of the good lenght. ###
################################################################################

#print("START TO IMPORT REF SEQ")	#for debogue
longOfSeq=0
seqRef=""
for lines in open(sys.argv[1]):
	if lines[0]!='>':
		longOfSeq=len(lines)-1+longOfSeq
		seqRef=seqRef+lines[0:len(lines)-1]
i=0
tabDict={}
while i<longOfSeq:
	tabDict[i]=LineOfTab()
	tabDict[i].position=i+1
	tabDict[i].ref=seqRef[i]
	i+=1

seqRef=""		#"free" seqRef memory? does it really work?

#print("Ref seg is now in memory!")	#for debogue
################################################################################
#### Second step: Read the input from samtools and put it in the dictionnary ###
################################################################################

#print("Start to read the input from stdin")
for lines in sys.stdin:		#read data from stdin one line at a time.
	#print("reading the first line") #for debogue
	l_startPosition=int(lines.split()[3])	
	l_cigar=lines.split()[5]
	l_quality=lines.split()[4]
	l_reads=lines.split()[9]
	
	###############################
	#### parse the cigar string ###
	###############################
	
	#is there an insertion or a deletion?
	isI=l_cigar.find("I")
	isD=l_cigar.find("D")
	if isI==-1 and isD==-1:
		isDorI=0	#there is not
	else:
		isDorI=1	#there is
	
	algnment_match=0
	soft_cliping=0
	#soft_cliping value and alignement match value
	if l_cigar.find("S")!=-1 and l_cigar.find("M")!=-1 and isDorI==0:	
		#there is 2 way the Cigar can be if there is a S in it:
		#63S151M or 123M32S (mid or end)
		#the solution is to determine where it compared to the M.
		#The same principle will be used for the next cigar parsing.
		#b is the "switch case like" value
		#case 63S151M
		if l_cigar.find("S")<l_cigar.find("M"):
			b=0
			soft_cliping=int(l_cigar.split("S")[0])
			alignment_match=int(l_cigar.split("S")[1].split("M")[0])
		#case 123M32S
		elif l_cigar.find("S")>l_cigar.find("M"):
			b=1
			alignment_match=int(l_cigar.split("M")[0])
			soft_cliping=int(l_cigar.split("M")[1].split("S")[0])
		else:
			algnment_match=0
			soft_cliping=0
			b=3 #error value: case 123M2S43M
	
	#alignement_match value only
	#case 151M		
	elif l_cigar.find("M")!=-1 and isDorI==0 and l_cigar.find("S")==-1:
		b=2
		alignment_match=int(l_cigar.split('M')[0])
		soft_cliping=0
	
	else:
		b=3
####################################################################################
#cases where there is an insertion or a deletion are not considered for the moment.#
#the implementation could be made in an other script or in this one ################
#(more difficult to implement)#######################################
###############################
	#######################
	#end of cigar parsing##
	#######################
	
	##########################################################
	# start to insert the read sequence in the dict #
	##########################################################
	longReads=len(l_reads)
	#print("longRead="+str(longReads)) #for debogue
	#print("start to copy the line sequence in the dict")	#for debogue
	if b==0: #case where 12S143M
		#print("entered the case 0")	#for debogue
		posInSeq=l_startPosition-1
		posInReads=soft_cliping
		while posInReads<longReads and posInSeq<longOfSeq:
			#print(posInReads)	#for debogue
			if l_reads[posInReads]=='A':
				tabDict[posInSeq].numA+=1
				tabDict[posInSeq].total+=1
			elif l_reads[posInReads]=='T':
				tabDict[posInSeq].numT+=1
				tabDict[posInSeq].total+=1
			elif l_reads[posInReads]=='G':
				tabDict[posInSeq].numG+=1
				tabDict[posInSeq].total+=1
			elif l_reads[posInReads]=='C':
				tabDict[posInSeq].numC+=1
				tabDict[posInSeq].total+=1
			posInSeq+=1
			posInReads+=1
	
	if b==1:	#case where 123M23S
		#print("entered the case 1")	#for debogue
		posInSeq=l_startPosition-1
		posInReads=0
		while posInReads<(len(l_reads)-soft_cliping) and posInSeq<longOfSeq:
			if l_reads[posInReads]=='A':
				tabDict[posInSeq].numA+=1
				tabDict[posInSeq].total+=1
			elif l_reads[posInReads]=='T':
				tabDict[posInSeq].numT+=1
				tabDict[posInSeq].total+=1
			elif l_reads[posInReads]=='G':
				tabDict[posInSeq].numG+=1
				tabDict[posInSeq].total+=1
			elif l_reads[posInReads]=='C':
				tabDict[posInSeq].numC+=1
				tabDict[posInSeq].total+=1	
			posInSeq+=1
			posInReads+=1
	
	if b==2:	#case where 143M
		#print("entered the case 2")	#for debogue
		posInSeq=l_startPosition-1
		posInReads=0
		while posInReads<len(l_reads) and posInSeq<longOfSeq:
			if l_reads[posInReads]=='A':
				tabDict[posInSeq].numA+=1
				tabDict[posInSeq].total+=1
			elif l_reads[posInReads]=='T':
				tabDict[posInSeq].numT+=1
				tabDict[posInSeq].total+=1
			elif l_reads[posInReads]=='G':
				tabDict[posInSeq].numG+=1
				tabDict[posInSeq].total+=1
			elif l_reads[posInReads]=='C':
				tabDict[posInSeq].numC+=1
				tabDict[posInSeq].total+=1
			posInSeq+=1
			posInReads+=1
	if b==3:
		errLog=open("BamToTabError.log", 'a')
		errLog.write(strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()))
		errLog.write(lines)
		errLog.close()
		continue	#The read is skipped and written into an error log
		
	######################################
	# end of reads insertion in the dict #
	######################################
	#print("Line sequence is now in the dict")	#for debogue
#################################################
# start of the dict completion (type and total) #
#################################################
i=0
#print("start of the dict completion")	#for debogue
while i < len(tabDict):
	tabDict[i].total=tabDict[i].numA+tabDict[i].numG+tabDict[i].numC+tabDict[i].numT
	#fill the total attribut
	if tabDict[i].total!=0:
		tabDict[i].numA=float(tabDict[i].numA/tabDict[i].total)
		tabDict[i].numT=float(tabDict[i].numT/tabDict[i].total)
		tabDict[i].numG=float(tabDict[i].numG/tabDict[i].total)
		tabDict[i].numC=float(tabDict[i].numC/tabDict[i].total)
	#fill the now attribut
	if tabDict[i].total==0:
		tabDict[i].now=tabDict[i].ref
	elif (tabDict[i].numA>tabDict[i].numT and tabDict[i].numA>tabDict[i].numG and 
	tabDict[i].numA>tabDict[i].numC and tabDict[i].total!=0):
		tabDict[i].now='A'
	elif (tabDict[i].numT>tabDict[i].numA and tabDict[i].numT>tabDict[i].numG and 
	tabDict[i].numT>tabDict[i].numC and tabDict[i].total!=0):
		tabDict[i].now='T'
	elif (tabDict[i].numC>tabDict[i].numT and tabDict[i].numC>tabDict[i].numG and 
	tabDict[i].numC>tabDict[i].numA and tabDict[i].total!=0):
		tabDict[i].now='C'
	elif (tabDict[i].numG>tabDict[i].numT and tabDict[i].numG>tabDict[i].numA and
	tabDict[i].numG>tabDict[i].numC and tabDict[i].total!=0):
		tabDict[i].now='G'
	#fill the type attribut
	if tabDict[i].total==0:
		tabDict[i].type="Reference"
	elif tabDict[i].total < cut_Off_Uncertainty and tabDict[i].ref==tabDict[i].now:
		tabDict[i].type="Reference low coverage"
	elif tabDict[i].total < cut_Off_Uncertainty and tabDict[i].ref!=tabDict[i].now:
		tabDict[i].type="Variant low coverage"
	elif tabDict[i].total >= cut_Off_Uncertainty and tabDict[i].ref==tabDict[i].now:
		tabDict[i].type="Observed"
	elif tabDict[i].total >= cut_Off_Uncertainty and tabDict[i].ref!=tabDict[i].now:
		tabDict[i].type="Variant"
	else:
		tabDict[i].type="Erreur"
	i+=1
	#print("position"+str(i-1)+" is completed in the dict")	#for debogue

##############################
# end of the dict completion #
##############################

#################
# print results##
#################

#print("start to print the results")	#for debogue
#position=0		
#numA=0
#numT=0
#numG=0
#numC=0
#total=0
#ref=''
#now=''
#type=""
i=0
print("Pos\tA\tT\tC\tG\tTotal\tReference\tNow\tType")
while i<len(tabDict):
	print(str(tabDict[i].position)+"\t"+str(tabDict[i].numA)+"\t"+str(tabDict[i].numT)+
	"\t"+str(tabDict[i].numG)+"\t"+str(tabDict[i].numC)+"\t"+str(tabDict[i].total)+
	"\t"+str(tabDict[i].ref)+"\t"+str(tabDict[i].now)+"\t"+str(tabDict[i].type))
	i+=1



	
	
	
	

