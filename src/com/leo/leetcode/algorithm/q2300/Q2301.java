package com.leo.leetcode.algorithm.q2300;

import java.util.*;

import static com.leo.utils.LCUtil.stringToChar2dArray;

/**
 * 给你两个字符串 s 和 sub 。同时给你一个二维字符数组 mappings ，其中 mappings[i] = [old_i, new_i] 表示你可以替换 sub 中任意数目的 old_i 个字符，替换成 new_i 。
 * sub 中每个字符 不能 被替换超过一次。
 * 如果使用 mappings 替换 0 个或者若干个字符，可以将 sub 变成 s 的一个子字符串，请你返回 true，否则返回 false 。
 * 一个 子字符串 是字符串中连续非空的字符序列。
 * 提示：
 * 1、1 <= sub.length <= s.length <= 5000
 * 2、0 <= mappings.length <= 1000
 * 3、mappings[i].length == 2
 * 4、old_i != new_i
 * 5、s 和 sub 只包含大写和小写英文字母和数字。
 * 6、old_i 和 new_i 是大写、小写字母或者是个数字。
 * 链接：https://leetcode.cn/problems/match-substring-after-replacement
 */
public class Q2301 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q2301().matchReplacement("llllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrllllllllllllllllllllllllllllllllrlllllllllllllllllllllllllllllllll"
                , "lllllllllllllllllllllllllllllllll"
                , stringToChar2dArray("[[\"l\",\"a\"],[\"l\",\"b\"],[\"l\",\"c\"],[\"l\",\"d\"],[\"l\",\"e\"],[\"l\",\"f\"],[\"l\",\"g\"],[\"l\",\"h\"],[\"l\",\"i\"],[\"l\",\"j\"],[\"l\",\"k\"],[\"l\",\"m\"],[\"l\",\"n\"],[\"l\",\"o\"],[\"l\",\"p\"],[\"l\",\"q\"],[\"l\",\"s\"],[\"l\",\"t\"],[\"l\",\"u\"],[\"l\",\"v\"],[\"l\",\"w\"],[\"l\",\"x\"],[\"l\",\"y\"],[\"l\",\"z\"],[\"l\",\"0\"],[\"l\",\"1\"],[\"l\",\"2\"],[\"l\",\"3\"],[\"l\",\"4\"],[\"l\",\"5\"],[\"l\",\"6\"],[\"l\",\"7\"],[\"l\",\"8\"],[\"l\",\"9\"],[\"r\",\"a\"],[\"r\",\"b\"],[\"r\",\"c\"],[\"r\",\"d\"],[\"r\",\"e\"],[\"r\",\"f\"],[\"r\",\"g\"],[\"r\",\"h\"],[\"r\",\"i\"],[\"r\",\"j\"],[\"r\",\"k\"],[\"r\",\"m\"],[\"r\",\"n\"],[\"r\",\"o\"],[\"r\",\"p\"],[\"r\",\"q\"],[\"r\",\"s\"],[\"r\",\"t\"],[\"r\",\"u\"],[\"r\",\"v\"],[\"r\",\"w\"],[\"r\",\"x\"],[\"r\",\"y\"],[\"r\",\"z\"],[\"r\",\"0\"],[\"r\",\"1\"],[\"r\",\"2\"],[\"r\",\"3\"],[\"r\",\"4\"],[\"r\",\"5\"],[\"r\",\"6\"],[\"r\",\"7\"],[\"r\",\"8\"],[\"r\",\"9\"]]")));
        // true
        System.out.println(new Q2301().matchReplacement("fool3e7bar", "leet", stringToChar2dArray("[[\"e\",\"3\"],[\"t\",\"7\"],[\"t\",\"8\"]]")));
        // false
        System.out.println(new Q2301().matchReplacement("fooleetbar", "f00l", stringToChar2dArray("[[\"o\",\"0\"]]")));
        // true
        System.out.println(new Q2301().matchReplacement("Fool33tbaR", "leetd", stringToChar2dArray("[[\"e\",\"3\"],[\"t\",\"7\"],[\"t\",\"8\"],[\"d\",\"b\"],[\"p\",\"b\"]]")));
    }

    public boolean matchReplacement(String s, String sub, char[][] mappings) {
        char[] str = s.toCharArray();
        int len1 = s.length(), len2 = sub.length();
        Map<Character, Set<Character>> map = new HashMap<>();
        for (char[] mapping : mappings) {
            map.putIfAbsent(mapping[0], new HashSet<>());
            map.get(mapping[0]).add(mapping[1]);
        }
        boolean find = false;
        for (int i = 0; i <= len1 - len2; i++) {
            int j = 0;
            for (; j < len2; j++) {
                char c1 = str[i + j], c2 = sub.charAt(j);
                if (c1 != c2) {
                    if (!map.getOrDefault(c2, new HashSet<>()).contains(c1)) {
                        break;
                    }
                }
            }
            if (j == len2) {
                find = true;
                break;
            }
        }
        return find;
    }
}
