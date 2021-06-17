package com.leo.leetcode.algorithm.q0400;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
 * 请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
 * 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
 * <p>
 * 提示：
 * 1、1 <= strs.length <= 600
 * 2、1 <= strs[i].length <= 100
 * 3、strs[i] 仅由 '0' 和 '1' 组成
 * 4、1 <= m, n <= 100
 * <p>
 * 链接：https://leetcode-cn.com/problems/ones-and-zeroes
 */
public class Q474 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q474().findMaxForm(stringToStringArray("[\"10\",\"0001\",\"111001\",\"1\",\"0\"]"), 5, 3));
        // 4
        System.out.println(new Q474().findMaxForm(stringToStringArray("[\"10\",\"0001\",\"111001\",\"1\",\"0\"]"), 5, 6));
        // 2
        System.out.println(new Q474().findMaxForm(stringToStringArray("[\"10\", \"0\", \"1\"]"), 1, 1));
    }

    public int findMaxForm(String[] strs, int m, int n) {
        int nStr = strs.length;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i < nStr + 1; i++) {
            int c0 = 0, c1 = 0;
            for (char c : strs[i - 1].toCharArray()) {
                if (c == '0') c0++;
                else if (c == '1') c1++;
            }
            for (int j = m; j >= 0; j--) {
                for (int k = n; k >= 0; k--) {
                    if (j >= c0 && k >= c1) dp[j][k] = Math.max(dp[j - c0][k - c1] + 1, dp[j][k]);
                }
            }
        }
        return dp[m][n];
    }
}
