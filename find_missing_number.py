def find_missing(arr):
    missing_numbers = []
    n = len(arr)

    low = 0
    high = n - 1

    while low < high:  # Iterate through the array
        # If there is a gap between consecutive elements
        if arr[low + 1] - arr[low] > 1:
            # Find the midpoint (first missing number in the gap)
            missing_number = (arr[low] + arr[low + 1]) // 2
            missing_numbers.append(missing_number)
            
            # Insert the missing number temporarily to handle multiple gaps
            arr.insert(low + 1, missing_number)
            high += 1  # Adjust the array's bounds since we've added an element
        else:
            # Move to the next element if no gap exists
            low += 1

    return missing_numbers

# Example Usage
sorted_array = [1, 2, 3, 5, 6, 8]
result = find_missing(sorted_array)
print(f"Missing numbers: {result}")
