#! /usr/bin/env python
# -*- coding:Utf-8 -*-
#Author: Pier-Luc Plante

import sys

for lines in sys.stdin:
	print(lines)
for line in open(sys.argv[1]):
	print(line)


print("done")