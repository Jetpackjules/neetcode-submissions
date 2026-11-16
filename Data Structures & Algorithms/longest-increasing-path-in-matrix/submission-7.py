class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        seen = {}
        dirs = [[-1, 0], [1,0], [0,1], [0,-1]]
        rows, cols = len(matrix), len(matrix[0])

        # DFS:
        # RETUR: LONGEST PATH FROM THIS POSITION, WITHOUT DUPING
        def dfs(curr):
            if curr not in seen:
                r,c = curr
                longest = 0
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:                    
                        longest = max(longest, dfs((nr,nc)))

                seen[curr] = 1+longest

            return seen[curr]

        best = 0
        for r in range(rows):
            for c in range(cols):
                best = max(best, dfs((r,c)))
        return best

            