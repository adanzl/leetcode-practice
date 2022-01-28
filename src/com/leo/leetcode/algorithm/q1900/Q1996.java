package com.leo.leetcode.algorithm.q1900;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击 和 防御 。
 * 给你一个二维整数数组 properties ，其中 properties[i] = [attack_i, defense_i] 表示游戏中第 i 个角色的属性。
 * 如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为 弱角色 。
 * 更正式地，如果认为角色 i 弱于 存在的另一个角色 j ，那么 attack_j > attack_i 且 defense_j > defense_i 。
 * 返回 弱角色 的数量。
 * <p>
 * 链接：https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game
 */
public class Q1996 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q1996().numberOfWeakCharacters(stringToInt2dArray("[[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]")));
        // 0
        System.out.println(new Q1996().numberOfWeakCharacters(stringToInt2dArray("[[5,5],[6,3],[3,6]]")));
        // 1
        System.out.println(new Q1996().numberOfWeakCharacters(stringToInt2dArray("[[2,2],[3,3]]")));
        // 1
        System.out.println(new Q1996().numberOfWeakCharacters(stringToInt2dArray("[[1,5],[10,4],[4,3]]")));
    }

    public int numberOfWeakCharacters(int[][] properties) {
        Arrays.sort(properties, (o1, o2) -> o2[0] != o1[0] ? o2[0] - o1[0] : o1[1] - o2[1]);
        int ret = 0, maxY = 0;
        for (int[] p : properties) {
            if (maxY > p[1]) ret++;
            else maxY = p[1];
        }
        return ret;
    }
}
