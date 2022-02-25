package com.leo.leetcode.algorithm.q0800;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一座由 n x n 个街区组成的城市，每个街区都包含一座立方体建筑。
 * 给你一个下标从 0 开始的 n x n 整数矩阵 grid ，其中 grid[r][c] 表示坐落于 r 行 c 列的建筑物的 高度 。
 * 城市的 天际线 是从远处观察城市时，所有建筑物形成的外部轮廓。从东、南、西、北四个主要方向观测到的 天际线 可能不同。
 * 我们被允许为 任意数量的建筑物 的高度增加 任意增量（不同建筑物的增量可能不同） 。
 * 高度为 0 的建筑物的高度也可以增加。然而，增加的建筑物高度 不能影响 从任何主要方向观察城市得到的 天际线 。
 * 在 不改变 从任何主要方向观测到的城市 天际线 的前提下，返回建筑物可以增加的 最大高度增量总和 。
 * 提示：
 * 1、n == grid.length
 * 2、n == grid[r].length
 * 3、2 <= n <= 50
 * 4、0 <= grid[r][c] <= 100
 * 链接：https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline
 */
public class Q807 {

    public static void main(String[] args) {
        // 35
        System.out.println(new Q807().maxIncreaseKeepingSkyline(stringToInt2dArray("[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]")));
        // 0
        System.out.println(new Q807().maxIncreaseKeepingSkyline(stringToInt2dArray("[[0,0,0],[0,0,0],[0,0,0]]")));
    }

    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int ret = 0, row = grid.length, col = grid[0].length;
        int[] maxRow = new int[row], maxCol = new int[col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                maxRow[i] = Math.max(maxRow[i], grid[i][j]);
                maxCol[j] = Math.max(maxCol[j], grid[i][j]);
            }
        }
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                ret += Math.min(maxRow[i], maxCol[j]) - grid[i][j];
            }
        }
        return ret;
    }
}
