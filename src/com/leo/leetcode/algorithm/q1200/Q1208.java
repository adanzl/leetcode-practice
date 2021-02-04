package com.leo.leetcode.algorithm.q1200;

/**
 * 给你两个长度相同的字符串，s 和 t。
 * 将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。
 * 用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。
 * 如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。
 * 如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。
 * <p>
 * 提示：
 * 1、1 <= s.length, t.length <= 10^5
 * 2、0 <= maxCost <= 10^6
 * 3、s 和 t 都只含小写英文字母。
 * <p>
 * 链接：https://leetcode-cn.com/problems/get-equal-substrings-within-budget
 */
public class Q1208 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q1208().equalSubstring("abcd", "bcdf", 3));
        // 1
        System.out.println(new Q1208().equalSubstring("abcd", "cdef", 3));
        // 1
        System.out.println(new Q1208().equalSubstring("abcd", "acde", 0));
    }

    public int equalSubstring(String s, String t, int maxCost) {
        int ret = 0, count = 0, len = 0, l = 0, r = 0, sLen = s.length();
        char[] ss = s.toCharArray(), st = t.toCharArray();
        int[] cost = new int[sLen];
        for (int i = 0; i < sLen; i++) cost[i] = Math.abs(ss[i] - st[i]);
        while (r < sLen) {
            len += cost[r];
            count++;
            if (len > maxCost) {
                len -= cost[l];
                l++;
                count--;
            }
            ret = Math.max(ret, count);
            r++;
        }
        return ret;
    }
}
