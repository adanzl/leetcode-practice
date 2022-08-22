package com.leo.leetcode.algorithm.q2300;

/**
 * 给你一个二进制字符串 s 。在一秒之中，所有 子字符串 "01" 同时 被替换成 "10" 。这个过程持续进行到没有 "01" 存在。
 * 请你返回完成这个过程所需要的秒数。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、s[i] 要么是 '0' ，要么是 '1' 。
 * 链接：https://leetcode.cn/problems/time-needed-to-rearrange-a-binary-string
 */
public class Q2380 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q2380().secondsToRemoveOccurrences("0110101"));
        // 0
        System.out.println(new Q2380().secondsToRemoveOccurrences("11100"));
        // 0
        System.out.println(new Q2380().secondsToRemoveOccurrences("111"));
        // 0
        System.out.println(new Q2380().secondsToRemoveOccurrences("000"));
    }


    public int secondsToRemoveOccurrences(String s) {
        int pre = 0, n = s.length(), ans = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0') pre++;
            else if (pre > 0) ans = Math.max(pre, ans + 1);
        }
        return ans;
    }
}
