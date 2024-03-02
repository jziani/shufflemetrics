%% description

clear ; clc ;
%%
% Define the suits and ranks
suits = {'♠', '♦', '♥', '♣'};
ranks = {'2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'};

% Create a deck as paired cards
deck = {} ;
idx = 1 ;
for suit_idx = 1:length(suits)
    for rank_idx = 1:length(ranks)
        deck{idx} = [ranks{rank_idx},newline,suits{suit_idx}] ;
        idx = idx+1 ;
    end
end

%% permute the deck
% but the 2 of spades must come first
% shuffle = [1, randperm(51)+1] ;

% or load the best shuffle
% load('best_shuffle.mat')

deck = deck(shuffle) ;

% save('best_shuffle.mat','shuffle')

%%
% Create a figure
figure(1);
hold on;
axis equal;
axis tight;
axis off;

% Define parameters for card visualization
card_width = 1.1;
card_height = 1.75;
card_spacing = 0.2;
border_width = 1;
text_offset_x = 0.35;
text_offset_y = card_height/2;

% Loop through each card
for card_idx = 1:52
    % Calculate row and column index of the card
    row = ceil(card_idx / 13);
    col = mod(card_idx - 1, 13) + 1;
    
    % Calculate the position of the card
    x = (col - 1) * (card_width + card_spacing);
    y = (4 - row) * (card_height + card_spacing);
    
    % Draw the card as a rectangle
    rectangle('Position', [x, y, card_width, card_height], 'EdgeColor', 'black', 'LineWidth', border_width, 'FaceColor', 'white');
    
    % % Get the suit and rank of the card
    % suit = suits{mod(i - 1, 4) + 1};
    % rank = ranks{ceil(i / 4)};
    card_text = deck{card_idx} ;
    suit = card_text(end) ;
    
    % Set color of text based on suit
    if suit == '♥' || suit == '♦' % Hearts or Diamonds
        text_color = 'red';
    else
        text_color = 'black';
    end
    
    % Add the suit and rank inside the card
    text(x + text_offset_x, y + text_offset_y, card_text,...
        'FontSize', 15, 'Color', text_color, 'FontName', 'Arial Unicode MS');
    % text(x + text_offset_x, y + text_offset_y, suit,...
    %     'FontSize', 20, 'Color', text_color, 'FontName', 'Arial Unicode MS');
    % text(x + card_width/2, y + card_height - text_offset_y, rank,...
    %     'FontSize', 12, 'HorizontalAlignment', 'right', 'Color', text_color, 'FontName', 'Arial Unicode MS');
end

hold off;
