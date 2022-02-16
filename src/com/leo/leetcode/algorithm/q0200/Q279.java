package com.leo.leetcode.algorithm.q0200;

import java.util.HashSet;
import java.util.Set;

/**
 * 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
 * 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
 * 提示：
 * 1 <= n <= 10^4
 * 链接：https://leetcode-cn.com/problems/perfect-squares
 */
public class Q279 {

    public static void main(String[] args) {
        new Q279().TestOJ();
    }

    public void TestOJ() {
        // 3
        System.out.println(numSquares(12));
        // 2
        System.out.println(numSquares(13));
        // 2
        System.out.println(numSquares(101));
    }

    public int numSquares(int n) {
        int[] arr = new int[(int) Math.sqrt(n)];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (i + 1) * (i + 1);
        }
        int deep = 0;
        Set<Integer> s = new HashSet<>(), current = new HashSet<>();
        current.add(n);
        while (true) {
            Set<Integer> next = new HashSet<>();
            for (int v : current) {
                for (int i : arr) {
                    int c = v - i;
                    if (c < 0 || s.contains(c)) {
                        continue;
                    }
                    if (c == 0) return deep + 1;
                    s.add(c);
                    next.add(c);
                }
            }
            current = next;
            deep++;
        }
    }
}
