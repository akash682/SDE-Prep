import heapq


def minMeetingRooms(intervals):
        lst = []
        for start, end in intervals:
            lst.append((start, 1))
            lst.append((end, -1))
        lst.sort()
        res, curr_rooms = 0, 0
        for t, n in lst:
            curr_rooms += n
            res = max(res, curr_rooms)
        return res

intervals = [[0,30],[5,10],[15,20]]
print(minMeetingRooms(intervals))

def minMeetingRooms(intervals):
    intervals.sort(key = lambda x: x[0])
    res = 0
    heap, heap_size = [], 0
    for interval in intervals:
        while heap and heap[0] <= interval[0]:
            heapq.heappop(heap)
            heap_size -= 1
        heapq.heappush(heap, interval[1])
        heap_size += 1
        res = max(res, heap_size)
    return res

print(minMeetingRooms(intervals))

