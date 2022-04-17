package com.leo.leetcode.algorithm.q0800;

import java.util.*;

/**
 * 给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。
 * 题目保证至少有一个词不在禁用列表中，而且答案唯一。
 * 禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。
 * 提示：
 * 1、1 <= 段落长度 <= 1000
 * 2、0 <= 禁用单词个数 <= 100
 * 3、1 <= 禁用单词长度 <= 10
 * 4、答案是唯一的, 且都是小写字母 (即使在 paragraph 里是大写的，即使是一些特定的名词，答案都是小写的。)
 * 5、paragraph 只包含字母、空格和下列标点符号!?',;.
 * 6、不存在没有连字符或者带有连字符的单词。
 * 7、单词里只包含字母，不会出现省略号或者其他标点符号。
 * 链接：https://leetcode-cn.com/problems/most-common-word
 */
public class Q819 {

    public static void main(String[] args) {
        // ball
        System.out.println(new Q819().mostCommonWord("Bob. hIt, baLl", new String[]{"hit", "bob"}));
        // ball
        System.out.println(new Q819().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", new String[]{"hit"}));
    }

    public String mostCommonWord(String paragraph, String[] banned) {
        String str = paragraph.replaceAll("[^a-zA-Z\\s]", " ");
        Set<String> bannedSet = new HashSet<>();
        Map<String, Integer> cMap = new HashMap<>();
        for (String s : banned) bannedSet.add(s.toLowerCase());
        String[] words = str.split(" ");
        int max = 0;
        String ret = "";
        for (String word : words) {
            String lWord = word.toLowerCase();
            if (lWord.length() == 0 || bannedSet.contains(lWord)) continue;
            int cnt = cMap.getOrDefault(lWord, 0) + 1;
            cMap.put(lWord, cnt);
            if (cnt > max) {
                max = cnt;
                ret = lWord;
            }
        }
        return ret;
    }
}
