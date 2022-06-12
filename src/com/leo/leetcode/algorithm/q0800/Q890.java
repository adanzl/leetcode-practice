package com.leo.leetcode.algorithm.q0800;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 你有一个单词列表 words 和一个模式  pattern，你想知道 words 中的哪些单词与模式匹配。
 * 如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。
 * （回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）
 * 返回 words 中与给定模式匹配的单词列表。
 * 你可以按任何顺序返回答案。
 * 提示：
 * 1、1 <= words.length <= 50
 * 2、1 <= pattern.length = words[i].length <= 20
 * 链接：https://leetcode.cn/problems/find-and-replace-pattern
 */
public class Q890 {

    public static void main(String[] args) {
        // ["mee","aqq"]
        System.out.println(new Q890().findAndReplacePattern(stringToStringArray("[\"abc\",\"deq\",\"mee\",\"aqq\",\"dkd\",\"ccc\"]"), "abb"));
    }

    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> ret = new ArrayList<>();
        for (String word : words) {
            Map<Character, Character> cMap = new HashMap<>(), pMap = new HashMap<>();
            boolean match = true;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i), p = pattern.charAt(i);
                if (cMap.containsKey(p) || pMap.containsKey(c)) {
                    if (cMap.getOrDefault(p, ' ') != c || pMap.getOrDefault(c, ' ') != p) {
                        match = false;
                        break;
                    }
                } else {
                    cMap.put(p, c);
                    pMap.put(c, p);
                }
            }
            if (match) ret.add(word);
        }
        return ret;
    }
}
