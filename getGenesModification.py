#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante


#Utilisation: getGenesModification.py file.vcf file.gff qualityValue(default=0)
#Exemple: getGenesModification.py myFile1.vcf myFile2.gff 100 >getGenesModif.out
import sys
fvcf=open(sys.argv[1], 'r')
exit=0
#read vcf file to usefull part
while 1:
	ligneVCF=fvcf.readline()
	if ligneVCF=="":  #eof
		print('VCF file does not fit original model')
		fvcf.close()
		sys.exit()
	if ('#CHROM'==ligneVCF.split()[0] and 'POS'==ligneVCF.split()[1] and 
		'ID'==ligneVCF.split()[2] and 'REF'==ligneVCF.split()[3] and 
		'ALT'==ligneVCF.split()[4] and 'QUAL'==ligneVCF.split()[5]):
		break

#read gff file
fgff=open(sys.argv[2], 'r')
ligneGFF=fgff.readline()
if '##gff' in ligneGFF:
	ligneGFF=fgff.readline()
	if len(ligneGFF.split())==9 and ligneGFF.split()[3].isdigit() and ligneGFF.split()[4].isdigit():
		fgff.close()
		exit=0
	else:
		exit=1
else:
	exit=1
if exit==1:
	print('GFF file is not a standard GFF format')
	fgff.close()
	fvcf.close()
	sys.exit()

#Assignation de la cutoff value. Valeur par défaut: 0
if len(sys.argv)==3:
	qualityCutoff=0
elif (sys.argv[3].isdigit()):
	qualityCutoff=sys.argv[3]
else:
	print('quality cutoff is not defined correctly')
	sys.exit()

print('Name\tgene start\tgene end\tmodification position\treference\tmodification\tQuality\tVCFinfo')	
while 1:
	ligneVCF=fvcf.readline()
	
	if ligneVCF=="":
		fvcf.close()
		break
	splitVCF=ligneVCF.split()
	
	for line in open(sys.argv[2]):
		splitGFF=line.split()
		if len(splitGFF)==9:
			position=splitVCF[1]
			genes=splitGFF[3]
			genee=splitGFF[4]
			quality=splitVCF[5]
		if ((len(splitGFF)==9) and (int(position)>=int(genes)) and (int(position)<=int(genee)) and (float(quality)>=float(qualityCutoff))):
			#Name, start, end, position, reference, modification, Quality, VCFinfo 
			print(splitVCF[0]+'\t'+splitGFF[3]+'\t'+splitGFF[4]+'\t'+splitVCF[1]+'\t'+splitVCF[3]+'\t'+
			splitVCF[4]+'\t'+splitVCF[5]+'\t'+splitVCF[7])
			break
		elif (len(splitGFF)==9 and int(genes)>int(position)):
			break

#fin du script
		

	
		
	
	
	
	
	
	
	
	
	