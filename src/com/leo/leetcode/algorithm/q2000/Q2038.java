package com.leo.leetcode.algorithm.q2000;

/**
 * 总共有 n 个颜色片段排成一列，每个颜色片段要么是 'A' 要么是 'B' 。
 * 给你一个长度为 n 的字符串 colors ，其中 colors[i] 表示第 i 个颜色片段的颜色。
 * Alice 和 Bob 在玩一个游戏，他们 轮流 从这个字符串中删除颜色。Alice 先手 。
 * 1、如果一个颜色片段为 'A' 且 相邻两个颜色 都是颜色 'A' ，那么 Alice 可以删除该颜色片段。Alice 不可以 删除任何颜色 'B' 片段。
 * 2、如果一个颜色片段为 'B' 且 相邻两个颜色 都是颜色 'B' ，那么 Bob 可以删除该颜色片段。Bob 不可以 删除任何颜色 'A' 片段。
 * 3、Alice 和 Bob 不能 从字符串两端删除颜色片段。
 * 4、如果其中一人无法继续操作，则该玩家 输 掉游戏且另一玩家 获胜 。
 * 5、假设 Alice 和 Bob 都采用最优策略，如果 Alice 获胜，请返回 true，否则 Bob 获胜，返回 false。
 * 提示：
 * 1、1 <= colors.length <= 10^5
 * 2、colors 只包含字母 'A' 和 'B'
 * 链接：https://leetcode-cn.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color
 */
public class Q2038 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q2038().winnerOfGame("AAABABB"));
        // false
        System.out.println(new Q2038().winnerOfGame("AA"));
        // false
        System.out.println(new Q2038().winnerOfGame("ABBBBBBBAAA"));
    }

    public boolean winnerOfGame(String colors) {
        int countA = 0, countB = 0, sa = 0, sb = 0;
        for (int i = 0; i < colors.length(); i++) {
            if (colors.charAt(i) == 'A') {
                sa++;
                sb = 0;
                if (sa > 2) countA++;
            } else {
                sb++;
                sa = 0;
                if (sb > 2) countB++;
            }
        }
        return countA > countB;
    }
}
