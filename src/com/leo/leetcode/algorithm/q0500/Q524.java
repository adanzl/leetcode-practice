package com.leo.leetcode.algorithm.q0500;

import com.leo.utils.TestCase;

import java.util.List;

import static com.leo.utils.LCUtil.stringToStringList;

/**
 * 给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
 * 如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、1 <= dictionary.length <= 1000
 * 3、1 <= dictionary[i].length <= 1000
 * 4、s 和 dictionary[i] 仅由小写英文字母组成
 * 链接：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting
 */
public class Q524 {

    public static void main(String[] args) {
        // ntgcykxhdfescxxypyew
        TestCase tc = new TestCase("resources/Q524/Case001.txt");
        System.out.println(new Q524().findLongestWord(tc.getData(0), stringToStringList(tc.getData(1))));
        // apple
        System.out.println(new Q524().findLongestWord("abpcple", stringToStringList("[\"ale\",\"apple\",\"monkey\",\"plea\"]")));
        // apple
        System.out.println(new Q524().findLongestWord("abpplea", stringToStringList("[\"ale\",\"apple\",\"monkey\",\"plea\"]")));
        // a
        System.out.println(new Q524().findLongestWord("abpcplea", stringToStringList("[\"a\",\"b\",\"c\"]")));
    }

    public String findLongestWord(String s, List<String> dictionary) {
        dictionary.sort((o1, o2) -> o1.length() != o2.length() ? o2.length() - o1.length() : o1.compareTo(o2));
        for (String str : dictionary) {
            if (fit(s, str)) return str;
        }
        return "";
    }

    boolean fit(String s1, String s2) {
        int i = 0, j = 0;
        for (; i < s2.length() && j < s1.length(); i++, j++) {
            char c = s2.charAt(i);
            while (j < s1.length() && c != s1.charAt(j)) j++;
            if (j >= s1.length()) return false;
        }
        return i == s2.length();
    }
}
