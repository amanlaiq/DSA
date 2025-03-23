class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if s[i] == "*" else 0)

        left_candle = [0] * n 
        curr_left = -1
        for i in range(n):
            if s[i] =="|":
                curr_left = i
            left_candle[i] = curr_left

        right_candle = [0] * n
        curr_right = -1
        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                curr_right = i
            right_candle[i] = curr_right 

        result = [0] * len(queries)
        for i, (left, right) in enumerate(queries):
            start = right_candle[left]
            end = left_candle[right]
            if start != -1 and end != -1 and start < end:
                result[i] = prefix[end] - prefix[start + 1]
        return result
        
        # n = len(s)
        # # Prefix sum of plates
        # prefix = [0] * (n + 1)
        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + (1 if s[i] == '*' else 0)
        
        # # Nearest candle to the left
        # left_candle = [0] * n
        # curr_left = -1
        # for i in range(n):
        #     if s[i] == '|':
        #         curr_left = i
        #     left_candle[i] = curr_left
        
        # # Nearest candle to the right
        # right_candle = [0] * n
        # curr_right = -1
        # for i in range(n - 1, -1, -1):
        #     if s[i] == '|':
        #         curr_right = i
        #     right_candle[i] = curr_right
        
        # # Process queries
        # result = [0] * len(queries)
        # for i, (left, right) in enumerate(queries):
        #     # Get the candles bounding the range
        #     start = right_candle[left]  # Rightmost candle at or after left
        #     end = left_candle[right]    # Leftmost candle at or before right
        #     if start != -1 and end != -1 and start < end:
        #         result[i] = prefix[end] - prefix[start + 1]
        
        # return result