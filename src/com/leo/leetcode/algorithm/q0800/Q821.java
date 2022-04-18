package com.leo.leetcode.algorithm.q0800;

import java.util.Arrays;

/**
 * 给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。
 * 返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的字符 c 的 距离 。
 * 两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。
 * 提示：
 * 1、1 <= s.length <= 10^4
 * 2、s[i] 和 c 均为小写英文字母
 * 3、题目数据保证 c 在 s 中至少出现一次
 * 链接：https://leetcode-cn.com/problems/shortest-distance-to-a-character
 */
public class Q821 {

    public static void main(String[] args) {
        // [3,2,1,0,1,0,0,1,2,2,1,0]
        System.out.println(Arrays.toString(new Q821().shortestToChar("loveleetcode", 'e')));
        // [3,2,1,0]
        System.out.println(Arrays.toString(new Q821().shortestToChar("aaab", 'b')));
    }

    public int[] shortestToChar(String s, char c) {
        int n = s.length();
        int[] ans = new int[n];
        for (int i = 0, idx = -n; i < n; ++i) {
            if (s.charAt(i) == c) idx = i;
            ans[i] = i - idx;
        }
        for (int i = n - 1, idx = 2 * n; i >= 0; --i) {
            if (s.charAt(i) == c) idx = i;
            ans[i] = Math.min(ans[i], idx - i);
        }
        return ans;
    }
}
