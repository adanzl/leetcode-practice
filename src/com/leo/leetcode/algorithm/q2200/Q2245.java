package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个二维整数数组 grid ，大小为 m x n，其中每个单元格都含一个正整数。
 * 转角路径 定义为：包含至多一个弯的一组相邻单元。具体而言，路径应该完全 向水平方向 或者 向竖直方向 移动过弯（如果存在弯），而不能访问之前访问过的单元格。
 * 在过弯之后，路径应当完全朝 另一个 方向行进：如果之前是向水平方向，那么就应该变为向竖直方向；反之亦然。当然，同样不能访问之前已经访问过的单元格。
 * 一条路径的 乘积 定义为：路径上所有值的乘积。
 * 请你从 grid 中找出一条乘积中尾随零数目最多的转角路径，并返回该路径中尾随零的数目。
 * 注意：
 * 1、水平 移动是指向左或右移动。
 * 2、竖直 移动是指向上或下移动。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 10^5
 * 4、1 <= m * n <= 10^5
 * 5、1 <= grid[i][j] <= 1000
 * 链接：https://leetcode-cn.com/problems/maximum-trailing-zeros-in-a-cornered-path
 */
public class Q2245 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2245().maxTrailingZeros(stringToInt2dArray("[[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]")));
        // 0
        System.out.println(new Q2245().maxTrailingZeros(stringToInt2dArray("[[4,3,2],[7,6,1],[8,8,8]]")));
    }

    public int maxTrailingZeros(int[][] grid) {
        int m = grid.length, n = grid[0].length, ret = 0;
        int[][][] preGridCol = new int[n][m + 1][2];
        int[][][] preGridRow = new int[m][n + 1][2];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                preGridCol[j][i + 1][0] = countX(grid[i][j], 2) + preGridCol[j][i][0];
                preGridCol[j][i + 1][1] = countX(grid[i][j], 5) + preGridCol[j][i][1];
                preGridRow[i][j + 1][0] = countX(grid[i][j], 2) + preGridRow[i][j][0];
                preGridRow[i][j + 1][1] = countX(grid[i][j], 5) + preGridRow[i][j][1];
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int count2 = preGridRow[i][j + 1][0] - preGridRow[i][j][0];
                int count5 = preGridRow[i][j + 1][1] - preGridRow[i][j][1];
                ret = Math.max(ret, Math.min(preGridRow[i][j + 1][0] + preGridCol[j][i + 1][0] - count2, preGridRow[i][j + 1][1] + preGridCol[j][i + 1][1] - count5));
                ret = Math.max(ret, Math.min(preGridRow[i][j + 1][0] + (preGridCol[j][m][0] - preGridCol[j][i][0]) - count2, preGridRow[i][j + 1][1] + (preGridCol[j][m][1] - preGridCol[j][i][1]) - count5));
                ret = Math.max(ret, Math.min((preGridRow[i][n][0] - preGridRow[i][j][0]) + preGridCol[j][i + 1][0] - count2, (preGridRow[i][n][1] - preGridRow[i][j][1]) + preGridCol[j][i + 1][1] - count5));
                ret = Math.max(ret, Math.min((preGridRow[i][n][0] - preGridRow[i][j][0]) + (preGridCol[j][m][0] - preGridCol[j][i][0]) - count2, (preGridRow[i][n][1] - preGridRow[i][j][1]) + (preGridCol[j][m][1] - preGridCol[j][i][1]) - count5));
            }
        }
        return ret;
    }

    int countX(int num, int x) {
        int ret = 0;
        while (num != 0 && num % x == 0) {
            num /= x;
            ret++;
        }
        return ret;
    }

}
