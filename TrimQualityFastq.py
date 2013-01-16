#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante

import sys

"""
This script is intended to remove the uncertain part of an Illumina read.
It will cut reads so they are of the specified length. It removes the end of a the reads because quality is lower.
Created because of low quality reads in a MiSeq run. Tada!!!
to use:
TrimQualityFastq.py file.fastq 150
"""

if len(sys.argv)!=3:
	print(__doc__);
	sys.exit(1);
long=int(sys.argv[2])

file=open(sys.argv[1], 'r');
while (1):
	title=file.readline();
	if title=="":
		break
	sequence=file.readline();
	signe=file.readline();
	quality=file.readline();
	print(title)
	print(sequence[0:long])
	print(signe)
	print(quality[0:long])
	

	