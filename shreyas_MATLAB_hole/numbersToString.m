function result = numbersToString(numbers)
% THIS WAS WRITTEN BY CHAD GPT
    % Initialize an empty string
    result = '';
    
    % Loop through each number in the list
    for i = 1:length(numbers)
        % Convert the number to a string
        numStr = num2str(numbers(i));
        
        % If the number is between 1 and 9, prepend a 0
        if numbers(i) >= 1 && numbers(i) <= 9
            numStr = ['0', numStr];
        end
        
        % Concatenate the number string to the result string
        result = [result, numStr];
    end
end
