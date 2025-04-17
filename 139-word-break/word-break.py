class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}

        for word in wordDict:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["#"] = True

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            node = trie
            for j in range(i, n):
                char = s[j]
                if char not in node:
                    break
                node = node[char]
                if "#" in node:
                    dp[j + 1] = True
        return dp[n]