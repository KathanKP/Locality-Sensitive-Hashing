The LargeMinhash.py python file runs the logic of LSH and MinHash as discussed. 
It takes as input various 'hashX.txt' files generated using the searchSpaceHasher.pl prolog file and saves the LSH buckets. 

Whenever a new search space comes in, it should be first hashed using the MinHash logic(use the same MinHash hashers that were used to 
generated the LSH buckets,so save them beforehand) and then put into buckets using the LSH idea. Similar documents are obtained by 
calling the getSimilar() function that takes as arguments the search space whose similar docs you need to find and the LSH bucekts 
that are picled and saved. For new spaces, the docs belonging to the buckets that the space was hashed too are the candidates for similar pairs.


