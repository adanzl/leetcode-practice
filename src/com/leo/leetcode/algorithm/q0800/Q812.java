package com.leo.leetcode.algorithm.q0800;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
 * 注意:
 * 1、3 <= points.length <= 50.
 * 2、不存在重复的点。
 * 3、-50 <= points[i][j] <= 50.
 * 4、结果误差值在 10^-6 以内都认为是正确答案。
 * 链接：https://leetcode.cn/problems/largest-triangle-area
 */
public class Q812 {
    public static void main(String[] args) {
        // 2
        System.out.println(new Q812().largestTriangleArea(stringToInt2dArray("[[0,0],[0,1],[1,0],[0,2],[2,0]]")));
    }

    public double largestTriangleArea(int[][] points) {
        int n = points.length;
        double ret = 0.0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    ret = Math.max(ret, triangleArea(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]));
                }
            }
        }
        return ret;
    }

    public double triangleArea(int x1, int y1, int x2, int y2, int x3, int y3) {
        return 0.5 * Math.abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2);
    }
}
