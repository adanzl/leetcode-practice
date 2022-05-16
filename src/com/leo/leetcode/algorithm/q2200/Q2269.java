package com.leo.leetcode.algorithm.q2200;

/**
 * 一个整数 num 的 k 美丽值定义为 num 中符合以下条件的 子字符串 数目：
 * 1.子字符串长度为 k 。
 * 2、子字符串能整除 num 。
 * 给你整数 num 和 k ，请你返回 num 的 k 美丽值。
 * 注意：
 * 1、允许有 前缀 0 。
 * 2、0 不能整除任何值。
 * 一个 子字符串 是一个字符串里的连续一段字符序列。
 * 提示：
 * 1、1 <= num <= 10^9
 * 2、1 <= k <= num.length （将 num 视为字符串）
 * 链接：https://leetcode.cn/problems/find-the-k-beauty-of-a-number
 */
public class Q2269 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q2269().divisorSubstrings(240, 2));
        // 2
        System.out.println(new Q2269().divisorSubstrings(430043, 2));
    }

    public int divisorSubstrings(int num, int k) {
        String nStr = String.valueOf(num);
        int ret = 0;
        for (int i = 0; i < nStr.length() - k + 1; i++) {
            int v = Integer.parseInt(nStr.substring(i, i + k));
            if (v == 0) continue;
            if (num % v == 0) ret++;
        }
        return ret;
    }
}
