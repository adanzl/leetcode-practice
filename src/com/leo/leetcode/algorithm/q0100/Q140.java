package com.leo.leetcode.algorithm.q0100;

import static com.leo.utils.LCUtil.stringToStringList;

import java.util.*;


/**
 * 串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
 * <p>
 * 说明：
 * 1、分隔时可以重复使用字典中的单词。
 * 2、你可以假设字典中没有重复的单词。
 * <p>
 * 链接：https://leetcode-cn.com/problems/word-break-ii
 */
public class Q140 {

    public static void main(String[] args) {
        // [a b]
        System.out.println(new Q140().wordBreak("ab", stringToStringList("[\"a\", \"b\"]")));
        // []
        System.out.println(new Q140().wordBreak("catsandog", stringToStringList("[\"cats\", \"dog\", \"sand\", \"and\", \"cat\"]")));
        // ["cats and dog", "cat sand dog"]
        System.out.println(new Q140().wordBreak("catsanddog", stringToStringList("[\"cat\", \"cats\", \"and\", \"sand\", \"dog\"]")));
        // ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
        System.out.println(new Q140().wordBreak("pineapplepenapple", stringToStringList("[\"apple\", \"pen\", \"applepen\", \"pine\", \"pineapple\"]")));
    }

    public List<String> wordBreak(String s, List<String> wordDict) {
        char[] str = s.toCharArray();
        int maxDict = 0;
        Set<String> words = new HashSet<>();
        for (String word : wordDict) {
            maxDict = Math.max(word.length(), maxDict);
            words.add(word);
        }
        List<List<int[]>> marks = new ArrayList<>(s.length());
        for (int i = 0; i < str.length; i++) marks.add(null);
        for (int i = 0; i < str.length; i++) {
            for (int j = i; j >= Math.max(0, i - maxDict); j--) {
                if (j != 0 && marks.get(j - 1) == null) continue;
                String sub = s.substring(j, i + 1);
                if (words.contains(sub)) {
                    if (marks.get(i) == null) marks.set(i, new ArrayList<>());
                    if (j == 0) marks.get(i).add(new int[]{-1, j, i + 1});
                    else marks.get(i).add(new int[]{j - 1, j, i + 1});
                }
            }
        }
        List<String> ret = new ArrayList<>();
        if (marks.get(str.length - 1) != null) getPath(s, marks, str.length - 1, new LinkedList<>(), ret);
        return ret;
    }

    void getPath(String s, List<List<int[]>> marks, int index, LinkedList<String> pre, List<String> out) {
        for (int[] next : marks.get(index)) {
            if (next[0] == -1) {
                pre.addFirst(s.substring(next[1], next[2]));
                out.add(String.join(" ", pre));
                return;
            } else {
                LinkedList<String> path = new LinkedList<>(pre);
                path.addFirst(s.substring(next[1], next[2]));
                getPath(s, marks, next[0], path, out);
            }
        }
    }

}
