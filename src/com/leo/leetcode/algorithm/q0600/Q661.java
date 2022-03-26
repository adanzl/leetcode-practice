package com.leo.leetcode.algorithm.q0600;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.int2dArrayToString;

/**
 * 图像平滑器 是大小为 3 x 3 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。
 * 每个单元格的 平均灰度 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9 个单元格的平均值）。
 * 如果一个单元格周围存在单元格缺失的情况，则计算平均灰度时不考虑缺失的单元格（即，需要计算红色平滑器中 4 个单元格的平均值）。
 * 给你一个表示图像灰度的 m x n 整数矩阵 img ，返回对图像的每个单元格平滑处理后的图像 。
 * 提示:
 * 1、m == img.length
 * 2、n == img[i].length
 * 3、1 <= m, n <= 200
 * 4、0 <= img[i][j] <= 255
 * 链接：https://leetcode-cn.com/problems/image-smoother
 */
public class Q661 {

    public static void main(String[] args) {
        // [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
        System.out.println(int2dArrayToString(new Q661().imageSmoother(stringToInt2dArray("[[1,1,1],[1,0,1],[1,1,1]]"))));
        // [[137,141,137],[141,138,141],[137,141,137]]
        System.out.println(int2dArrayToString(new Q661().imageSmoother(stringToInt2dArray("[[100,200,100],[200,50,200],[100,200,100]]"))));
    }

    int count = 0, sum = 0;

    public int[][] imageSmoother(int[][] img) {
        int row = img.length, col = img[0].length;
        int[][] ret = new int[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                sum = img[i][j];
                count = 1;
                this.sumTime(img, i - 1, j, row, col);
                this.sumTime(img, i - 1, j - 1, row, col);
                this.sumTime(img, i - 1, j + 1, row, col);
                this.sumTime(img, i + 1, j, row, col);
                this.sumTime(img, i + 1, j - 1, row, col);
                this.sumTime(img, i + 1, j + 1, row, col);
                this.sumTime(img, i, j - 1, row, col);
                this.sumTime(img, i, j + 1, row, col);
                ret[i][j] = sum / count;
            }
        }
        return ret;
    }

    void sumTime(int[][] img, int x, int y, int row, int col) {
        if (x < 0 || x >= row || y < 0 || y >= col) return;
        sum += img[x][y];
        count++;
    }
}
