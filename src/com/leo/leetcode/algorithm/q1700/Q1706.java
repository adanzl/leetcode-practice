package com.leo.leetcode.algorithm.q1700;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 用一个大小为 m x n 的二维网格 grid 表示一个箱子。你有 n 颗球。箱子的顶部和底部都是开着的。
 * 箱子中的每个单元格都有一个对角线挡板，跨过单元格的两个角，可以将球导向左侧或者右侧。
 * 1、将球导向右侧的挡板跨过左上角和右下角，在网格中用 1 表示。
 * 2、将球导向左侧的挡板跨过右上角和左下角，在网格中用 -1 表示。
 * 在箱子每一列的顶端各放一颗球。每颗球都可能卡在箱子里或从底部掉出来。
 * 如果球恰好卡在两块挡板之间的 "V" 形图案，或者被一块挡导向到箱子的任意一侧边上，就会卡住。
 * 返回一个大小为 n 的数组 answer ，其中 answer[i] 是球放在顶部的第 i 列后从底部掉出来的那一列对应的下标，如果球卡在盒子里，则返回 -1 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 100
 * 4、grid[i][j] 为 1 或 -1
 * 链接：https://leetcode-cn.com/problems/where-will-the-ball-fall
 */
public class Q1706 {

    public static void main(String[] args) {
        // [1,-1,-1,-1,-1]
        System.out.println(Arrays.toString(new Q1706().findBall(stringToInt2dArray("[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]"))));
        // [-1]
        System.out.println(Arrays.toString(new Q1706().findBall(stringToInt2dArray("[[-1]]"))));
        // [0,1,2,3,4,-1]
        System.out.println(Arrays.toString(new Q1706().findBall(stringToInt2dArray("[[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]"))));
    }

    public int[] findBall(int[][] grid) {
        int n = grid[0].length;
        int[] pos = new int[n], flags = new int[n];
        for (int i = 0; i < n; i++) pos[i] = i;
        for (int[] line : grid) {
            for (int i = 0; i < n; i++) {
                if (line[i] == 1) {
                    if (i == n - 1 || line[i + 1] == -1) flags[i] = 0;
                    else flags[i] = 1;
                } else {
                    if (i == 0 || line[i - 1] == 1) flags[i] = 0;
                    else flags[i] = -1;
                }
            }
            for (int i = 0; i < n; i++) {
                int p = pos[i];
                if (p == -1) continue;
                if (flags[p] == 0) pos[i] = -1;
                else pos[i] = p + flags[p];
            }
        }
        return pos;
    }
}
