package com.leo.leetcode.algorithm.q0500;

import static com.leo.utils.LCUtil.int2dArrayToString;
import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
 * 给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
 * 重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
 * 如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
 * <p>
 * 注意：
 * 1、给定矩阵的宽和高范围在 [1, 100]。
 * 2、给定的 r 和 c 都是正数。
 * <p>
 * 链接：https://leetcode-cn.com/problems/reshape-the-matrix
 */
public class Q566 {

    public static void main(String[] args) {
        // [[1,2,3,4]]
        System.out.println(int2dArrayToString(new Q566().matrixReshape(stringToInt2dArray("[[1,2],[3,4]]"), 1, 4)));
        // [[1,2],[3,4]]
        System.out.println(int2dArrayToString(new Q566().matrixReshape(stringToInt2dArray("[[1,2],[3,4]]"), 2, 4)));
    }

    public int[][] matrixReshape(int[][] nums, int r, int c) {
        if (nums.length * nums[0].length != r * c)
            return nums;
        int[][] ret = new int[r][c];
        for (int i = 0, idx = 0; i < nums.length; i++) {
            for (int j = 0; j < nums[i].length; j++, idx++) {
                ret[idx / c][idx % c] = nums[i][j];
            }
        }
        return ret;
    }
}
