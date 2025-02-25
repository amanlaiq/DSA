class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posdiag = set()
        negdiag = set()
        res = 0
        
        board = [ ["."] * n for i in range(n)]

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return 
            
            for c in range(n):
                if c in col or (r + c) in posdiag or (r - c) in negdiag:
                    continue
                
                col.add(c)
                posdiag.add(r + c)
                negdiag.add(r - c)

                backtrack(r + 1)
                
                col.remove(c)
                posdiag.remove(r + c)
                negdiag.remove(r - c)

        backtrack(0)
        return res