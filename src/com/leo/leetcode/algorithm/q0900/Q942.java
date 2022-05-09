package com.leo.leetcode.algorithm.q0900;

import java.util.Arrays;

/**
 * 由范围 [0,n] 内所有整数组成的 n + 1 个整数的排列序列可以表示为长度为 n 的字符串 s ，其中:
 * 1、如果 perm[i] < perm[i + 1] ，那么 s[i] == 'I'
 * 2、如果 perm[i] > perm[i + 1] ，那么 s[i] == 'D'
 * 给定一个字符串 s ，重构排列 perm 并返回它。如果有多个有效排列perm，则返回其中 任何一个 。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 只包含字符 "I" 或 "D"
 * 链接：https://leetcode.cn/problems/di-string-match
 */
public class Q942 {

    public static void main(String[] args) {
        // [0,4,1,3,2]
        System.out.println(Arrays.toString(new Q942().diStringMatch("IDID")));
        // [0,1,2,3]
        System.out.println(Arrays.toString(new Q942().diStringMatch("III")));
        // [3,2,0,1]
        System.out.println(Arrays.toString(new Q942().diStringMatch("DDI")));
    }

    public int[] diStringMatch(String s) {
        int n = s.length(), l = 0, r = n;
        int[] ret = new int[n + 1];
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == 'I') ret[i] = l++;
            else ret[i] = r--;
        }
        ret[n] = l;
        return ret;
    }
}
