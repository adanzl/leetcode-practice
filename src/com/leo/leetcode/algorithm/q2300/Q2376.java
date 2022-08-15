package com.leo.leetcode.algorithm.q2300;

import java.util.Arrays;

/**
 * 如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。
 * 给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。
 * 提示：1 <= n <= 2 * 10^9
 * 链接：https://leetcode.cn/problems/count-special-integers/
 */
public class Q2376 {

    public static void main(String[] args) {
        // 323
        System.out.println(new Q2376().countSpecialNumbers(420));
        // 19
        System.out.println(new Q2376().countSpecialNumbers(20));
        // 110
        System.out.println(new Q2376().countSpecialNumbers(135));
        // 5
        System.out.println(new Q2376().countSpecialNumbers(5));
    }

    //    数位DP-记忆
    int[][] dp;
    char[] nums;

    public int countSpecialNumbers(int n) {
        nums = String.valueOf(n).toCharArray();
        dp = new int[nums.length][];
        for (int i = 0; i < nums.length; i++) {
            dp[i] = new int[1 << 10];
            Arrays.fill(dp[i], -1);
        }
        return f(0, 0, true, true);
    }

    /**
     * @param i       idx
     * @param mask    数字的使用情况
     * @param isLimit 前一位是否是最大值，如果是则当前位上界为nums[i]，否则为'9'
     * @param isFirst 当前位是否是首位，如果是则当前位下界不能为'0'
     */
    int f(int i, int mask, boolean isLimit, boolean isFirst) {
        if (i == nums.length) return isFirst ? 0 : 1;
        if (!isFirst && !isLimit && dp[i][mask] != -1) return dp[i][mask];
        int up = isLimit ? (nums[i] - '0') : 9, ret = 0;
        if (isFirst) {
            ret += f(i + 1, mask, false, true);
        }
        for (int j = isFirst ? 1 : 0; j <= up; j++) {
            if ((mask & 1 << j) != 0) continue;
            ret += f(i + 1, mask | 1 << j, isLimit && j == up, false);
        }
        if (!isFirst && !isLimit) dp[i][mask] = ret;
        return ret;
    }
}
