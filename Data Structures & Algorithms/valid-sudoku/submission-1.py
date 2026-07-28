class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 steps: check grids, check rows, check colss. we can do all at once:

        rows  = [set() for _ in range(9)]
        cols  = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]


        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == ".":
                    continue
                grid = i // 3 *3+ j//3
                if curr in rows[i] or curr in cols[j] or curr in grids[grid]:
                    return False
                else:
                    rows[i].add(curr)
                    cols[j].add(curr)
                    grids[grid].add(curr)
        return True
