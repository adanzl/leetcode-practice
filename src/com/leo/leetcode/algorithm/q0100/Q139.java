package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;

import java.util.Arrays;
import java.util.List;

/**
 * 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
 * 说明：
 * 拆分时可以重复使用字典中的单词。
 * 你可以假设字典中没有重复的单词。
 * 链接：https://leetcode-cn.com/problems/word-break
 */
public class Q139 {

    public static void main(String[] args) {
        new Q139().TestOJ();
    }

    public void TestOJ() {
        System.out.println(wordBreak("leetcode", LCUtil.stringToStringList("[\"leet\",\"code\"]"))); // t
        System.out.println(wordBreak("applepenapple", LCUtil.stringToStringList("[\"apple\",\"pen\"]"))); // t
        System.out.println(wordBreak("catsandog", LCUtil.stringToStringList("[\"cats\", \"dog\", \"sand\", \"and\", \"cat\"]"))); // f
        System.out.println(wordBreak("aaaaaaa", LCUtil.stringToStringList("[\"aaaa\", \"aaa\"]"))); // t
        System.out.println(wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                , LCUtil.stringToStringList("[\"a\",\"aa\",\"aaa\",\"aaaa\",\"aaaaa\",\"aaaaaa\",\"aaaaaaa\",\"aaaaaaaa\",\"aaaaaaaaa\",\"aaaaaaaaaa\"]"))); // f
    }

    public boolean wordBreak(String s, List<String> wordDict) {
        int[] mark = new int[s.length() + 1];
        Arrays.fill(mark, -1);
        return fit(mark, s, 0, wordDict);
    }

    boolean fit(int[] mark, String s, int start, List<String> dict) {
        if (start >= s.length()) return true;
        if (mark[start] != -1) return mark[start] == 1;
        for (int i = start; i <= s.length(); i++) {
            String str = s.substring(start, i);
            if (dict.contains(str)) {
                if (fit(mark, s, i, dict)) {
                    mark[i] = 1;
                    return true;
                }
            }
        }
        mark[start] = 0;
        return false;
    }
}
