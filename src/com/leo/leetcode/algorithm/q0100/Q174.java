package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;

import java.util.Arrays;

/**
 * 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。
 * 我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
 * 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
 * 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；
 * 其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
 * 为了尽快到达公主，骑士决定每次只向右或向下移动一步。
 * 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
 * 说明:
 * 骑士的健康点数没有上限。
 * 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。
 * 链接：https://leetcode-cn.com/problems/dungeon-game
 */
public class Q174 {

    public static void main(String[] args) {
        System.out.println(new Q174().calculateMinimumHP(LCUtil.stringToInt2dArray("[[1,-3,3],[0,-2,0],[-3,-3,-3]]"))); // 3
        System.out.println(new Q174().calculateMinimumHP(LCUtil.stringToInt2dArray("[[-2,-3,3],[-5,-10,1],[10,30,-5]]"))); // 7
        System.out.println(new Q174().calculateMinimumHP(LCUtil.stringToInt2dArray("[[0,0,0],[1,1,-1]]"))); // 1
        System.out.println(new Q174().calculateMinimumHP(LCUtil.stringToInt2dArray("[[-3, 5]]"))); // 4
        System.out.println(new Q174().calculateMinimumHP(LCUtil.stringToInt2dArray("[[-1, 1]]"))); // 2
        System.out.println(new Q174().calculateMinimumHP(LCUtil.stringToInt2dArray("[[100]]"))); // 1
    }

    public int calculateMinimumHP(int[][] dungeon) {
        int n = dungeon.length, m = dungeon[0].length;
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 0; i <= n; ++i) Arrays.fill(dp[i], Integer.MAX_VALUE);
        dp[n][m - 1] = dp[n - 1][m] = 1;
        for (int i = n - 1; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                int minn = Math.min(dp[i + 1][j], dp[i][j + 1]);
                dp[i][j] = Math.max(minn - dungeon[i][j], 1);
            }
        }
        return dp[0][0];
    }
}
