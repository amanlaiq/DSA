from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  # If lengths differ, they can't be anagrams

        char_count = defaultdict(int)

        # Count occurrences of characters in s
        for char in s:
            char_count[char] += 1
        
        # Subtract occurrences using t
        for char in t:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False  # If count goes negative, extra character found in t

        return True  # If all counts are zero, it's an anagram
