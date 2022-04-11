package com.leo.leetcode.algorithm.q1200;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。
 * 请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返
 * 提示：
 * 1、m == mat.length
 * 2、n == mat[i].length
 * 3、1 <= m, n <= 300
 * 4、0 <= mat[i][j] <= 10^4
 * 5、0 <= threshold <= 10^5
 * 链接：https://leetcode-cn.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold
 */
public class Q1292 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q1292().maxSideLength(stringToInt2dArray("[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]"), 4));
        // 0
        System.out.println(new Q1292().maxSideLength(stringToInt2dArray("[[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]"), 1));
    }

    public int maxSideLength(int[][] mat, int threshold) {
        int m = mat.length, n = mat[0].length, ret = 0;
        int[][] preSum = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
                preSum[i][j] = mat[i - 1][j - 1] + preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int l = 0, r = Math.min(m - i, n - j);
                while (l <= r) {
                    int mid = (l + r) / 2;
                    int sum = preSum[i + mid][j + mid] - preSum[i + mid][j - 1] - preSum[i - 1][j + mid] + preSum[i - 1][j - 1];
                    if (sum > threshold) r = mid - 1;
                    else {
                        l = mid + 1;
                        ret = Math.max(ret, mid + 1);
                    }
                }
            }
        }
        return ret;
    }
}
