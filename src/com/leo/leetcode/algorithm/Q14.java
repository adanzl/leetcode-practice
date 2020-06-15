package com.leo.leetcode.algorithm;

/**
 * 编写一个函数来查找字符串数组中的最长公共前缀。
 * 如果不存在公共前缀，返回空字符串 ""。
 * 链接：https://leetcode-cn.com/problems/longest-common-prefix
 */
public class Q14 {
    public static void main(String[] args) {
        System.out.println(new Q14().longestCommonPrefix(new String[]{"flower", "flow", "flight"})); // "fl"
        System.out.println(new Q14().longestCommonPrefix(new String[]{"dog", "racecar", "car"})); // ""
    }

    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        StringBuilder sb = new StringBuilder();
        String s = strs[0];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            for (String str : strs) {
                if (str.length() < i + 1 || str.charAt(i) != c)
                    return sb.toString();
            }
            sb.append(c);
        }
        return sb.toString();
    }
}
