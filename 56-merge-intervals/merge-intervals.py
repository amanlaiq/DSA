class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastend = output[-1][1]

            if start <= lastend:
                output[-1][1] = max(lastend, end)
            else:
                output.append([start,end])
        return output