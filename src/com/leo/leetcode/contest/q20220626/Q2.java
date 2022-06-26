package com.leo.leetcode.contest.q20220626;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 链接：https://leetcode.cn/contest/sf-tech/problems/cINqyA/
 */
public class Q2 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q2().minRemainingSpace(stringToIntegerArray("[8, 1, 12, 7, 9, 7]"), 11));
        // 0
        System.out.println(new Q2().minRemainingSpace(stringToIntegerArray("[8, 2, 12, 7, 9, 7]"), 11));
        // 55
        System.out.println(new Q2().minRemainingSpace(stringToIntegerArray("[8, 2, 12, 7, 9, 7]"), 100));
        // 5
        System.out.println(new Q2().minRemainingSpace(stringToIntegerArray("[8, 19, 18,23,16,20]"), 5));
    }

    // 背包问题
    public int minRemainingSpace(int[] N, int V) {
        int[] f = new int[2022];
        for (int k : N)
            for (int j = V; j >= k; j--)
                if (f[j] < f[j - k] + k)
                    f[j] = f[j - k] + k;
        return V - f[V];
    }
}
