The hashingClauses.pl folder basically generates the hash values using the getHash() function for clauses present in the 
'clausesX.pl' file and writes the results to a file named 'hashX.txt' which is further used for LSH and MinHash experiments.

The searchSpaceGen.pl files runs Alpeh for various positive examples of train to generate the raw search spaces as a 
text file named 'clauseX.txt' which is further cleaned and processed using the clauseExtractor.py python file.

The searchSpaceHasher takes the output of the clauseExtractor.py file which contains clauses like 
"east(A) :-   has_car(A,B), closed(B), has_car(A,C), double(C),    load(C,circle,1)." 
and hashes them using the hashing logic from hashingClauses.pl file.


