% Sample examples to test out various ideas
% Facts
father(harin,kathan).
father(gautam,harin).
father(harin,kat).
wife(panna,gautam).
mother(panna,harin).
mother(ushma,kathan).
mother(ushma,kat).
male(kathan).
male(kat).
female(ushma).


% Rules
gf(X,Y):-father(X,Z),father(Z,Y).
gf(X,Y):-father(X,Y).
gf1(Z,W):-father(Z,A),father(A,W).
gm(X,Y):-wife(X,Z),gf(Z,Y).
gm1(X,Y):-mother(X,Z),father(Z,Y).
gm2(X,Y):-father(Z,Y),mother(X,Z).
brothers(X,Y):-male(X),male(Y),father(Z,Y),father(Z,X),X\=Y.
parent(X,Y):-father(X,Y);
                mother(X,Y).
siblings(X,Y):-parent(Z,X),parent(Z,Y).
happy(X):-male(X).
energetic(X):-female(X).

%------------------------------ Practice Ends-----------


get_clause_body(Clause, Body) :-
    clause(Clause, Elements),
    clause_body_list_rec(Elements, Body).

clause_body_list_rec(Elements,[BodyPart|BodyRest]) :-
    (not(Elements =(A,B))
    ->  BodyPart = Elements,
    BodyRest = []
    ; Elements=..[_,E|T],
    BodyPart=E,
    [ClauseRest]=T,
    clause_body_list_rec(ClauseRest,BodyRest)
    ).

getHash(Clause,Hash):-get_clause_body(Clause,Body),sort(Body,Sorted),numbervars(Sorted,0,End),term_hash(Sorted,Hash).

% Have to read the text file containing the clauses so getHash() can backtrack.
% see(filename),also load that file in prolog.
%  read(X),term_string(X,S),split_string(S,":-","",L),L=[H|T],term_string(Term,H),
%  numbervars(Term,0,End),findall(Hash,getHash(Term,Hash),List).