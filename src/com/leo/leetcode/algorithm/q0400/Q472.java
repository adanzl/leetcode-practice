package com.leo.leetcode.algorithm.q0400;

import java.util.*;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。
 * 连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。
 * 提示：
 * 1、1 <= words.length <= 10^4
 * 2、0 <= words[i].length <= 30
 * 3、words[i] 仅由小写字母组成
 * 4、0 <= sum(words[i].length) <= 10^5
 * 链接：https://leetcode.cn/problems/concatenated-words
 */
public class Q472 {

    public static void main(String[] args) {
        // ["catsdogcats","dogcatsdog","ratcatdogcat"]
        System.out.println(new Q472().findAllConcatenatedWordsInADict(stringToStringArray("[\"cat\",\"cats\",\"catsdogcats\",\"dog\",\"dogcatsdog\",\"hippopotamuses\",\"rat\",\"ratcatdogcat\"]")));
        // ["catdog"]
        System.out.println(new Q472().findAllConcatenatedWordsInADict(stringToStringArray("[\"cat\",\"dog\",\"catdog\"]")));
    }

    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        List<String> ret = new ArrayList<>();
        Arrays.sort(words, Comparator.comparingInt(String::length));
        // 前缀树
        Object[] tMap = new Object[27];
        for (String word : words) {
            if (dfs(tMap, word, 0, new boolean[word.length()])) ret.add(word);
            else {
                Object[] map = tMap;
                for (int i = 0; i < word.length(); i++) {
                    char c = word.charAt(i);
                    if (map[c - 'a'] == null) map[c - 'a'] = new Object[27];
                    map = (Object[]) map[c - 'a'];
                }
                map[26] = 'E';
            }
        }
        return ret;
    }

    // 前缀树搜索
    boolean dfs(Object[] tMap, String word, int start, boolean[] visited) {
        if (word.length() == start) return true;
        if (visited[start]) return false;
        visited[start] = true;
        Object[] node = tMap;
        for (int i = start; i < word.length(); i++) {
            char c = word.charAt(i);
            node = (Object[]) node[c - 'a'];
            if (node == null) return false;
            if (node[26] != null && dfs(tMap, word, i + 1, visited)) return true;
        }
        return false;
    }
}
