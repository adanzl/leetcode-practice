package com.leo.leetcode.algorithm.q1400;

/**
 * 给你一个字符串 sentence 作为句子并指定检索词为 searchWord ，其中句子由若干用 单个空格 分隔的单词组成。请你检查检索词 searchWord 是否为句子 sentence 中任意单词的前缀。
 * 如果 searchWord 是某一个单词的前缀，则返回句子 sentence 中该单词所对应的下标（下标从 1 开始）。如果 searchWord 是多个单词的前缀，则返回匹配的第一个单词的下标（最小下标）。
 * 如果 searchWord 不是任何单词的前缀，则返回 -1 。
 * 字符串 s 的 前缀 是 s 的任何前导连续子字符串。
 * 提示：
 * 1、1 <= sentence.length <= 100
 * 2、1 <= searchWord.length <= 10
 * 3、sentence 由小写英文字母和空格组成。
 * 4、searchWord 由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence
 */
public class Q1455 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q1455().isPrefixOfWord("i love eating burger", "burg"));
        // 2
        System.out.println(new Q1455().isPrefixOfWord("this problem is an easy problem", "pro"));
        // -1
        System.out.println(new Q1455().isPrefixOfWord("i am tired", "you"));
    }

    public int isPrefixOfWord(String sentence, String searchWord) {
        String[] words = sentence.split(" ");
        for (int i = 0; i < words.length; i++) {
            if (words[i].startsWith(searchWord)) return i + 1;
        }
        return -1;
    }
}
