class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> squares = new HashMap<>();

        for (int i = 0; i < board.length; i ++) {
            rows.putIfAbsent(i, new HashSet<>());
            cols.putIfAbsent(i, new HashSet<>());
            squares.putIfAbsent(i, new HashSet<>());
        }

        for (int r = 0; r < board.length; r ++) {
            for (int c = 0; c < board[0].length; c++) {
                if (board[r][c] == '.') continue;

                char num = board[r][c];
                int boxIndex = (r / 3) * 3 + (c / 3);

                if (rows.get(r).contains(num) || cols.get(c).contains(num) || squares.get(boxIndex).contains(num)) {
                    return false;
                }

                rows.get(r).add(num);
                cols.get(c).add(num);
                squares.get(boxIndex).add(num);
            }
        }

        return true;
    }
}