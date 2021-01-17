package com.leo.leetcode.algorithm.q0100;

import java.util.ArrayList;
import java.util.List;

/**
 * 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
 * 返回 s 所有可能的分割方案。
 * 链接：https://leetcode-cn.com/problems/palindrome-partitioning/
 */
public class Q131 {

    public static void main(String[] args) {
        System.out.println(new Q131().partition("aab")); // [["a","a","b"],["aa","b"]]
    }

    public List<List<String>> partition(String s) {
        List<List<String>> out = new ArrayList<>();
        boolean[][] marks = new boolean[s.length()][s.length()];
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                marks[j][i] = true;
            }
        }
        for (int i = 1; i < s.length(); i++) {
            for (int j = 0; j + i < s.length(); j++) {
                if (s.charAt(j) == s.charAt(j + i) && marks[j + 1][j + i - 1]) {
                    marks[j][j + i] = true;
                }
            }
        }
        dfs(s, 0, new ArrayList<>(), marks, out);
        return out;
    }

    void dfs(String str, int start, List<String> item, boolean[][] dp, List<List<String>> ans) {
        if (start == str.length()) {
            ans.add(new ArrayList<>(item));
            return;
        }
        for (int i = start + 1; i <= str.length(); i++) {
            if (dp[start][i - 1]) {
                item.add(str.substring(start, i));
                dfs(str, i, item, dp, ans);
                item.remove(item.size() - 1);
            }
        }
    }
}