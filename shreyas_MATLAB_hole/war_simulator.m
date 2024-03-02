%% description
% This script simulates a game of war!
%
% Authors: ChatGPT and Shreyas Kousik, but mostly ChatGPT
% Created: 2 Mar 2023

%% setup
% Generate a deck of cards represented as integers between 1 and 52
deck = randperm(52);

% play warrrr
playWar(deck) ;

%% how many turns do games of war usually take?
n_trials = 10000 ;
n_turns = nan(1,n_trials) ;
parfor idx = 1:n_trials
    deck = randperm(52) ;
    n_turns(idx) = playWar(deck) ;
end

histogram(n_turns')
xlabel('Number of Turns to Win')
ylabel('Number of Games')
make_plot_pretty()

%% play war
function turnCounter = playWar(deck)
    % Split the deck between two players
    player1Deck = deck(1:2:26);
    player2Deck = deck(2:2:end);
    
    % Initialize turn counter
    turnCounter = 0;
    
    % Play the game
    while ~isempty(player1Deck) && ~isempty(player2Deck) && turnCounter < 1000
        % Increase turn counter
        turnCounter = turnCounter + 1;
        
        % Draw a card from each player's deck
        player1Card = player1Deck(1);
        player1Deck = player1Deck(2:end);
        
        player2Card = player2Deck(1);
        player2Deck = player2Deck(2:end);
        
        % Take modulo 13 of the card values
        player1CardValue = mod(player1Card - 1, 13) + 1;
        player2CardValue = mod(player2Card - 1, 13) + 1;
        
        % Determine the winner of this round
        if player1CardValue > player2CardValue
            player1Deck = [player1Deck, player1Card, player2Card];
        elseif player2CardValue > player1CardValue
            player2Deck = [player2Deck, player1Card, player2Card];
        else
            [player1Deck, player2Deck] = war(player1Deck, player2Deck);
        end
    end
    
    % % Determine the winner of the game
    % if isempty(player1Deck)
    %     fprintf('Player 2 wins the game in %d turns!\n', turnCounter);
    % elseif isempty(player2Deck)
    %     fprintf('Player 1 wins the game in %d turns!\n', turnCounter);
    % else
    %     fprintf('Game terminated early!')
    % end
end

%% helper functions
function [deck1, deck2] = war(deck1, deck2)
    % Check if there are enough cards for war
    if length(deck1) < 4 || length(deck2) < 4
        % If one of the players doesn't have enough cards, the game ends
        deck1 = [];
        deck2 = [];
        return;
    end
    
    % Draw 3 cards from each player's deck
    player1Cards = deck1(1:3);
    deck1 = deck1(4:end);
    
    player2Cards = deck2(1:3);
    deck2 = deck2(4:end);
    
    % Draw a fourth card from each player's deck
    player1Card = deck1(1);
    deck1 = deck1(2:end);
    
    player2Card = deck2(1);
    deck2 = deck2(2:end);
    
    % Take modulo 13 of the card values
    player1CardValue = mod(player1Card - 1, 13) + 1;
    player2CardValue = mod(player2Card - 1, 13) + 1;
    
    % Determine the winner of this war
    if player1CardValue > player2CardValue
        deck1 = [deck1, player1Cards, player2Cards, player1Card, player2Card];
    elseif player2CardValue > player1CardValue
        deck2 = [deck2, player1Cards, player2Cards, player1Card, player2Card];
    else
        [deck1, deck2] = war(deck1, deck2);
    end
end
