package com.leo.leetcode.algorithm.q0800;

/**
 * 给定一个正整数 n，返回 连续正整数满足所有数字之和为 n 的组数 。
 * 提示： 1 <= n <= 10^9
 * 链接：https://leetcode.cn/problems/consecutive-numbers-sum/
 */
public class Q829 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q829().consecutiveNumbersSum(15));
        // 2
        System.out.println(new Q829().consecutiveNumbersSum(5));
        // 3
        System.out.println(new Q829().consecutiveNumbersSum(9));
        // 4
        System.out.println(new Q829().consecutiveNumbersSum(15));
        // 10
        System.out.println(new Q829().consecutiveNumbersSum(1_000_000_000));
    }

    // 数学题
    public int consecutiveNumbersSum(int n) {
        // n = (x + x + k - 1) * k / 2, k = 1, 2, 3, ... , (2*n)^0.5 => x = (2*n - k^2 + k) / 2 / k
        int k = (int) Math.sqrt(n * 2) + 1, ret = 0;
        for (int i = 1; i <= k; i++) {
            int x = 2 * n - i * i + i;
            if (x > 0 && x % (2 * i) == 0)
                ret++;
        }
        return ret;
    }
}
