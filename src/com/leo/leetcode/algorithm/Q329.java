package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

/**
 * 给定一个整数矩阵，找出最长递增路径的长度。 对于每个单元格，你可以往上，下，左，右四个方向移动。
 * 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
 * 链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/
 */
// TODO
class Q329 {

    public static void main(String[] args) {
        System.out.println(new Q329().longestIncreasingPath(LCUtil.stringToInt2dArray("[[9,9,4],[6,6,8],[2,1,1]]"))); // 4
        System.out.println(new Q329().longestIncreasingPath(LCUtil.stringToInt2dArray("[[3,4,5],[3,2,6],[2,2,1]]"))); // 4
    }

    public int longestIncreasingPath(int[][] matrix) {
        return 0;
    }
}