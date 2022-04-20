package com.leo.leetcode.algorithm.q0800;

import java.util.HashSet;
import java.util.Set;

/**
 * 给你一个由若干单词组成的句子 sentence ，单词间由空格分隔。每个单词仅由大写和小写英文字母组成。
 * 请你将句子转换为 “山羊拉丁文（Goat Latin）”（一种类似于 猪拉丁文 - Pig Latin 的虚构语言）。山羊拉丁文的规则如下：
 * 1、如果单词以元音开头（'a', 'e', 'i', 'o', 'u'），在单词后添加"ma"。
 * 1）例如，单词 "apple" 变为 "applema" 。
 * 2、如果单词以辅音字母开头（即，非元音字母），移除第一个字符并将它放到末尾，之后再添加"ma"。
 * 例如，单词 "goat" 变为 "oatgma" 。
 * 3、根据单词在句子中的索引，在单词最后添加与索引相同数量的字母'a'，索引从 1 开始。
 * 例如，在第一个单词后添加 "a" ，在第二个单词后添加 "aa" ，以此类推。
 * 返回将 sentence 转换为山羊拉丁文后的句子。
 * 提示：
 * 1、1 <= sentence.length <= 150
 * 2、sentence 由英文字母和空格组成
 * 3、sentence 不含前导或尾随空格
 * 4、sentence 中的所有单词由单个空格分隔
 * 链接：https://leetcode-cn.com/problems/goat-latin
 */
public class Q824 {

    public static void main(String[] args) {
        // "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
        System.out.println(new Q824().toGoatLatin("I speak Goat Latin"));
        // "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
        System.out.println(new Q824().toGoatLatin("The quick brown fox jumped over the lazy dog"));
    }

    public String toGoatLatin(String sentence) {
        Set<Character> vowels = new HashSet<Character>() {{
            add('a');
            add('e');
            add('i');
            add('o');
            add('u');
            add('A');
            add('E');
            add('I');
            add('O');
            add('U');
        }};

        int n = sentence.length();
        int i = 0, cnt = 1;
        StringBuilder ans = new StringBuilder();
        while (i < n) {
            int j = i;
            while (j < n && sentence.charAt(j) != ' ') ++j;
            ++cnt;
            if (cnt != 2) ans.append(' ');
            if (vowels.contains(sentence.charAt(i))) {
                ans.append(sentence, i, j);
            } else {
                ans.append(sentence, i + 1, j);
                ans.append(sentence.charAt(i));
            }
            ans.append('m');
            for (int k = 0; k < cnt; ++k) ans.append('a');
            i = j + 1;
        }

        return ans.toString();
    }
}
