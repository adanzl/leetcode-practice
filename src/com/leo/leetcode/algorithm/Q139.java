package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import org.junit.Test;

import java.util.Arrays;
import java.util.List;

public class Q139 {
    @Test
    public void TestOJ() {
        System.out.println(wordBreak("leetcode", LCUtil.stringToStringList("[\"leet\",\"code\"]"))); // t
        System.out.println(wordBreak("applepenapple", LCUtil.stringToStringList("[\"apple\",\"pen\"]"))); // t
        System.out.println(wordBreak("catsandog", LCUtil.stringToStringList("[\"cats\", \"dog\", \"sand\", \"and\", \"cat\"]"))); // f
        System.out.println(wordBreak("aaaaaaa", LCUtil.stringToStringList("[\"aaaa\", \"aaa\"]"))); // t
        System.out.println(wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
                , LCUtil.stringToStringList("[\"a\",\"aa\",\"aaa\",\"aaaa\",\"aaaaa\",\"aaaaaa\",\"aaaaaaa\",\"aaaaaaaa\",\"aaaaaaaaa\",\"aaaaaaaaaa\"]"))); // f
    }

    public boolean wordBreak(String s, List<String> wordDict) {
        int[] mark = new int[s.length() + 1];
        Arrays.fill(mark, -1);
        return fit(mark, s, 0, wordDict);
    }

    boolean fit(int[] mark, String s, int start, List<String> dict) {
        if (start >= s.length()) {
            return true;
        }
        if (mark[start] != -1) {
            return mark[start] == 1;
        }
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
