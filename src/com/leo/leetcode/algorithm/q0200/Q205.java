package com.leo.leetcode.algorithm.q0200;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * 给定两个字符串 s 和 t ，判断它们是否是同构的。
 * 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
 * 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。
 * 不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
 * 提示：
 * 1、1 <= s.length <= 5 * 10^4
 * 2、t.length == s.length
 * 3、s 和 t 由任意有效的 ASCII 字符组成
 * 链接：https://leetcode-cn.com/problems/isomorphic-strings
 */
public class Q205 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q205().isIsomorphic("badc", "baba"));
        // true
        System.out.println(new Q205().isIsomorphic("egg", "add"));
        // false
        System.out.println(new Q205().isIsomorphic("foo", "bar"));
        // true
        System.out.println(new Q205().isIsomorphic("paper", "title"));
    }

    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> cMap = new HashMap<>();
        Set<Character> tSet = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            char c1 = s.charAt(i), c2 = t.charAt(i);
            if (cMap.containsKey(c1)) {
                if (cMap.get(c1) != c2) return false;
                else continue;
            }
            if (tSet.contains(c2)) return false;
            tSet.add(c2);
            cMap.put(c1, c2);
        }
        return true;
    }
}
