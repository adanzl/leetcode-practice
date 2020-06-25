package com.leo.leetcode.lcci;

/**
 * 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
 * 链接：https://leetcode-cn.com/problems/is-unique-lcci/
 */
public class Q0101 {
    public static void main(String[] args) {
        System.out.println(new Q0101().isUnique("leetcode")); // false
        System.out.println(new Q0101().isUnique("abc")); // true

    }

    public boolean isUnique(String aStr) {
        int[] mark = new int[128];
        char[] str = aStr.toCharArray();
        for (char c : str) {
            if (mark[c] == 1) return false;
            mark[c] = 1;
        }
        return true;
    }
}
