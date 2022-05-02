package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.*;

/**
 * 给你一个整数数组 cards ，其中 cards[i] 表示第 i 张卡牌的 值 。如果两张卡牌的值相同，则认为这一对卡牌 匹配 。
 * 返回你必须拿起的最小连续卡牌数，以使在拿起的卡牌中有一对匹配的卡牌。如果无法得到一对匹配的卡牌，返回 -1 。
 * 提示：
 * 1、1 <= cards.length <= 10^5
 * 2、0 <= cards[i] <= 10^6
 * 链接：https://leetcode-cn.com/problems/minimum-consecutive-cards-to-pick-up
 */
public class Q2260 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q2260().minimumCardPickup(stringToIntegerArray("[3,4,2,3,4,7]")));
        // -1
        System.out.println(new Q2260().minimumCardPickup(stringToIntegerArray("[1,0,5,3]")));
    }

    public int minimumCardPickup(int[] cards) {
        int ret = -1;
        Map<Integer, Integer> cMap = new HashMap<>();
        for (int i = 0; i < cards.length; i++) {
            int idx = cMap.getOrDefault(cards[i], -1);
            if (idx >= 0) {
                if (ret < 0) ret = i - idx + 1;
                else ret = Math.min(ret, i - idx + 1);
            }
            cMap.put(cards[i], i);
        }
        return ret;
    }
}
