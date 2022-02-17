package com.leo.leetcode.algorithm.q1300;

/**
 * 给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：
 * 字符（'a' - 'i'）分别用（'1' - '9'）表示。
 * 字符（'j' - 'z'）分别用（'10#' - '26#'）表示。
 * 返回映射之后形成的新字符串。
 * 题目数据保证映射始终唯一。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、s[i] 只包含数字（'0'-'9'）和 '#' 字符。
 * 3、s 是映射始终存在的有效字符串。
 * 链接：https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping
 */
public class Q1309 {

    public static void main(String[] args) {
        // "jkab"
        System.out.println(new Q1309().freqAlphabets("10#11#12"));
        // "acz"
        System.out.println(new Q1309().freqAlphabets("1326#"));
        // "y"
        System.out.println(new Q1309().freqAlphabets("25#"));
        // "abcdefghijklmnopqrstuvwxyz"
        System.out.println(new Q1309().freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"));
    }

    public String freqAlphabets(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c;
            if (i < s.length() - 2 && s.charAt(i + 2) == '#') {
                c = (char) ((s.charAt(i) - '0') * 10 + (s.charAt(i + 1) - '0') - 10 + 'j');
                i += 2;
            } else {
                c = (char) (s.charAt(i) - '1' + 'a');
            }
            sb.append(c);
        }
        return sb.toString();
    }
}
