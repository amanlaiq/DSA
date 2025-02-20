class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        minheap = []
        curpass = 0

        for numpass, start, end in trips:
            while minheap and minheap[0][0] <= start:
                curpass -= heapq.heappop(minheap)[1]
            curpass += numpass
            if curpass > capacity:
                return False
            heapq.heappush(minheap, [end, numpass])
        return True


        # #BruteForce
        # passchange = [0] * 1001

        # for t in trips:
        #     curpass, start, end = t
        #     passchange[start] += curpass
        #     passchange[end] -= curpass
        
        # curpass = 0
        # for i in range(1001):
        #     curpass += passchange[i]
        #     if curpass > capacity:
        #         return False
        # return True