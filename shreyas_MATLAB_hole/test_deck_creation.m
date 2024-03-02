% create the first and final decks
D1 = 1:52 ; 
Df = 52:-1:1 ;

% create powers for hashing
T = 10.^(2.*Df - 1) ;

% make the BIG NUMBERS for min and max hash; these numbers are REALLY BIG,
% so we are going to represent them as strings until we really need them to
% be integers
mstr = numbersToString(D1)
Mstr = numbersToString(Df)



%% helpy bois
