package com.leo.leetcode.algorithm.q1400;

import java.util.ArrayList;
import java.util.List;

/**
 * 给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。
 * 斐波那契数字定义为：
 * F1 = 1
 * F2 = 1
 * Fn = Fn-1 + Fn-2 ， 其中 n > 2 。
 * 数据保证对于给定的 k ，一定能找到可行解
 * 提示：
 * 1 <= k <= 10^9
 * <p>
 * 链接：https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k
 */
public class Q1414 {
    public static void main(String[] args) {
        // 2
        System.out.println(new Q1414().findMinFibonacciNumbers(7));
        // 2
        System.out.println(new Q1414().findMinFibonacciNumbers(10));
        // 3
        System.out.println(new Q1414().findMinFibonacciNumbers(19));
    }

    List<Integer> fa = new ArrayList<>();

    public int findMinFibonacciNumbers(int k) {
        int a0 = 1, a1 = 1;
        fa.add(a0);
        while (a0 < k) {
            int t = a0 + a1;
            a0 = a1;
            a1 = t;
            fa.add(a0);
        }
        return func(k);
    }

    int func(int k) {
        if (k == 0) return 0;
        int v = 0;
        for (Integer integer : fa) {
            if (integer > k) break;
            v = integer;
        }
        return func(k - v) + 1;
    }
}
