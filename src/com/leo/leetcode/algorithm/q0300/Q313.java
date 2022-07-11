package com.leo.leetcode.algorithm.q0300;

import java.util.PriorityQueue;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
 * 给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。
 * 题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、1 <= primes.length <= 100
 * 3、2 <= primes[i] <= 1000
 * 4、题目数据 保证 primes[i] 是一个质数
 * 5、primes 中的所有值都 互不相同 ，且按 递增顺序 排列
 * 链接：https://leetcode.cn/problems/super-ugly-number
 */
public class Q313 {

    public static void main(String[] args) {
        // 34535457
        System.out.println(new Q313().nthSuperUglyNumber(100000, stringToIntegerArray("[2,3,5,7,11,13,17,19,23,29,31,37]")));
        // 32
        System.out.println(new Q313().nthSuperUglyNumber(12, stringToIntegerArray("[2,7,13,19]")));
        // 1
        System.out.println(new Q313().nthSuperUglyNumber(1, stringToIntegerArray("[2,3,5]")));
    }

    public int nthSuperUglyNumber(int n, int[] primes) {
        int[] dp = new int[n + 1];
        dp[1] = 1;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 2; i <= n; i++) {
            for (int p : primes) {
                long v = (long) p * dp[i - 1];
                if (v < Integer.MAX_VALUE) pq.offer((int) v);
            }
            while (!pq.isEmpty() && pq.peek() == dp[i - 1]) pq.poll();
            if (!pq.isEmpty()) dp[i] = pq.poll();
        }
        return dp[n];
    }
}
