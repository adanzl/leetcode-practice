package com.leo.leetcode.algorithm.q0600;

/**
 * 在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。
 * 行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。
 * 象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。
 * 每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。
 * 骑士继续移动，直到它走了 k 步或离开了棋盘。
 * 返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。
 * 提示:
 * 1、1 <= n <= 25
 * 2、0 <= k <= 100
 * 3、0 <= row, column <= n
 * 链接：https://leetcode-cn.com/problems/knight-probability-in-chessboard
 */
public class Q688 {

    public static void main(String[] args) {
        // 0.0625
        System.out.println(new Q688().knightProbability(3, 2, 0, 0));
        // 1.00000
        System.out.println(new Q688().knightProbability(1, 0, 0, 0));
        // 0.0000
        System.out.println(new Q688().knightProbability(1, 1, 0, 0));
    }

    int[][] dirs = new int[][]{{-2, -1}, {-2, 1}, {2, -1}, {2, 1}, {-1, -2}, {-1, 2}, {1, -2}, {1, 2}};
    double[][][] map;
    int n;

    public double knightProbability(int n, int k, int row, int column) {
        if (k == 0) return 1.0;
        map = new double[k][n][n];
        this.n = n;
        for (int i = 1; i < k; i++) for (int j = 0; j < n; j++) for (int l = 0; l < n; l++) map[i][j][l] = -1;
        for (int j = 0; j < n; j++) {
            for (int l = 0; l < n; l++) {
                for (int[] dir : dirs) {
                    if (check(j + dir[0], l + dir[1]))
                        map[0][j][l] += 1 / 8.0;
                }
            }
        }

        return getProbability(row, column, k - 1);
    }

    double getProbability(int x, int y, int k) {
        if (!check(x, y)) return 0;
        if (map[k][x][y] != -1) return map[k][x][y];
        double v = 0;
        for (int[] dir : dirs) v += getProbability(x + dir[0], y + dir[1], k - 1) / 8.0;
        map[k][x][y] = v;
        return v;
    }

    boolean check(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < n;
    }
}
