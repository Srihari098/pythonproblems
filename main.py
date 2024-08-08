def sockMerchant(n, ar):
    # Create a dictionary to count occurrences of each color
    color_count = {}
    
    # Count each sock color
    for color in ar:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    
    # Calculate the number of pairs for each color
    pairs = 0
    for count in color_count.values():
        pairs += count // 2
    
    return pairs

# Example usage:
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar))  # Output: 3