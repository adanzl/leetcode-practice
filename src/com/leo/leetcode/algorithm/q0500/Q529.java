package com.leo.leetcode.algorithm.q0500;

import static com.leo.utils.LCUtil.char2dToString;
import static com.leo.utils.LCUtil.stringToChar2dArray;

/**
 * 让我们一起来玩扫雷游戏！
 * 给定一个代表游戏板的二维字符矩阵。 
 * 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，
 * 'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，
 * 数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。
 * 现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：
 *     如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
 *     如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
 *     如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
 *     如果在此次点击中，若无更多方块可被揭露，则返回面板。
 * 链接：https://leetcode-cn.com/problems/minesweeper/
 */
public class Q529 {

    public static void main(String[] args) {
        System.out.println(char2dToString(new Q529().updateBoard(stringToChar2dArray(
                "[[\"E\",\"E\",\"E\",\"E\",\"E\"],[\"E\",\"E\",\"M\",\"E\",\"E\"],[\"E\",\"E\",\"E\",\"E\",\"E\"],[\"E\",\"E\",\"E\",\"E\",\"E\"]]"),
                new int[] { 3, 0 }))); // [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
        System.out.println(char2dToString(new Q529().updateBoard(stringToChar2dArray(
                "[[\"B\", \"1\", \"E\", \"1\", \"B\"], [\"B\", \"1\", \"M\", \"1\", \"B\"], [\"B\", \"1\", \"1\", \"1\", \"B\"], [\"B\", \"B\", \"B\", \"B\", \"B\"]]"),
                new int[] { 1, 2 }))); // [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    }

    public char[][] updateBoard(char[][] board, int[] click) {
        return updateBoard(board, click[0], click[1]);
    }

    char[][] updateBoard(char[][] board, int x, int y) {
        if (x < 0 || x > board.length - 1 || y < 0 || y > board[0].length - 1) return board;
        char v = board[x][y];
        if (v == 'M') {
            board[x][y] = 'X';
        }
        if (v == 'E') {
            int mCount = 0;
            if (isMine(board, x - 1, y)) ++mCount;
            if (isMine(board, x + 1, y)) ++mCount;
            if (isMine(board, x - 1, y + 1)) ++mCount;
            if (isMine(board, x + 1, y + 1)) ++mCount;
            if (isMine(board, x - 1, y - 1)) ++mCount;
            if (isMine(board, x + 1, y - 1)) ++mCount;
            if (isMine(board, x, y + 1)) ++mCount;
            if (isMine(board, x, y - 1)) ++mCount;
            if (mCount == 0) {
                board[x][y] = 'B';
                updateBoard(board, x - 1, y);
                updateBoard(board, x + 1, y);
                updateBoard(board, x - 1, y + 1);
                updateBoard(board, x + 1, y + 1);
                updateBoard(board, x - 1, y - 1);
                updateBoard(board, x + 1, y - 1);
                updateBoard(board, x, y + 1);
                updateBoard(board, x, y - 1);
            } else {
                board[x][y] = (char) ('0' + mCount);
            }
        }
        return board;
    }

    boolean isMine(char[][] board, int x, int y) {
        if (x < 0 || x > board.length - 1 || y < 0 || y > board[0].length - 1) return false;
        return board[x][y] == 'M';
    }
}