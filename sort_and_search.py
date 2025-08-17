# 1. Create a Python script called sort_and_search.py.

def linear_search(data, target):
    """
    Performs a linear search on a list to find the index of a target element.
    """
    for index in range(len(data)):
        if data[index] == target:
            return index  # Target found, return its index
    return -1  # Target not found

def insertion_sort(data):
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.
    """
    # Traverse through 1 to len(data)
    for i in range(1, len(data)):
        key = data[i]
        # Move elements of data[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def binary_search(sorted_data, target):
    """
    Performs a binary search on a sorted list to find the index of a target element.
    """
    low = 0
    high = len(sorted_data) - 1
    while low <= high:
        mid = (low + high) // 2
        # Check if target is present at mid
        if sorted_data[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif sorted_data[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1
    return -1  # Target not found

# The list provided for the task
data_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target_number = 9

print("--- Task 3: Sorting and Searching ---")
print(f"Original list: {data_list}\n")

# 2. Implement a search algorithm to find the number 9.
# Comment:
# Linear search is the appropriate choice here because the list is unsorted.
# This algorithm checks each element sequentially until the target is found,
# which is the only reliable method for an unordered collection.
print(f"--- Step 2: Searching for {target_number} in the unsorted list ---")
index_found = linear_search(data_list, target_number)
if index_found != -1:
    print(f"Using Linear Search, the number {target_number} was found at index: {index_found}\n")
else:
    print(f"The number {target_number} was not found in the list.\n")


# 3. Research and implement the Insertion sort on this list.
print("--- Step 3: Sorting the list using Insertion Sort ---")
sorted_list = insertion_sort(list(data_list)) # Use a copy to preserve original
print(f"List after Insertion Sort: {sorted_list}\n")


# 4. Implement a different searching algorithm on the sorted list to find the number 9.
print(f"--- Step 4: Searching for {target_number} in the sorted list ---")
index_found_sorted = binary_search(sorted_list, target_number)
if index_found_sorted != -1:
    print(f"Using Binary Search, the number {target_number} was found at index: {index_found_sorted}")
else:
    print(f"The number {target_number} was not found in the sorted list.")