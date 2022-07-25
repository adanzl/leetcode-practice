package com.leo.leetcode.algorithm.q6000;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。
 * 如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。
 * 提示：
 * 1、n == grid.length == grid[i].length
 * 2、1 <= n <= 200
 * 3、1 <= grid[i][j] <= 10^5
 * 链接：https://leetcode.cn/problems/equal-row-and-column-pairs
 */
public class Q2352 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q2352().equalPairs(stringToInt2dArray("[[3,2,1],[1,7,6],[2,7,7]]")));
        // 3
        System.out.println(new Q2352().equalPairs(stringToInt2dArray("[[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]")));
    }

    public int equalPairs(int[][] grid) {
        int ret = 0, n = grid.length;
        int[] countRow = new int[n];
        countRow[0] = 1;
        for (int i = 0; i < n; i++) {
            // row
            boolean fit = true;
            for (int j = 0; j < i; j++) {
                fit = true;
                for (int k = 0; k < n; k++) {
                    if (grid[i][k] != grid[j][k]) {
                        fit = false;
                        break;
                    }
                }
                if (fit) {
                    countRow[j]++;
                    break;
                }
            }
            if (!fit) countRow[i] = 1;
        }

        for (int i = 0; i < n; i++) { // col
            for (int j = 0; j < n; j++) { // row
                boolean fit = true;
                for (int k = 0; k < n; k++) {
                    if (grid[k][i] != grid[j][k]) {
                        fit = false;
                        break;
                    }
                }
                if (fit) {
                    ret += countRow[j];
                    break;
                }
            }
        }
        return ret;
    }

}
