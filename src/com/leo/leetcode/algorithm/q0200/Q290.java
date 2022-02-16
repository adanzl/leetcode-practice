package com.leo.leetcode.algorithm.q0200;

import java.util.HashMap;
import java.util.Map;

/**
 * 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
 * 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
 * 说明:
 * 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
 * 链接：https://leetcode-cn.com/problems/word-pattern
 */
public class Q290 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q290().wordPattern("abba", "dog cat cat dog"));
        // false
        System.out.println(new Q290().wordPattern("abba", "dog cat cat fish"));
        // false
        System.out.println(new Q290().wordPattern("aaaa", "dog cat cat dog"));
        // false
        System.out.println(new Q290().wordPattern("abba", "dog dog dog dog"));
    }

    public boolean wordPattern(String pattern, String s) {
        Map<Character, String> cMap = new HashMap<>();
        Map<String, Character> sMap = new HashMap<>();
        String[] sArr = s.split(" ");
        if (sArr.length != pattern.length()) return false;
        for (int i = 0; i < pattern.length(); i++) {
            Character c0 = pattern.charAt(i);
            String str0 = sArr[i];
            Character c1 = sMap.get(str0);
            String str1 = cMap.get(c0);
            if (c1 == null && str1 == null) {
                cMap.put(c0, str0);
                sMap.put(str0, c0);
            } else if (c1 == null || c0.compareTo(c1) != 0 || str0.compareTo(str1) != 0) {
                return false;
            }
        }
        return true;
    }
}
