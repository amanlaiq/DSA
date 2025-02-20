class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passchange = [0] * 1001

        for t in trips:
            curpass, start, end = t
            passchange[start] += curpass
            passchange[end] -= curpass
        
        curpass = 0
        for i in range(1001):
            curpass += passchange[i]
            if curpass > capacity:
                return False
        return True
        