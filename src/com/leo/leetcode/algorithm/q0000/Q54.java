package com.leo.leetcode.algorithm.q0000;

import com.leo.utils.LCUtil;

import java.util.ArrayList;
import java.util.List;

/**
 * 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
 * <p>
 * 提示：
 * 1、m == matrix.length
 * 2、n == matrix[i].length
 * 3、1 <= m, n <= 10
 * 4、-100 <= matrix[i][j] <= 100
 * <p>
 * 链接：https://leetcode-cn.com/problems/spiral-matrix
 */
public class Q54 {

    public static void main(String[] args) {
        System.out.println(new Q54().spiralOrder(LCUtil.stringToInt2dArray("[[1,2,3],[4,5,6],[7,8,9]]"))); // [1,2,3,6,9,8,7,4,5]
    }

    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> out = new ArrayList<>();
        if (matrix.length == 0) return out;
        int d = 0; // r=0, d=1, l=2, u=3
        int maxX = matrix[0].length - 1;
        int maxY = matrix.length - 1;
        int minX = 0, minY = 0;
        int x = 0, y = 0;
        while (maxX >= minX || maxY >= minY) {
            if (x >= minX && x <= maxX && y >= minY && y <= maxY) out.add(matrix[y][x]);
            switch (d) {
                case 0:
                    x++;
                    if (x > maxX) {
                        x = maxX;
                        d = 1;
                        minY++;
                    }
                    break;
                case 1:
                    y++;
                    if (y > maxY) {
                        y = maxY;
                        d = 2;
                        maxX--;
                    }
                    break;
                case 2:
                    x--;
                    if (x < minX) {
                        x = minX;
                        d = 3;
                        maxY--;
                    }
                    break;
                case 3:
                    y--;
                    if (y < minY) {
                        y = minY;
                        d = 0;
                        minX++;
                    }
                    break;
            }
        }

        return out;
    }
}
