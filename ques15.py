def generate_parity(binary_pattern, parity_type='even'):

    # Ensure the binary_pattern only contains '0' and '1'
    if not all(bit in '01' for bit in binary_pattern):
        raise ValueError("The binary pattern should only contain '0' and '1'.")
    
    # Count the number of '1's in the binary pattern
    count_of_ones = binary_pattern.count('1')
    
    # Determine parity based on the count of '1's
    if parity_type == 'even':
        if count_of_ones % 2 == 0:
            parity_bit = '0'
        else:
            parity_bit = '1'
    elif parity_type == 'odd':
        if count_of_ones % 2 == 0:
            parity_bit = '1'
        else:
            parity_bit = '0'
    else:
        raise ValueError("Invalid parity_type. Choose either 'even' or 'odd'.")
    
    # Return the original pattern with the appended parity bit
    return binary_pattern + parity_bit

# Example usage:
patterns = ['101010', '1111', '1000000', '1011', '0']
for pattern in patterns:
    even_parity_pattern = generate_parity(pattern, parity_type='even')
    odd_parity_pattern = generate_parity(pattern, parity_type='odd')
    print(f"Pattern: {pattern}")
    print(f"Even parity: {even_parity_pattern}")
    print(f"Odd parity : {odd_parity_pattern}")
    print()
