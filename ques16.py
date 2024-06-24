def check_parity(binary_pattern):
    """
    Check the parity of a given binary pattern.
    
    Parameters:
    binary_pattern (str): A string representing the binary pattern (e.g., '101010').
    
    Returns:
    str: 'Even parity' if the number of 1s is even, 'Odd parity' if the number of 1s is odd.
    """
    # Ensure the binary_pattern only contains '0' and '1'
    if not all(bit in '01' for bit in binary_pattern):
        raise ValueError("The binary pattern should only contain '0' and '1'.")
    
    # Count the number of '1's in the binary pattern
    count_of_ones = binary_pattern.count('1')
    
    # Determine parity based on the count of '1's
    if count_of_ones % 2 == 0:
        return 'Even parity'
    else:
        return 'Odd parity'

# Example usage:
patterns = ['10101', '0100111', '11000000', '1110111', '111000']
for pattern in patterns:
    result = check_parity(pattern)
    print(f"Pattern: {pattern} -> {result}")
