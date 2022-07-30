package com.leo.leetcode.algorithm.q0600;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
 * 现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
 * 给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。
 * 提示：给出数对的个数在 [1, 1000] 范围内。
 * 链接：https://leetcode.cn/problems/maximum-length-of-pair-chain
 */
public class Q646 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q646().findLongestChain(stringToInt2dArray("[[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]")));
        // 2
        System.out.println(new Q646().findLongestChain(stringToInt2dArray("[[1,2], [2,3], [3,4]]")));
    }

    public int findLongestChain(int[][] pairs) {
        int n = pairs.length, ret = 1;
        int[] dp = new int[n + 1];
        Arrays.sort(pairs, (a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
        Arrays.fill(dp, Integer.MAX_VALUE);
        for (int[] pair : pairs) {
            dp[1] = Math.min(dp[1], pair[1]);
            for (int i = 0; i < n; i++) {
                if (dp[i] < pair[0]) {
                    dp[i + 1] = Math.min(dp[i + 1], pair[1]);
                    ret = Math.max(ret, i + 1);
                }
            }
        }
        return ret;
    }
}
