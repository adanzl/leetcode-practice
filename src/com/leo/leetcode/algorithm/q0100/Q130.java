package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;

/**
 * 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
 * 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
 * 解释:
 * 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
 * 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
 * 如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
 * 链接：https://leetcode-cn.com/problems/surrounded-regions
 */
public class Q130 {
    public static void main(String[] args) {
        char[][] case1 = LCUtil.stringToChar2dArray("[[\"X\",\"X\",\"X\",\"X\"],[\"X\",\"O\",\"O\",\"X\"],[\"X\",\"X\",\"O\",\"X\"],[\"X\",\"O\",\"X\",\"X\"]]");
        new Q130().solve(case1); // [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        System.out.println(LCUtil.char2dToString(case1));
        char[][] case2 = LCUtil.stringToChar2dArray("[[\"X\",\"O\",\"X\"],[\"O\",\"X\",\"O\"],[\"X\",\"O\",\"X\"]]");
        new Q130().solve(case2); // [["X","O","X"],["O","X","O"],["X","O","X"]]
        System.out.println(LCUtil.char2dToString(case2));
    }

    public void solve(char[][] board) {
        if (board.length == 0) return;
        for (int i = 0; i < board[0].length; i++) dp(board, 0, i);
        for (int i = 0; i < board[0].length; i++) dp(board, board.length - 1, i);
        for (int i = 0; i < board.length; i++) dp(board, i, 0);
        for (int i = 0; i < board.length; i++) dp(board, i, board[i].length - 1);

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                else if (board[i][j] == ' ') board[i][j] = 'O';
            }
        }
    }

    void dp(char[][] board, int x, int y) {
        if (x < 0 || x > board.length - 1 || y < 0 || y > board[0].length - 1) return;
        if (board[x][y] == 'O') {
            board[x][y] = ' ';
            dp(board, x + 1, y);
            dp(board, x - 1, y);
            dp(board, x, y + 1);
            dp(board, x, y - 1);
        }
    }
}
