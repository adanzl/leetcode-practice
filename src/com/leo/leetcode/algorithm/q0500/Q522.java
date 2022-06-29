package com.leo.leetcode.algorithm.q0500;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 给定字符串列表 strs ，返回其中 最长的特殊序列 。如果最长特殊序列不存在，返回 -1 。
 * 特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。
 * s 的 子序列可以通过删去字符串 s 中的某些字符实现。
 * 例如，"abc" 是 "aebdc" 的子序列，因为您可以删除 "aebdc" 中的下划线字符来得到 "abc" 。
 * "aebdc" 的子序列还包括 "aebdc" 、 "aeb" 和 "" (空字符串)。
 * 提示:
 * 1、2 <= strs.length <= 50
 * 2、1 <= strs[i].length <= 10
 * 3、strs[i] 只包含小写英文字母
 * 链接：https://leetcode.cn/problems/longest-uncommon-subsequence-ii
 */
public class Q522 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q522().findLUSLength(stringToStringArray("[\"aabbcc\", \"aabbcc\",\"cb\"]")));
        // 3
        System.out.println(new Q522().findLUSLength(stringToStringArray("[\"aba\",\"cdc\",\"eae\"]")));
        // -1
        System.out.println(new Q522().findLUSLength(stringToStringArray("[\"aaa\",\"aaa\",\"aa\"]")));
    }

    public int findLUSLength(String[] strs) {
        int n = strs.length;
        Arrays.sort(strs, (a, b) -> b.length() - a.length());
        outer:
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                int p1 = 0, p2 = 0;
                while (p1 < strs[i].length() && p2 < strs[j].length()) {
                    if (strs[i].charAt(p1) == strs[j].charAt(p2)) p1++;
                    p2++;
                }
                if (p1 == strs[i].length()) continue outer;
            }
            return strs[i].length();
        }
        return -1;
    }
}
