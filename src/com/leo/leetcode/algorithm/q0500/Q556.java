package com.leo.leetcode.algorithm.q0500;

import java.util.Arrays;

/**
 * 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
 * 注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。
 * 提示：
 * 1 <= n <= 2^31 - 1
 * 链接：https://leetcode-cn.com/problems/next-greater-element-iii
 */
public class Q556 {

    public static void main(String[] args) {
        // 2147483647
        System.out.println(new Q556().nextGreaterElement(2147483476));
        // 21
        System.out.println(new Q556().nextGreaterElement(12));
        // 230412
        System.out.println(new Q556().nextGreaterElement(230241));
        // -1
        System.out.println(new Q556().nextGreaterElement(Integer.MAX_VALUE));
        // 132
        System.out.println(new Q556().nextGreaterElement(123));
        // -1
        System.out.println(new Q556().nextGreaterElement(21));
        // -1
        System.out.println(new Q556().nextGreaterElement(20));
        // -1
        System.out.println(new Q556().nextGreaterElement(200));
    }

    public int nextGreaterElement(int n) {
        char[] str = String.valueOf(n).toCharArray();
        char max = str[str.length - 1];
        for (int i = str.length - 2; i >= 0; i--) {
            if (str[i] > max) {
                max = str[i];
            } else if (str[i] < max) {
                int idx = i + 1;
                for (int j = i + 1; j < str.length; j++) {
                    if (str[j] > str[i] && str[j] < str[idx]) {
                        idx = j;
                    }
                }
                char c = str[i];
                str[i] = str[idx];
                str[idx] = c;
                Arrays.sort(str, i + 1, str.length);
                long v = Long.parseLong(new String(str));
                return v <= Integer.MAX_VALUE ? (int) v : -1;
            }
        }
        return -1;
    }
}
