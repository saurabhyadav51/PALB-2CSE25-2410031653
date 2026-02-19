def merge(intervals):
    intervals.sort()
    result = []

    for interval in intervals:
        if not result:
            result.append(interval)
        else:
            last = result[-1]
            if interval[0] <= last[1]:
                last[1] = max(last[1], interval[1])
            else:
                result.append(interval)

    return result


print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[4,7],[1,4]]))