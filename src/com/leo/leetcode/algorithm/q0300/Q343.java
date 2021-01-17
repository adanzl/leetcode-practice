package com.leo.leetcode.algorithm.q0300;

/**
 * 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 
 * 返回你可以获得的最大乘积。
 * 说明: 你可以假设 n 不小于 2 且不大于 58。
 * 链接：https://leetcode-cn.com/problems/integer-break/
 */
public class Q343 {

    public static void main(String[] args) {
        System.out.println(new Q343().integerBreak(2)); // 1
        System.out.println(new Q343().integerBreak(4)); // 4
        System.out.println(new Q343().integerBreak(5)); // 6
        System.out.println(new Q343().integerBreak(6)); // 9
        System.out.println(new Q343().integerBreak(10)); // 36
    }

    public int integerBreak(int n) {
        if (n == 2) return 1;
        if (n == 3) return 2;
        if (n == 4) return 4;
        return iBreak(n);
    }

    int iBreak(int n) {
        if (n == 2) return 2;
        if (n == 3) return 3;
        if (n == 4) return 4;
        return iBreak(n - 3) * 3;
    }
}