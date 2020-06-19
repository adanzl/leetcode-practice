package com.leo.leetcode.algorithm;

/**
 * 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
 * '.' 匹配任意单个字符
 * '*' 匹配零个或多个前面的那一个元素
 * 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
 * 说明:
 * s 可能为空，且只包含从 a-z 的小写字母。
 * p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
 * <p>
 * 链接：https://leetcode-cn.com/problems/regular-expression-matching
 */
public class Q10 {

    public static void main(String[] args) {
        System.out.println(new Q10().isMatch("aa", "a")); // false
        System.out.println(new Q10().isMatch("aa", "a*")); // true
        System.out.println(new Q10().isMatch("ab", ".*")); // true
        System.out.println(new Q10().isMatch("aab", "c*a*b")); // true
        System.out.println(new Q10().isMatch("mississippi", "mis*is*p*.")); // false
    }

    public boolean isMatch(String s, String p) {
        if (p.isEmpty()) return s.isEmpty();
        boolean first_match = (!s.isEmpty() && (p.charAt(0) == s.charAt(0) || p.charAt(0) == '.'));
        if (p.length() >= 2 && p.charAt(1) == '*')
            return (isMatch(s, p.substring(2)) || (first_match && isMatch(s.substring(1), p)));
        else return first_match && isMatch(s.substring(1), p.substring(1));
    }
}
