package com.leo.leetcode.algorithm.q2200;

/**
 * 给你一个下标从 0 开始长度为 n 的字符串 num ，它只包含数字。
 * 如果对于 每个 0 <= i < n 的下标 i ，都满足数位 i 在 num 中出现了 num[i]次，那么请你返回 true ，否则返回 false 。
 * 提示：
 * 1、n == num.length
 * 2、1 <= n <= 10
 * 3、num 只包含数字。
 * 链接：https://leetcode.cn/problems/check-if-number-has-equal-digit-count-and-digit-value
 */
public class Q2283 {
    public static void main(String[] args) {
        // true
        System.out.println(new Q2283().digitCount("1210"));
        // false
        System.out.println(new Q2283().digitCount("030"));
    }

    public boolean digitCount(String num) {
        int[] count = new int[10];
        char[] nums = num.toCharArray();
        for (char c : nums) {
            count[c - '0']++;
        }
        for (int i = 0; i < nums.length; i++) {
            if (count[i] != nums[i] - '0') {
                return false;
            }
        }
        return true;
    }
}
