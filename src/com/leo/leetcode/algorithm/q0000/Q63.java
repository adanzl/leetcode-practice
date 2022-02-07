package com.leo.leetcode.algorithm.q0000;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
 * 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
 * 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
 * 网格中的障碍物和空位置分别用 1 和 0 来表示。
 * 说明：m 和 n 的值均不超过 100。
 * 链接：https://leetcode-cn.com/problems/unique-paths-ii
 */
public class Q63 {
    public static void main(String[] args) {
        System.out.println(new Q63().uniquePathsWithObstacles(stringToInt2dArray("[[1],[0]]"))); // 0
        System.out.println(new Q63().uniquePathsWithObstacles(stringToInt2dArray("[[0,0,0],[0,1,0],[0,0,0]]"))); // 2
    }

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid.length == 0) return 0;
        int[] marks = new int[obstacleGrid[0].length];
        for (int i = 0; i < obstacleGrid.length; i++) {
            for (int j = 0; j < marks.length; j++) {
                if (obstacleGrid[i][j] == 1) marks[j] = 0;
                else if (i == 0) marks[j] = j == 0 ? 1 : marks[j - 1];
                else marks[j] = j == 0 ? marks[j] : marks[j - 1] + marks[j];
            }
        }
        return marks[marks.length - 1];
    }
}
