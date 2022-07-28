package com.leo.leetcode.algorithm.q2300;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个长度为 n 的整数数组 rolls 和一个整数 k 。你扔一个 k 面的骰子 n 次，骰子的每个面分别是 1 到 k ，其中第 i 次扔得到的数字是 rolls[i] 。
 * 请你返回 无法 从 rolls 中得到的 最短 骰子子序列的长度。
 * 扔一个 k 面的骰子 len 次得到的是一个长度为 len 的 骰子子序列 。
 * 注意 ，子序列只需要保持在原数组中的顺序，不需要连续。
 * 提示：
 * 1、n == rolls.length
 * 2、1 <= n <= 10^5
 * 3、1 <= rolls[i] <= k <= 10^5
 * 链接：https://leetcode.cn/problems/shortest-impossible-sequence-of-rolls
 */
public class Q2350 {

    public static void main(String[] args) {
        // 93
        System.out.println(new Q2350().shortestSequence(stringToIntegerArray("[2,2,2,2,2,2,1,2,2,2,1,1,1,2,2,2,2,1,2,1,1,2,2,2,2,1,1,1,1,2,1,1,2,1,1,2,2,1,1,1,2,1,1,1,2,2,1,2,1,2,1,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,2,1,2,1,2,1,2,2,1,1,2,1,1,1,1,2,2,2,2,1,2,1,1,2,1,2,1,1,2,2,1,2,1,1,2,2,2,1,2,2,1,1,2,2,1,2,1,1,2,1,1,1,1,2,2,1,2,2,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,1,1,2,1,1,1,1,2,1,1,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,1,1,2,1,2,1,2,2,2,2,2,2,1,1,2,1,2,2,2,2,1,2,1,2,1,2,1,1,1,2,1,1,1,2,1,1,2,2,1,1,1,1,2,2,2,2,1,2,1,1,1,1,1,2,1,1,1,1,2,2,1,1,1,2,2,1,2,1,2,1,1,2,2,2,1,1,2,1,2,1,2,2,1,1,1,1,2,2,2,1,1,2,2,1,1,1,1,1,1,2,1,1,2,2,2,1,1,2,1,2,2,2,2,2]"), 2));
        // 3
        System.out.println(new Q2350().shortestSequence(stringToIntegerArray("[4,2,1,2,3,3,2,4,1]"), 4));
        // 11
        System.out.println(new Q2350().shortestSequence(stringToIntegerArray("[2,1,4,2,1,1,2,2,2,3,2,1,4,2,4,2,2,1,1,4,2,4,3,2,3,4,1,3,4,2,1,1,2,3,1,4,2,2,3,4,1,2,1,1,1,1,1,4,3,2,3,4,1,4,1,3,3,2,1,4,3,4,2,3,2]"), 4));
        // 2
        System.out.println(new Q2350().shortestSequence(stringToIntegerArray("[1,1,2,2]"), 2));
        // 1
        System.out.println(new Q2350().shortestSequence(stringToIntegerArray("[1,1,3,2,2,2,3,3]"), 4));
    }

    public int shortestSequence(int[] rolls, int k) {
        Set<Integer> s = new HashSet<>();
        int ret = 0;
        for (int roll : rolls) {
            s.add(roll);
            if (s.size() == k) {
                s.clear();
                ret++;
            }
        }
        return ret + 1;
    }
}
