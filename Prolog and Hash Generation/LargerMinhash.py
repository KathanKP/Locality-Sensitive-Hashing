from __future__ import division
import pandas as pd  
import numpy as np  
from random import randint
import sys
import gc
import pickle
import time

# Generate pairs of random numbers that act as seeds for the minhash functions
def generateMinHashSeeds(noOfSeeds):
	seeds=[]
	unique_seeds=set()
	i=0
	while i<noOfSeeds:
		i=i+1
		a=randint(0,100000)
		b=randint(0,100000)
		seed_hash=hash((a,b))
		if seed_hash not in unique_seeds:
			unique_seeds.add((a,b))
			seeds.append((a,b))
		else:
			i=i-1

	return seeds

# Generate the hash value of a given data item based on the two seed values of a minhash function
def getHash(data,seedone,seedtwo):
	hash_val=17
	hash_val=hash_val*37^hash(seedone)
	hash_val=hash_val*37^hash(seedtwo)
	hash_val=hash_val*37^hash(data)
	return hash_val

def getMinHash(data):
	current_minhash=np.full((1,no_seeds),sys.maxsize,dtype="int64")
	for token in set(data):
		for hash_function in xrange(no_seeds):
			currentHash=getHash(token,seeds[hash_function][0],seeds[hash_function][1])
			if currentHash<current_minhash[0][hash_function]:
				current_minhash[0][hash_function]=currentHash

	return current_minhash

def getSimilar(number,lshbuckets):
	similar_docs=[]
	for bucket in lshbuckets:
		for key,value in bucket.items():
			if number in value:
				print value
				for matches in value:
					print matches
					#similar_docs.append(matches)
				break

	unique_docs=set(similar_docs)
	return unique_docs


# FOR MINHASH AND LSH
no_seeds=100
seeds=generateMinHashSeeds(no_seeds)
no_of_spaces=100

start_time=time.time()
# Create a matrix of size 1000*100 and fill it with max size elements.
minhash=np.full((no_of_spaces,no_seeds),sys.maxsize,dtype="int64")

# Read in each file one by one,calculate its minhash and store it in the created minhash matrix.
for i in xrange(no_of_spaces):
	print "Working on"+str(i+1)
	with open('hash'+str(i+1)+'.txt','r') as myfile:
		data=myfile.read().replace('\n','').split(' ')
		data=data[:len(data)-1]
		data=map(int,data)

		minhashes=getMinHash(data)
		minhash[i,:]=minhashes
print "MinHashing took"+str(time.time()-start_time)+" seconds"

per_band=20
num_bands=no_seeds/per_band

c=1000000007
a=randint(1,c-1)		
b=randint(1,c-1)
lsh_buckets=[]
for i in xrange(num_bands):
	current_bucket={}
	for j in xrange(no_of_spaces):
		hashVal=long(0)
		for k in xrange(i*per_band,(i+1)*per_band):
			hashVal=hashVal+(((minhash[j][k]*a)+b)%c)
		if hashVal not in current_bucket:
			current_bucket[hashVal]=[]
		current_bucket[hashVal].append(j)
	lsh_buckets.append(current_bucket)
	del current_bucket
	gc.collect()

print "MinHashing and LSH took"+str(time.time()-start_time)+" seconds"

#Saving the lsh buckets
with open('lshbuckets.txt','wb') as myfile:
	pickle.dump(lsh_buckets,myfile)

# Readin the lsh buckets
with open('lshbuckets.txt','rb') as myfile:
	lsh_buckets=pickle.load(myfile)
docs=getSimilar(5,lsh_buckets)
print docs


### FOR TRUE JACCARD CALCULATION
dataset=[]
start_time=time.time()
print "Brute Force Jaccard Calclation"
for i in xrange(100):
	with open('hash'+str(i+1)+'.txt','r') as myfile:
		data=myfile.read().replace('\n','').split(' ')
		data=data[:len(data)-1]
		data=map(int,data)

		dataset.append(data)

n=100
jaccard_actual=np.full((n,n),0.0)
for i in xrange(n):
	for j in xrange(i+1,n):
		jaccard_actual[i][j]=len(set(dataset[i])&set(dataset[j]))/len(set(dataset[i])|set(dataset[j]))

print 'BF Jaccard took '+str((time.time()-start_time))+ "seconds"