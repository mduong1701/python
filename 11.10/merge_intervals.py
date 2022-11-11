intervals = [[9,10],[6,8],[4,7],[3,5],[1,2]]

def mergeOverlappingIntervals(intervals):
    intervals.sort(key = lambda i: i[0])
    output = []
    for start, end in intervals:
        if not output or start > output[-1][1]:
            output.append([start, end])
        else:
            output[-1][1] = max(output[-1][1], end)

    return output

print(mergeOverlappingIntervals(intervals))
