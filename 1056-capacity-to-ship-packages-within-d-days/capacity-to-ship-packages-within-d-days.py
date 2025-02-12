class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r 

        def canship(cap):
            ship = 1
            curcap = cap 
            for w in weights:
                if curcap - w < 0:
                    ship += 1
                    if ship > days:
                        return False
                    curcap = cap
                curcap -= w
            return True

        while l <= r:
            cap = ( l + r ) // 2

            if canship(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res