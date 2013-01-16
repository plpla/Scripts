#! /usr/bin/env python
# -*- coding:Utf-8 -*-

import os, sys, urllib

url="http://www.ncbi.nlm.nih.gov/protein/ADN76215.1";
data = urllib.urlopen(url)
for lines in data:
	if ("<title>" in lines):
		print (lines);
		break
data.close();

	
input ("\n\nTappez sur une touche pour quitter!")

