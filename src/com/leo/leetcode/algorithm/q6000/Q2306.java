package com.leo.leetcode.algorithm.q6000;

import java.util.Collections;
import java.util.HashSet;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 给你一个字符串数组 ideas 表示在公司命名过程中使用的名字列表。公司命名流程如下：
 * 1、从 ideas 中选择 2 个 不同 名字，称为 ideaA 和 ideaB 。
 * 2、交换 ideaA 和 ideaB 的首字母。
 * 3、如果得到的两个新名字 都 不在 ideas 中，那么 ideaA ideaB（串联 ideaA 和 ideaB ，中间用一个空格分隔）是一个有效的公司名字。
 * 4、否则，不是一个有效的名字。
 * 返回 不同 且有效的公司名字的数目。
 * 提示：
 * 1、2 <= ideas.length <= 5 * 10^4
 * 2、1 <= ideas[i].length <= 10
 * 3、ideas[i] 由小写英文字母组成
 * 4、ideas 中的所有字符串 互不相同
 * 链接：https://leetcode.cn/problems/naming-a-company
 */
public class Q2306 {

    public static void main(String[] args) {
        // 6
        System.out.println(new Q2306().distinctNames(stringToStringArray("[\"coffee\",\"donuts\",\"time\",\"toffee\"]")));
        // 0
        System.out.println(new Q2306().distinctNames(stringToStringArray("[\"lack\",\"back\"]")));
        // 6
        System.out.println(new Q2306().distinctNames(stringToStringArray("[\"coffee\",\"donuts\",\"time\"]")));
    }

    // https://leetcode.cn/problems/naming-a-company/solution/dui-mei-ge-idea-zhao-chu-ke-yi-pei-dui-d-zpv5/
    public long distinctNames(String[] ideas) {
        HashSet<String> set = new HashSet<>();
        long ret = 0;
        int[][] flags = new int[26][26];
        Collections.addAll(set, ideas);
        for (String idea : ideas) {
            char first = idea.charAt(0);
            for (char c = 'a'; c <= 'z'; c++) {
                String s = c + idea.substring(1);
                if (!set.contains(s)) flags[first - 'a'][c - 'a']++;
            }
        }
        for (String idea : ideas) {
            char first = idea.charAt(0);
            for (char c = 'a'; c <= 'z'; c++) {
                String s = c + idea.substring(1);
                if (!set.contains(s)) ret += flags[c - 'a'][first - 'a'];
            }
        }
        return ret;
    }
}
