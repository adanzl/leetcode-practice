package com.leo.leetcode.algorithm.q0700;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。
 * 若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。
 * 提示：
 * 1、1 <= words.length <= 1000
 * 2、1 <= words[i].length <= 30
 * 3、所有输入的字符串 words[i] 都只包含小写字母。
 * 链接：https://leetcode-cn.com/problems/longest-word-in-dictionary
 */
public class Q720 {

    public static void main(String[] args) {
        // world
        System.out.println(new Q720().longestWord(stringToStringArray("[\"w\",\"wo\",\"wor\",\"worl\", \"world\"]")));
        // w
        System.out.println(new Q720().longestWord(stringToStringArray("[\"w\"]")));
        // ""
        System.out.println(new Q720().longestWord(stringToStringArray("[\"ww\"]")));
        // wor
        System.out.println(new Q720().longestWord(stringToStringArray("[\"w\",\"wo\",\"wor\", \"world\"]")));
        // apple
        System.out.println(new Q720().longestWord(
                stringToStringArray("[\"a\", \"banana\", \"app\", \"appl\", \"ap\", \"apply\", \"apple\"]")));
    }

    public String longestWord(String[] words) {
        Arrays.sort(words, ((o1, o2) -> o1.length() != o2.length() ? o1.length() - o2.length() : o1.compareTo(o2)));
        CharNode root = new CharNode(' ');
        String ret = "";
        for (String word : words) {
            if (putCharNode(root, word) && word.length() > ret.length())
                ret = word;
        }
        return ret;
    }

    boolean putCharNode(CharNode root, String word) {
        CharNode p = root;
        int len = word.length() - 1;
        for (int i = 0; i < len; i++) {
            p = p.next.get(word.charAt(i));
            if (p == null)
                return false;
        }
        p.next.put(word.charAt(len), new CharNode(word.charAt(len)));
        return true;
    }

    static class CharNode {
        CharNode(char c) {
            this.c = c;
        }

        char c;
        Map<Character, CharNode> next = new HashMap<>();
    }
}
