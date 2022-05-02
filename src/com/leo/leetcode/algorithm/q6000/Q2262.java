package com.leo.leetcode.algorithm.q6000;

import java.util.HashMap;
import java.util.Map;

/**
 * 字符串的 引力 定义为：字符串中 不同 字符的数量。
 * 例如，"abbca" 的引力为 3 ，因为其中有 3 个不同字符 'a'、'b' 和 'c' 。
 * 给你一个字符串 s ，返回 其所有子字符串的总引力 。
 * 子字符串 定义为：字符串中的一个连续字符序列。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 由小写英文字母组成
 * 链接：https://leetcode-cn.com/problems/total-appeal-of-a-string
 */
public class Q2262 {

    public static void main(String[] args) {
        // 8
        System.out.println(new Q2262().appealSum("abb"));
        // 16
        System.out.println(new Q2262().appealSum("abbc"));
        // 28
        System.out.println(new Q2262().appealSum("abbca"));
        // 20
        System.out.println(new Q2262().appealSum("code"));
    }

    public long appealSum(String s) {
        char[] str = s.toCharArray();
        int n = str.length;
        long ret = 0, last = 0;
        Map<Character, Integer> lastIdx = new HashMap<>();
        for (int i = 0; i < n; i++) {
            char c = str[i];
            int idx = lastIdx.getOrDefault(c, -1);
            last += i - idx;
            ret += last;
            lastIdx.put(c, i);
        }
        return ret;
    }
}
