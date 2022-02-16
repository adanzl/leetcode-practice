package com.leo.leetcode.algorithm.q0700;

import java.util.ArrayList;
import java.util.List;

/**
 * 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
 * 返回一个表示每个字符串片段的长度的列表。
 * 提示：
 * 1、S的长度在[1, 500]之间。
 * 2、S只包含小写字母 'a' 到 'z' 。
 * 链接：https://leetcode-cn.com/problems/partition-labels/
 */
public class Q763 {

    public static void main(String[] args) {
        // [9,7,8]
        System.out.println(new Q763().partitionLabels("ababcbacadefegdehijhklij"));
    }

    public List<Integer> partitionLabels(String s) {
        List<Integer> ret = new ArrayList<>();
        int[] flag = new int[26];
        int len = s.length(), l = 0, r = 0;
        for (int i = 0; i < len; i++) flag[s.charAt(i) - 'a'] = i;
        for (int i = 0; i < len; i++) {
            char c = s.charAt(i);
            r = Math.max(r, flag[c - 'a']);
            if (i == r) {
                ret.add(r - l + 1);
                l = i + 1;
                r = l;
            }
        }
        return ret;
    }
}
