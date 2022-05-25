package com.leo.leetcode.lcci;

import com.leo.utils.LCUtil;

import java.util.Arrays;

/**
 * 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
 * 不占用额外内存空间能否做到？
 * 注意：本题与主站 48 题相同：https://leetcode-cn.com/problems/rotate-image/
 * 链接：https://leetcode.cn/problems/rotate-matrix-lcci/
 */
public class Q01_07 {

    public static void main(String[] args) {
        int[][] matrix = LCUtil.stringToInt2dArray("[[1,2,3], [4,5,6], [7,8,9]]");
        new Q01_07().rotate(matrix);
        System.out.println(Arrays.toString(matrix));
        matrix = LCUtil.stringToInt2dArray("[[ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16]]");
        new Q01_07().rotate(matrix);
        System.out.println(Arrays.toString(matrix));
    }

    public void rotate(int[][] matrix) {
        // 水平 - 翻转
        for (int i = 0; i < matrix.length >> 1; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                swap(matrix, i, j, matrix.length - 1 - i, j);
            }
        }
        // 对角线 \ 翻转
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < i; j++) {
                swap(matrix, i, j, j, i);
            }
        }
    }

    void swap(int[][] matrix, int x0, int y0, int x1, int y1) {
        int t = matrix[x0][y0];
        matrix[x0][y0] = matrix[x1][y1];
        matrix[x1][y1] = t;
    }
}
