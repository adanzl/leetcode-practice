package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.*;

/**
 * 给你一个下标从 0 开始的字符串 s ，该字符串仅由小写英文字母组成，s 中的每个字母都 恰好 出现 两次 。另给你一个下标从 0 开始、长度为 26 的的整数数组 distance 。
 * 字母表中的每个字母按从 0 到 25 依次编号（即，'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25）。
 * 在一个 匀整 字符串中，第 i 个字母的两次出现之间的字母数量是 distance[i] 。如果第 i 个字母没有在 s 中出现，那么 distance[i] 可以 忽略 。
 * 如果 s 是一个 匀整 字符串，返回 true ；否则，返回 false 。
 * 提示：
 * 1、2 <= s.length <= 52
 * 2、s 仅由小写英文字母组成
 * 3、s 中的每个字母恰好出现两次
 * 4、distance.length == 26
 * 5、0 <= distance[i] <= 50
 * 链接：https://leetcode.cn/problems/check-distances-between-same-letters
 */
public class Q2399 {
    public static void main(String[] args) {
        // true
        System.out.println(new Q2399().checkDistances("abaccb", stringToIntegerArray("[1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")));
        // false
        System.out.println(new Q2399().checkDistances("aa", stringToIntegerArray("[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")));
    }

    public boolean checkDistances(String s, int[] distance) {
        int n = s.length();
        int[] preIdx = new int[26];
        Arrays.fill(preIdx, -1);
        for (int i = 0; i < n; i++) {
            int v = s.charAt(i) - 'a';
            if (preIdx[v] == -1) {
                preIdx[v] = i;
            } else {
                if (i - preIdx[v] - 1 != distance[v]) return false;
            }
        }
        return true;
    }
}
