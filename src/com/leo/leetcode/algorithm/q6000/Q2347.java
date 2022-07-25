package com.leo.leetcode.algorithm.q6000;

import static com.leo.utils.LCUtil.stringToCharArray;
import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 ranks 和一个字符数组 suit 。你有 5 张扑克牌，第 i 张牌大小为 ranks[i] ，花色为 suits[i] 。
 * 下述是从好到坏你可能持有的 手牌类型 ：
 * 1、"Flush"：同花，五张相同花色的扑克牌。
 * 2、"Three of a Kind"：三条，有 3 张大小相同的扑克牌。
 * 3、"Pair"：对子，两张大小一样的扑克牌。
 * 4、"High Card"：高牌，五张大小互不相同的扑克牌。
 * 请你返回一个字符串，表示给定的 5 张牌中，你能组成的 最好手牌类型 。
 * 注意：返回的字符串 大小写 需与题目描述相同。
 * 提示：
 * 1、ranks.length == suits.length == 5
 * 2、1 <= ranks[i] <= 13
 * 3、'a' <= suits[i] <= 'd'
 * 4、任意两张扑克牌不会同时有相同的大小和花色。
 * 链接：https://leetcode.cn/problems/best-poker-hand
 */
public class Q2347 {

    public static void main(String[] args) {
        // Flush
        System.out.println(new Q2347().bestHand(stringToIntegerArray("[13,2,3,1,9]"), stringToCharArray("[\"a\",\"a\",\"a\",\"a\",\"a\"]")));
        // Three of a Kind
        System.out.println(new Q2347().bestHand(stringToIntegerArray("[4,4,2,4,4]"), stringToCharArray("[\"d\",\"a\",\"a\",\"b\",\"c\"]")));
        // Pair
        System.out.println(new Q2347().bestHand(stringToIntegerArray("[10,10,2,12,9]"), stringToCharArray("[\"a\",\"b\",\"c\",\"a\",\"d\"]")));
    }

    public String bestHand(int[] ranks, char[] suits) {
        String r1 = "Flush", r2 = "Three of a Kind", r3 = "Pair", r4 = "High Card";
        boolean fit = true;
        for (int i = 1; i < suits.length; i++) {
            if (suits[i] != suits[i - 1]) {
                fit = false;
                break;
            }
        }
        if (fit) return r1;
        int[] count = new int[14];
        for (int r : ranks) {
            count[r]++;
            if (count[r] >= 3) return r2;
        }
        count = new int[14];
        for (int r : ranks) {
            count[r]++;
            if (count[r] >= 2) return r3;
        }
        return r4;
    }
}
