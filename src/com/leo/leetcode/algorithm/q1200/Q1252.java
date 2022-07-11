package com.leo.leetcode.algorithm.q1200;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 m x n 的矩阵，最开始的时候，每个单元格中的值都是 0。
 * 另有一个二维索引数组 indices，indices[i] = [ri, ci] 指向矩阵中的某个位置，其中 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。
 * 对 indices[i] 所指向的每个位置，应同时执行下述增量操作：
 * 1、ri 行上的所有单元格，加 1 。
 * 2、ci 列上的所有单元格，加 1 。
 * 给你 m、n 和 indices 。请你在执行完所有 indices 指定的增量操作后，返回矩阵中 奇数值单元格 的数目。
 * 提示：
 * 1、1 <= m, n <= 50
 * 2、1 <= indices.length <= 100
 * 3、0 <= ri < m
 * 4、0 <= ci < n
 * 进阶：你可以设计一个时间复杂度为 O(n + m + indices.length) 且仅用 O(n + m) 额外空间的算法来解决此问题吗？
 * 链接：https://leetcode.cn/problems/cells-with-odd-values-in-a-matrix
 */
public class Q1252 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q1252().oddCells(2, 2, stringToInt2dArray("[[1,1],[0,0]]")));
        // 6
        System.out.println(new Q1252().oddCells(2, 3, stringToInt2dArray("[[0,1],[1,1]]")));
    }

    public int oddCells(int m, int n, int[][] indices) {
        boolean[] v1 = new boolean[m], v2 = new boolean[n];
        for (int[] indic : indices) {
            v1[indic[0]] = !v1[indic[0]];
            v2[indic[1]] = !v2[indic[1]];
        }
        int cnt_o1 = 0, cnt_o2 = 0;
        for (boolean v : v1) if (v) cnt_o1++;
        for (boolean v : v2) if (v) cnt_o2++;
        return cnt_o1 * (n - cnt_o2) + cnt_o2 * (m - cnt_o1);
    }
}
