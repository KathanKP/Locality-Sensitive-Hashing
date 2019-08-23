# Locality-Sensitive-Hashing
Showing MinHash as as unbiased estimator of Jaccard Similarity and use LSH to hash search spaces. 

The first task was to implement a simple Locality Sensitive Hashing model that used MinHash and use it to show MinHash as an unbiased estimator of Jaccard Similarity. All the code is contained in the LSH folder for this part. 
1) LSH.py is a basic implementation of Minhashing and Locality Sensitive Hashing to calculate possible candidate pairs.
2) LSH_2.py extend LSH.py by calculating Minhash Jaccard values for various sizes of items and varying true Jaccard similarity. 

Results are displayed as a matrix with rows being array sizes and columns being true Jaccard values. (Yes/No) in each box indicates if the two arrays are seen as a candidate pair by the LSH algorithm. Results can be seen in the report.

The next part was to generate search spaces for the Michalskis Train Problem as defined in https://slidewiki.org/deck/1030-1/michalskis-train-problem/slide/8650-2/8650-2:2/view, hash them and then use LSH to find similar search spaces. Aleph, an Inductive Logic Progamming system (read more at https://www.cs.ox.ac.uk/activities/programinduction/Aleph/aleph.html) has been used to generate the search spaces. All code for this is in the Prolog and Hash Generation Folder. Pardon for the messy state. I'm working to improve it. 

The basic workflow is something like this:
1) searchSpaceGen.pl is used to generate 100 search spaces using Aleph and stores the clauses in clausesX.txt where X is the search space number from 1-100.
2) clauseExtractor.py reads these clauses and pre-processed them and writes them to a clauseX.pl file so that the prolog hasher can read it.
3) getHash() function in hashingClauses.pl is used to generate the hashes in hashX.txt folder in the searchSpaceHasher.pl program for all 100 search spaces.
4) LargerMinhash.py runs he LSH and MinHash logic as discussed in the previous section.

Please feel free to reach out in case of any queries or bugs or any other issue. I would be happy to help. 
