#! /usr/bin/env python
# -*- coding:Utf-8 -*-


#Script created to provide a valid input to Primer 3.
#The first input file is tsv. The second file is the fasta file containing the sequences.
#Conting	Way		Debut/Fin/AV/AP		Position(pour AP/AV)
#Contig-1000013	Reverse	Debut							
#Contig-1000013	Normal	Fin							
#contig-1000031	Reverse	AP	125						
#contig-1000031	Normal	AV	5410

import sys
fd=open(sys.argv[1]+".primer3", 'w')
for primers in open(sys.argv[1], 'r'):	#pour chaques lignes du fichier tsv avec la description des primers
	fd.write("SEQUENCE_ID="+primers.split()[0]+"_"+primers.split()[1]+"_"+primers.split()[2]+"\n")
	fd.write("SEQUENCE_TEMPLATE=")
	ch=open(sys.argv[2])
	detect=0
	while detect==0:		#Tranfert de la séquence
		lines=ch.readline()
		if lines=="":
			fd.write("ERREUR\n")
			break
		if (">"+primers.split()[0]) in lines.split():
			detect=1
			sequence=""
			while 1:
				lines=ch.readline()
				if lines=="":
					ch.close()
					break
				if lines[0]==">":
					ch.close()
					break
				else:
					sequence=sequence+lines[0:len(lines)-1]
	if 	primers.split()[2]=="Debut":
		fd.write(sequence[0:350]+"\n")
		fd.write("SEQUENCE_TARGET=1,25"+"\n")	#start at 1 for length 25
		fd.write("PRIMER_TASK=generic"+"\n")
		if primers.split()[1]=="Normal":
			fd.write("PRIMER_PICK_LEFT_PRIMER=1"+"\n")
			fd.write("PRIMER_PICK_INTERNAL_OLIGO=0"+"\n")
			fd.write("PRIMER_PICK_RIGHT_PRIMER=0"+"\n")
		if primers.split()[1]=="Reverse":
			fd.write("PRIMER_PICK_LEFT_PRIMER=0"+"\n")
			fd.write("PRIMER_PICK_INTERNAL_OLIGO=0"+"\n")
			fd.write("PRIMER_PICK_RIGHT_PRIMER=1"+"\n")
		fd.write("PRIMER_OPT_SIZE=21"+"\n")
		fd.write("PRIMER_MIN_SIZE=15"+"\n")
		fd.write("PRIMER_MAX_SIZE=30"+"\n")
		fd.write("PRIMER_MAX_NS_ACCEPTED=1"+"\n")
		fd.write("P3_FILE_FLAG=1"+"\n")
		fd.write("PRIMER_EXPLAIN_FLAG=1"+"\n")
		fd.write("="+"\n")
	if primers.split()[2]=="Fin":
		m_seq=sequence[(len(sequence)-350):(len(sequence))]
		fd.write(m_seq+"\n")
		fd.write("SEQUENCE_TARGET="+str(len(m_seq)-25)+",25\n")
		fd.write("PRIMER_TASK=generic"+"\n")
		if primers.split()[1]=="Normal":
			fd.write("PRIMER_PICK_LEFT_PRIMER=1"+"\n")
			fd.write("PRIMER_PICK_INTERNAL_OLIGO=0"+"\n")
			fd.write("PRIMER_PICK_RIGHT_PRIMER=0"+"\n")
		if primers.split()[1]=="Reverse":
			fd.write("PRIMER_PICK_LEFT_PRIMER=0"+"\n")
			fd.write("PRIMER_PICK_INTERNAL_OLIGO=0"+"\n")
			fd.write("PRIMER_PICK_RIGHT_PRIMER=1"+"\n")
		fd.write("PRIMER_OPT_SIZE=21"+"\n")
		fd.write("PRIMER_MIN_SIZE=15"+"\n")
		fd.write("PRIMER_MAX_SIZE=30"+"\n")
		fd.write("PRIMER_MAX_NS_ACCEPTED=1"+"\n")
		fd.write("P3_FILE_FLAG=1"+"\n")
		fd.write("PRIMER_EXPLAIN_FLAG=1"+"\n")
		fd.write("="+"\n")
	if primers.split()[2]=="AV":
		value=primers.split()[3]
		fd.write(sequence[len(sequence)-(int(value)+350):len(sequence)]+"\n")
		fd.write("SEQUENCE_TARGET="+value+","+str(len(sequence)-1)+"\n")	#start at 1 for length 100
		fd.write("PRIMER_TASK=generic"+"\n")
		if primers.split()[1]=="Normal":
			fd.write("PRIMER_PICK_LEFT_PRIMER=1"+"\n")
			fd.write("PRIMER_PICK_INTERNAL_OLIGO=0"+"\n")
			fd.write("PRIMER_PICK_RIGHT_PRIMER=0"+"\n")
		if primers.split()[1]=="Reverse":
			fd.write("PRIMER_PICK_LEFT_PRIMER=0"+"\n")
			fd.write("PRIMER_PICK_INTERNAL_OLIGO=0"+"\n")
			fd.write("PRIMER_PICK_RIGHT_PRIMER=1"+"\n")
		fd.write("PRIMER_OPT_SIZE=21"+"\n")
		fd.write("PRIMER_MIN_SIZE=15"+"\n")
		fd.write("PRIMER_MAX_SIZE=30"+"\n")
		fd.write("PRIMER_MAX_NS_ACCEPTED=1"+"\n")
		#long=len(sequence)-int(value)
		#fd.write("PRIMER_PRODUCT_SIZE_RANGE="+str(long)+"-"+str(long+50)+"\n")
		fd.write("P3_FILE_FLAG=1"+"\n")
		fd.write("PRIMER_EXPLAIN_FLAG=1"+"\n")
		fd.write("="+"\n")
	if primers.split()[2]=="AP":
		value=primers.split()[3]
		fd.write(sequence[0:int(value)+350]+"\n")
		fd.write("SEQUENCE_TARGET=1,"+value+"\n")	#start at 1 for length 100
		fd.write("PRIMER_TASK=generic"+"\n")
		if primers.split()[1]=="Normal":
			fd.write("PRIMER_PICK_LEFT_PRIMER=1"+"\n")
			fd.write("PRIMER_PICK_INTERNAL_OLIGO=0"+"\n")
			fd.write("PRIMER_PICK_RIGHT_PRIMER=0"+"\n")
		if primers.split()[1]=="Reverse":
			fd.write("PRIMER_PICK_LEFT_PRIMER=0"+"\n")
			fd.write("PRIMER_PICK_INTERNAL_OLIGO=0"+"\n")
			fd.write("PRIMER_PICK_RIGHT_PRIMER=1"+"\n")
		fd.write("PRIMER_OPT_SIZE=21"+"\n")
		fd.write("PRIMER_MIN_SIZE=15"+"\n")
		fd.write("PRIMER_MAX_SIZE=30"+"\n")
		fd.write("PRIMER_MAX_NS_ACCEPTED=1"+"\n")
		#fd.write("PRIMER_PRODUCT_SIZE_RANGE="+value+"-"+str(int(value)+50)+"\n")
		fd.write("P3_FILE_FLAG=1"+"\n")
		fd.write("PRIMER_EXPLAIN_FLAG=1"+"\n")
		fd.write("="+"\n")
	