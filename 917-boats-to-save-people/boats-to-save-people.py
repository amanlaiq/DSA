class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        res = 0

        while l <= r:
            remain = limit - people[r]
            res += 1
            r -= 1
            if l <= r and people[l] <= remain:
                l += 1
        return res

