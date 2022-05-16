package com.leo.leetcode.algorithm.q2200;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 给你一个下标从 0 开始的字符串 words ，其中 words[i] 由小写英文字符组成。
 * 在一步操作中，需要选出任一下标 i ，从 words 中 删除 words[i] 。其中下标 i 需要同时满足下述两个条件：
 * 1、0 < i < words.length
 * 2、words[i - 1] 和 words[i] 是 字母异位词 。
 * 只要可以选出满足条件的下标，就一直执行这个操作。
 * 在执行所有操作后，返回 words 。可以证明，按任意顺序为每步操作选择下标都会得到相同的结果。
 * 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。例如，"dacb" 是 "abdc" 的一个字母异位词。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、1 <= words[i].length <= 10
 * 3、words[i] 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/find-resultant-array-after-removing-anagrams
 */
public class Q2273 {
    public static void main(String[] args) {
        // ["abba","cd"]
        System.out.println(new Q2273().removeAnagrams(new String[]{"abba", "baba", "bbaa", "cd", "cd"}));
        // ["a","b","c","d","e"]
        System.out.println(new Q2273().removeAnagrams(new String[]{"a", "b", "c", "d", "e"}));
    }

    public List<String> removeAnagrams(String[] words) {
        List<String> res = new ArrayList<>();
        String preKey = "";
        for (String word : words) {
            int[] chars = new int[26];
            for (char c : word.toCharArray()) chars[c - 'a']++;
            String key = Arrays.toString(chars);
            if (preKey.equals(key)) continue;
            res.add(word);
            preKey = key;
        }
        return res;
    }
}
