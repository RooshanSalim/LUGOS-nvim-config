def merge_sort(array):
    if len(array) <= 1:
        return array

    # Divide the array into two halves.
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # Merge the two sorted halves.
    return merge(left, right)

def merge(left, right):
    merged_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1

    # Add the remaining elements from the left and right arrays.
    merged_array += left[i:]
    merged_array += right[j:]

    return merged_array

# Example usage:

array = [5, 3, 2, 1, 4]
sorted_array = merge_sort(array)

print(sorted_array)
