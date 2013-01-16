#! /usr/bin/env python
# -*- coding:Utf-8 -*-


#Script permettant de recevoir en entré un pipe de samtools view FILE.sorted.bam et
#de distribuer les reads selon la séquence sur laquel ils s'alignent.
#to be run once in a directory since result are made to be added to the same result file

import sys
fileInUse=''
for lines in sys.stdin:
	fileLine=lines.split()[2]
	if fileLine==fileInUse:
		file.write(lines)
	else:
		if fileInUse!='':
			file.close()
		fileInUse=fileLine
		file=open(fileInUse, 'a')
		file.write(lines)
file.close()
