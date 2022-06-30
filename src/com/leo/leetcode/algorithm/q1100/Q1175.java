package com.leo.leetcode.algorithm.q1100;

import java.util.ArrayList;
import java.util.List;

/**
 * 请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。
 * 让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。
 * 由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。
 * 提示：1 <= n <= 100
 * 链接：https://leetcode.cn/problems/prime-arrangements
 */
public class Q1175 {

    public static void main(String[] args) {
        // 12
        System.out.println(new Q1175().numPrimeArrangements(5));
        // 682289015
        System.out.println(new Q1175().numPrimeArrangements(100));
    }

    // 线性筛选质数
    public int numPrimeArrangements(int n) {
        int MOD = 1_000_000_007;
        int[] bPrime = new int[n + 1];
        List<Integer> primeList = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (bPrime[i] == 0) primeList.add(i);
            for (int prime : primeList) {
                int next = prime * i;
                if (next <= n) bPrime[next] = 1;
            }
        }
        int nPrime = primeList.size(), nV = n - nPrime;
        long ret = 1;
        while (nPrime > 1) ret = (ret * nPrime--) % MOD;
        while (nV > 1) ret = (ret * nV--) % MOD;
        return (int) ret;
    }
}
