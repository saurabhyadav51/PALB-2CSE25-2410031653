def isSubset(a, b):
    count = {}

    for num in a:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in b:
        if num in count and count[num] > 0:
            count[num] -= 1
        else:
            return False

    return True


print(isSubset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]))
print(isSubset([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]))
print(isSubset([10, 5, 2, 23, 19], [19, 5, 3]))