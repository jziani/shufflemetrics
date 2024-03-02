function formatted_str = addCommas(long_number_str)
    % Remove any commas from the input string
    long_number_str = strrep(long_number_str, ',', '');
    
    % Calculate the length of the input string
    len = length(long_number_str);
    
    % Determine the number of groups of three digits
    num_commas = floor((len-1) / 3);
    
    % Initialize the formatted string with the first group of digits
    formatted_str = long_number_str(1:mod(len, 3));
    
    % Iterate through the remaining groups of digits
    for i = 1:num_commas
        start_idx = mod(len, 3) + 3*(i-1) + 1;
        end_idx = start_idx + 2;
        formatted_str = [formatted_str, ',', long_number_str(start_idx:end_idx)];
    end
end
