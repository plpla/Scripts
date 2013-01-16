#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante

#This script is to convert Fastq file to fasta

import sys

#there should be file opening verification
fs=open(sys.argv[1])

while 1:
    ch=fs.readline()
    if ch=="":
        break
    else:
        print (">"+ch[0:(len(ch)-1)])
        ch=fs.readline()
        print ch[0:(len(ch)-1)]
        ch=fs.readline()
        ch=fs.readline()

