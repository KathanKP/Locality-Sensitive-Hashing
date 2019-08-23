import numpy as numpy
import pandas as pd 
import re


for number in xrange(100):
	number=number+1
	print "Working on file ",number
	with open('space'+str(number)+'.txt','r') as clausefile:
		data=clausefile.read().replace('\n','')

	loc1=[m.start() for m in re.finditer('east\(A\)',data)]

	strings=[]
	for location in loc1:
		pos=location
		while(data[pos]!='.'):
			pos=pos+1
		strings.append(data[location:(pos+1)])

	newstrings=list(set(strings))
	newstrings.sort()

	with open('refinedSpaces/clauses'+str(number)+'.pl','w') as write:
		for item in newstrings:
			print>>write,item
