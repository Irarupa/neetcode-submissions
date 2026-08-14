class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                digit = board[r][c]
                boxes_id = (r//3)*3+(c//3)

                if digit in rows[r] or digit in cols[c] or digit in boxes[boxes_id]:
                    return False
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[boxes_id].add(digit)
        return True


