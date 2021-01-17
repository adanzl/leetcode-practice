package com.leo.leetcode.algorithm.q0300;

import java.util.Arrays;

import com.leo.utils.LCUtil;

/**
 * 给定一个整数矩阵，找出最长递增路径的长度。 对于每个单元格，你可以往上，下，左，右四个方向移动。
 * 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
 * 链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/
 */
class Q329 {

    public static void main(String[] args) {
        System.out.println(new Q329().longestIncreasingPath(LCUtil.stringToInt2dArray("[[2147483647,1]]"))); // 2
        System.out.println(new Q329().longestIncreasingPath(LCUtil.stringToInt2dArray("[[9,9,4],[6,6,8],[2,1,1]]"))); // 4
        System.out.println(new Q329().longestIncreasingPath(LCUtil.stringToInt2dArray("[[3,4,5],[3,2,6],[2,2,1]]"))); // 4
    }

    public int longestIncreasingPath(int[][] matrix) {
        if (matrix.length == 0) return 0;
        int[][] marks = new int[matrix.length][matrix[0].length];
        for (int[] l : marks) {
            Arrays.fill(l, -1);
        }
        int out = 0;
        for (int i = 0; i < marks.length; i++) {
            for (int j = 0; j < marks[i].length; j++) {
                out = Math.max(out, process(matrix, marks, i, j, Integer.MAX_VALUE + 1L));
            }
        }
        return out;
    }

    int process(int[][] matrix, int[][] marks, int x, int y, long pre_v) {
        if (x < 0 || x >= marks.length || y < 0 || y >= marks[0].length || matrix[x][y] >= pre_v) return 0;
        if (marks[x][y] != -1) return marks[x][y];
        int out = 0, v = matrix[x][y];
        out = Math.max(out, process(matrix, marks, x - 1, y, v));
        out = Math.max(out, process(matrix, marks, x + 1, y, v));
        out = Math.max(out, process(matrix, marks, x, y + 1, v));
        out = Math.max(out, process(matrix, marks, x, y - 1, v));
        ++out;
        marks[x][y] = out;
        return out;
    }
}