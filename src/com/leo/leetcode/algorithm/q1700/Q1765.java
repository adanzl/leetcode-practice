package com.leo.leetcode.algorithm.q1700;

import java.util.ArrayDeque;
import java.util.Queue;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.int2dArrayToString;

/**
 * 给你一个大小为 m x n 的整数矩阵 isWater ，它代表了一个由 陆地 和 水域 单元格组成的地图。
 * 1、如果 isWater[i][j] == 0 ，格子 (i, j) 是一个 陆地 格子。
 * 2、如果 isWater[i][j] == 1 ，格子 (i, j) 是一个 水域 格子。
 * 你需要按照如下规则给每个单元格安排高度：
 * 1、每个格子的高度都必须是非负的。
 * 2、如果一个格子是是 水域 ，那么它的高度必须为 0 。
 * 3、任意相邻的格子高度差 至多 为 1 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）
 * 找到一种安排高度的方案，使得矩阵中的最高高度值 最大 。
 * 请你返回一个大小为 m x n 的整数矩阵 height ，其中 height[i][j] 是格子 (i, j) 的高度。如果有多种解法，请返回 任意一个 。
 * 提示：
 * 1、m == isWater.length
 * 2、n == isWater[i].length
 * 3、1 <= m, n <= 1000
 * 4、isWater[i][j] 要么是 0 ，要么是 1 。
 * 5、至少有 1 个水域格子。
 *
 * 链接：https://leetcode-cn.com/problems/map-of-highest-peak
 */
public class Q1765 {
    public static void main(String[] args) {
        // [[1,0],[2,1]]
        System.out.println(int2dArrayToString(new Q1765().highestPeak(stringToInt2dArray("[[0,1],[0,0]]"))));
        // [[1,1,0],[0,1,1],[1,2,2]]
        System.out.println(int2dArrayToString(new Q1765().highestPeak(stringToInt2dArray("[[0,0,1],[1,0,0],[0,0,0]]"))));
    }

    public int[][] highestPeak(int[][] isWater) {
        int count = 0, sign = 0, w = isWater.length, h = isWater[0].length;
        int[][] ret = new int[w][h];
        Queue<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                if (isWater[i][j] == 1) {
                    ret[i][j] = 0;
                    q.add(new int[]{i, j});
                    count++;
                } else {
                    ret[i][j] = -1;
                }
            }
        }

        while (count < w * h) {
            int size = q.size();
            for (int k = 0; k < size && !q.isEmpty(); k++) {
                int[] pos = q.poll();
                int i = pos[0], j = pos[1];
                if (i - 1 >= 0 && ret[i - 1][j] == -1) {
                    ret[i - 1][j] = sign + 1;
                    q.add(new int[]{i - 1, j});
                    ++count;
                }
                if (i + 1 < w && ret[i + 1][j] == -1) {
                    ret[i + 1][j] = sign + 1;
                    q.add(new int[]{i + 1, j});
                    ++count;
                }
                if (j - 1 >= 0 && ret[i][j - 1] == -1) {
                    ret[i][j - 1] = sign + 1;
                    q.add(new int[]{i, j - 1});
                    ++count;
                }
                if (j + 1 < h && ret[i][j + 1] == -1) {
                    ret[i][j + 1] = sign + 1;
                    q.add(new int[]{i, j + 1});
                    ++count;
                }
            }

            ++sign;
        }
        return ret;
    }
}
