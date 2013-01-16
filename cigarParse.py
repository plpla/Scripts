import from math max, min
def parseCigar(cigar):
	cigar2={}
	present=[]
	detectEndOfCigar=0
	while 1:
		if cigar.find('M')!=-1:
			posM=cigar.find('M')
			present.append(posM)
		if cigar.find('D')!=-1:
			posD=cigar.find('D')
			present.append(posD)
		if cigar.find('S')!=-1:
			posD=cigar.find('S')
			present.append(posS)
		if cigar.find('I')!=-1:
			posD=cigar.find('I')
			present.append(posI)
		i=0
		closest=min(present)
		if closest=posM:
			cigar2[i]=['M',cigar.split('M')[0]]
			if len(cigar.split('M'))==1:
				detectEndOfCigar=1
			else:
				cigar=cigar.split('M')[1]
		elif closest=posD:
			cigar2[i]=['D',cigar.split('D')[0]]
			if len(cigar.split('D'))==1:
				detectEndOfCigar=1
			else:
				cigar=cigar.split('D')[1]
		elif closest=posI:
			cigar2[i]=['I',cigar.split('I')[0]]
			if len(cigar.split('I'))==1:
				detectEndOfCigar=1
			else:
				cigar=cigar.split('I')[1]
		elif closest=posS:
			cigar2[i]=['S',cigar.split('S')[0]]
			if len(cigar.split('S'))==1:
				detectEndOfCigar=1
			else:
				cigar=cigar.split('I')[1]
		if detectEndOfCigar==1:
			break