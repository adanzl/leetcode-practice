package com.leo.leetcode.algorithm.q0800;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 在 n x n 的网格 grid 中，我们放置了一些与 x，y，z 三轴对齐的 1 x 1 x 1 立方体。
 * 每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
 * 现在，我们查看这些立方体在 xy 、yz 和 zx 平面上的投影。
 * 投影 就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。
 * 返回 所有三个投影的总面积 。
 * 提示：
 * 1、n == grid.length == grid[i].length
 * 2、1 <= n <= 50
 * 3、0 <= grid[i][j] <= 50
 * 链接：https://leetcode-cn.com/problems/projection-area-of-3d-shapes
 */
public class Q883 {

    public static void main(String[] args) {
        //
        System.out.println(new Q883().projectionArea(stringToInt2dArray("[[1,1,1],[1,0,1],[1,1,1]]")));
        // 17
        System.out.println(new Q883().projectionArea(stringToInt2dArray("[[1,2],[3,4]]")));
        // 5
        System.out.println(new Q883().projectionArea(stringToInt2dArray("[[2]]")));
        // 8
        System.out.println(new Q883().projectionArea(stringToInt2dArray("[[1,0],[0,2]]")));
    }

    public int projectionArea(int[][] grid) {
        int n = grid.length, ret = 0;
        int[] xy = new int[n], yz = new int[n], zx = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                zx[i] = Math.max(zx[i], grid[i][j]);
                yz[j] = Math.max(yz[j], grid[i][j]);
                if (grid[i][j] > 0) xy[i]++;
            }
        }
        for (int num : xy) ret += num;
        for (int num : yz) ret += num;
        for (int num : zx) ret += num;
        return ret;
    }
}
