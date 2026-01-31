def largest_element(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

arr = [1, 8, 7, 56, 90]
print(largest_element(arr))
