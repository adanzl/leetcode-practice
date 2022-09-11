package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个下标从 0 开始的 m x n 二进制矩阵 mat 和一个整数 cols ，表示你需要选出的列数。
 * 如果一行中，所有的 1 都被你选中的列所覆盖，那么我们称这一行 被覆盖 了。
 * 请你返回在选择 cols 列的情况下，被覆盖 的行数 最大 为多少。
 * 提示：
 * 1、m == mat.length
 * 2、n == mat[i].length
 * 3、1 <= m, n <= 12
 * 4、mat[i][j] 要么是 0 要么是 1 。
 * 5、1 <= cols <= n
 * 链接：https://leetcode.cn/problems/maximum-rows-covered-by-columns
 */
public class Q2397 {
    public static void main(String[] args) {
        // 2
        System.out.println(new Q2397().maximumRows(stringToInt2dArray("[[1,0,0,0,0,0,0],[0,1,0,1,1,1,1],[0,0,0,1,0,0,1]]"), 5));
        // 1
        System.out.println(new Q2397().maximumRows(stringToInt2dArray("[[0]]"), 1));
        // 2
        System.out.println(new Q2397().maximumRows(stringToInt2dArray("[[1],[0]]"), 1));
        // 3
        System.out.println(new Q2397().maximumRows(stringToInt2dArray("[[0,0,1],[1,0,0],[0,0,0]]"), 2));
        // 3
        System.out.println(new Q2397().maximumRows(stringToInt2dArray("[[0,0,0],[1,0,1],[0,1,1],[0,0,1]]"), 2));
    }

    int ans = 0;

    public int maximumRows(int[][] mat, int cols) {
        int m = mat.length, n = mat[0].length;
        int[] counts = new int[m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                counts[i] += mat[i][j];
            }
        }
        int full = 0;
        for (int i = 0; i < m; i++) if (counts[i] == 0) full |= (1 << i);
        walk(mat, 0, cols, counts, new int[m], full);
        return ans;
    }

    void walk(int[][] mat, int cIdx, int colsRemain, int[] fullCounts, int[] counts, int full) {
        int m = mat.length, newFull = full, n = mat[0].length;
        if (colsRemain == 0 || cIdx == n) return;
        walk(mat, cIdx + 1, colsRemain, fullCounts, counts, full);
        int[] newCounts = new int[m];
        for (int i = 0; i < m; i++) {
            newCounts[i] = counts[i] + mat[i][cIdx];
            if (newCounts[i] == fullCounts[i]) newFull |= (1 << i);
        }
        ans = Math.max(ans, Integer.bitCount(newFull));
        walk(mat, cIdx + 1, colsRemain - 1, fullCounts, newCounts, newFull);
    }
}