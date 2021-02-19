package com.leo.leetcode.algorithm.q0000;

import com.leo.utils.TestCase;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
 * 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
 * <p>
 * 链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
 */
public class Q30 {

    public static void main(String[] args) {
        TestCase tc1;
        // [0]
        System.out.println(new Q30().findSubstring("a", stringToStringArray("[\"a\"]")));
        // [8]
        tc1 = new TestCase("resources/Q30/Case005");
        System.out.println(new Q30().findSubstring(tc1.getData(0), stringToStringArray(tc1.getData(1))));
        // [0,9]
        tc1 = new TestCase("resources/Q30/Case001");
        System.out.println(new Q30().findSubstring(tc1.getData(0), stringToStringArray(tc1.getData(1))));
        // []
        tc1 = new TestCase("resources/Q30/Case002");
        System.out.println(new Q30().findSubstring(tc1.getData(0), stringToStringArray(tc1.getData(1))));
        // []
        tc1 = new TestCase("resources/Q30/Case003");
        System.out.println(new Q30().findSubstring(tc1.getData(0), stringToStringArray(tc1.getData(1))));
        // [6,9,12]
        tc1 = new TestCase("resources/Q30/Case004");
        System.out.println(new Q30().findSubstring(tc1.getData(0), stringToStringArray(tc1.getData(1))));
    }


    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> out = new ArrayList<>();
        if (words.length == 0) return out;
        int wLen = words[0].length(), pLen = wLen * words.length;
        Map<String, Integer> dict = new HashMap<>();
        for (String word : words) dict.put(word, dict.getOrDefault(word, 0) + 1);
        for (int i = 0; i < wLen; i++) {
            int l = i, r = i + pLen - 1;
            while (r < s.length()) {
                Map<String, Integer> tmp = new HashMap<>();
                int p = l, size = 0;
                while (p <= r) {
                    String str = s.substring(p, p + wLen);
                    int c = tmp.getOrDefault(str, 0);
                    if (c + 1 > dict.getOrDefault(str, 0)) break;
                    tmp.put(str, c + 1);
                    ++size;
                    p += wLen;
                }
                if (size == words.length) out.add(l);
                r += wLen;
                l += wLen;
            }
        }
        return out;
    }
}