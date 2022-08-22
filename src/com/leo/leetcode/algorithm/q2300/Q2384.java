package com.leo.leetcode.algorithm.q2300;

/**
 * 给你一个仅由数字（0 - 9）组成的字符串 num 。
 * 请你找出能够使用 num 中数字形成的 最大回文 整数，并以字符串形式返回。该整数不含 前导零 。
 * 注意：
 * 1、你 无需 使用 num 中的所有数字，但你必须使用 至少 一个数字。
 * 2、数字可以重新排序。
 * 提示：
 * 1、1 <= num.length <= 10^5
 * 2、num 由数字（0 - 9）组成
 * 链接：https://leetcode.cn/problems/largest-palindromic-number
 */
public class Q2384 {

    public static void main(String[] args) {
        // "7449447
        System.out.println(new Q2384().largestPalindromic("444947137"));
        // "9"
        System.out.println(new Q2384().largestPalindromic("00009"));
    }

    public String largestPalindromic(String num) {
        int n = num.length();
        int[] cCount = new int[10];
        int single = -1;
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < n; i++) cCount[num.charAt(i) - '0']++;
        for (int i = 9; i >= 0; i--) {
            if (cCount[i] % 2 == 1) single = Math.max(single, i);
            if (i == 0 && ans.length() == 0) continue;
            for (int j = 0; j < cCount[i] / 2; j++) ans.append(i);
        }
        if (single >= 0) ans.append(single);
        for (int i = ans.length() - 1 - (single >= 0 ? 1 : 0); i >= 0; i--) {
            ans.append(ans.charAt(i));
        }
        return ans.toString();
    }
}
