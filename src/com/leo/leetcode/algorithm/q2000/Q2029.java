package com.leo.leetcode.algorithm.q2000;

import com.leo.utils.LCUtil;

/**
 * Alice 和 Bob 再次设计了一款新的石子游戏。
 * 现有一行 n 个石子，每个石子都有一个关联的数字表示它的价值。给你一个整数数组 stones ，其中 stones[i] 是第 i 个石子的价值。
 * Alice 和 Bob 轮流进行自己的回合，Alice 先手。每一回合，玩家需要从 stones 中移除任石子。
 * 如果玩家移除石子后，导致 所有已移除石子 的价值 总和 可以被 3 整除，那么该玩家就 输掉游戏 。
 * 如果不满足上一条，且移除后没有任何剩余的石子，那么 Bob 将会直接获胜（即便是在 Alice 的回合）。
 * 假设两位玩家均采用 最佳 决策。如果 Alice 获胜，返回 true ；如果 Bob 获胜，返回 false 。
 * 链接：https://leetcode-cn.com/problems/stone-game-ix
 */

public class Q2029 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q2029().stoneGameIX(LCUtil.stringToIntegerArray("[2,1]")));
        // false
        System.out.println(new Q2029().stoneGameIX(LCUtil.stringToIntegerArray("[2]")));
        // false
        System.out.println(new Q2029().stoneGameIX(LCUtil.stringToIntegerArray("[5,1,2,4,3]")));
    }

    public boolean stoneGameIX(int[] stones) {
        int[] s = new int[3];
        for (int val : stones) s[val % 3]++;
        if (s[0] % 2 == 0) return s[1] >= 1 && s[2] >= 1;
        return s[1] - s[2] > 2 || s[2] - s[1] > 2;
    }
}
