class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows, cols = len(heights), len(heights[0])
        dirs = [[0,1], [0,-1],[1,0],[-1,0]]
        # run DFS/BFS for each SMALLER cell!

        def flood(start, side):
            r, c = start
            height = heights[r][c]

            for dr, dc in dirs:
                newr = r+dr
                newc = c+dc
                if 0 <= newr < rows and 0 <= newc < cols and (newr, newc) not in side:
                    if heights[newr][newc] >= height:
                        side.add((newr,newc))
                        flood((newr, newc), side)

        for c in range(cols):
            pacific.add((0,c))
            atlantic.add((rows-1,c))
            flood((0,c),pacific)
            flood((rows-1,c),atlantic)
        for r in range(rows):
            pacific.add((r,0))
            atlantic.add((r,cols-1))
            flood((r,0),pacific)
            flood((r,cols-1),atlantic)

        return list(pacific.intersection(atlantic))
