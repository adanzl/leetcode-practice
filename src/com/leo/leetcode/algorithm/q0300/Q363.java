package com.leo.leetcode.algorithm.q0300;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。
 * 题目数据保证总会存在一个数值和不超过 k 的矩形区域。
 * 提示：
 * 1、m == matrix.length
 * 2、n == matrix[i].length
 * 3、1 <= m, n <= 100
 * 4、-100 <= matrix[i][j] <= 100
 * 5、-10^5 <= k <= 10^5
 * 进阶：如果行数远大于列数，该如何设计解决方案？
 * 链接：https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k
 */
public class Q363 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q363().maxSumSubMatrix(stringToInt2dArray("[[2,2,-1]]"), 3));
        // 2
        System.out.println(new Q363().maxSumSubMatrix(stringToInt2dArray("[[1,0,1],[0,-2,3]]"), 2));
    }

    public int maxSumSubMatrix(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length, ret = Integer.MIN_VALUE;
        int[][] preSum = new int[m + 1][n + 1];
        // 二维数组前缀和
        for (int i = 0; i < m; i++) {
            int[] lPre = new int[n + 1];
            for (int j = 0; j < n; j++) {
                lPre[j + 1] = lPre[j] + matrix[i][j];
                preSum[i + 1][j + 1] = lPre[j + 1] + preSum[i][j + 1];
            }
        }
        for (int x0 = 0; x0 < m; x0++) {
            for (int y0 = 0; y0 < n; y0++) {
                for (int x1 = x0; x1 < m; x1++) {
                    for (int y1 = y0; y1 < n; y1++) {
                        long v = preSum[x0][y0] - preSum[x0][y1 + 1] - preSum[x1 + 1][y0] + preSum[x1 + 1][y1 + 1];
                        if (v > k) continue;
                        ret = Math.max(ret, (int) v);
                    }
                }
            }
        }
        return ret;
    }
}
