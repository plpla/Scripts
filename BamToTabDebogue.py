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
from math import max, min

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
	
def parseCigar(cigar):
	cigar2={}
	present=[]
	detectEndOfCigar=0
	i=0
	while 1:
		present=[]
		posM=cigar.find('M')
		posD=cigar.find('D')
		posS=cigar.find('S')
		posI=cigar.find('I')
		if cigar.find('M')!=-1:
			present.append(posM)
		if cigar.find('D')!=-1:
			present.append(posD)
		if cigar.find('S')!=-1:
			present.append(posS)
		if cigar.find('I')!=-1:
			present.append(posI)
		#print(present)
		closest=min(present)
		#print("Closest="+str(closest))
		if closest==posM:
			cigar2[i]=['M',cigar.split('M')[0]]
			if len(present)==1:
				detectEndOfCigar=1
			else:
				cigar=cigar.split('M')[1]
		elif closest==posD:
			cigar2[i]=['D',cigar.split('D')[0]]
			if len(present)==1:
				detectEndOfCigar=1
			else:
				cigar=cigar.split('D')[1]
		elif closest==posI:
			cigar2[i]=['I',cigar.split('I')[0]]
			if len(present)==1:
				detectEndOfCigar=1
			else:
				cigar=cigar.split('I')[1]
		elif closest==posS:
			cigar2[i]=['S',cigar.split('S')[0]]
			if len(present)==1:
				detectEndOfCigar=1
			else:
				cigar=cigar.split('S')[1]
		#print("detectEndCigar="+str(detectEndOfCigar))
		if detectEndOfCigar==1:
			break
		del(present[present.index(closest)])
		i+=1
	return cigar2


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

#print("Ref sequence is now in memory!")	#for debogue
################################################################################
#### Second step: Read the input from samtools and put it in the dictionnary ###
################################################################################

#print("Start to read the input from stdin")
for lines in sys.stdin:		#read data from stdin one line at a time.
	#print("reading the first line") #for debogue
	l_startPosition=int(lines.split()[3])	
	l_cigar=lines.split()[5]
	#l_quality=lines.split()[4]
	l_reads=lines.split()[9]
	
	###############################
	#### parse the cigar string ###
	###############################
	#print("Start to parse a cigar")
	
	parsedCigar=parseCigar(l_cigar)
	#print(parsedCigar)
	
	#print("This cigar parsing is done")
	#######################
	#end of cigar parsing##
	#######################
	
	##########################################################
	# start to insert the read sequence in the dict #
	##########################################################
	
	longReads=len(l_reads)
	#print("longRead="+str(longReads)) #for debogue
	#print("start to copy the line sequence in the dict")	#for debogue
	
	u=0
	posInSeq=l_startPosition-1
	posInReads=0
	while u < len(parsedCigar):
		if parsedCigar[u][0]=='M':
			value=int(parsedCigar[u][1])
			while posInReads<value and posInSeq<longOfSeq:
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
		elif parsedCigar[u][0]=='S':
			value=int(parsedCigar[u][1])
			posInReads=posInReads+value
		elif parsedCigar[u][0]=='D':
			value=int(parsedCigar[u][1])
			posInSeq=posInSeq+value		#we skip the nt that are deleted from the ref seq.
		elif parsedCigar[u][0]=='I':
			value=int(parsedCigar[u][1])
			posInReads=posInReads+value		#we skip the nt that are only in the read
		u+=1	
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
	if (max(tabDict[i].numA, tabDict[i].numT, tabDict[i].numG, tabDict[i].numC)==
		tabDict[i].numA):
		tabDict[i].now='A'
	if (max(tabDict[i].numA, tabDict[i].numT, tabDict[i].numG, tabDict[i].numC)==
		tabDict[i].numT):
		tabDict[i].now='T'
	if (max(tabDict[i].numA, tabDict[i].numT, tabDict[i].numG, tabDict[i].numC)==
		tabDict[i].numC):
		tabDict[i].now='C'
	if (max(tabDict[i].numA, tabDict[i].numT, tabDict[i].numG, tabDict[i].numC)==
		tabDict[i].numG):
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



	
	
	
	

