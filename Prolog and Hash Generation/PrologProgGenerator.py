# with open ('searchSpaceGen.pl','w') as myfile:
# 	print>>myfile,":-[aleph6]."
# 	print>>myfile,":-read_all(train)."
# 	for i in xrange(100):
# 		string=":-sat("+str(i+1)+"),tell('space"+str(i+1)+".txt'),reduce,told."
# 		print>>myfile,string

with open ('searchSpaceHasher.pl','w') as myfile:
	print>>myfile,":-[hashingClauses]."
	for i in xrange(100):
		string=":-[clauses"+str(i+1)+"]."
		print>>myfile,string
		string=":-see('clauses"+str(i+1)+".pl'),read(X),term_string(X,S),split_string(S,':-',"+"' '"+",L),L=[H|T],term_string(Term,H),numbervars(Term,0,End),open('hash"+str(i+1)+".txt',write,Stream),forall(getHash(Term,Hash),(write(Stream,Hash),write(Stream,' '))),close(Stream),seen()."		
		print>>myfile,string
		string=":-unload_file('clauses"+str(i+1)+".pl')."
		print>>myfile,string