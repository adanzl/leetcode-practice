package com.leo.leetcode.algorithm.q0900;

import java.util.Comparator;
import java.util.PriorityQueue;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.int2dArrayToString;

/**
 * 给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，并且是一个整数 k ，返回离原点 (0,0) 最近的 k 个点。
 * 这里，平面上两点之间的距离是 欧几里德距离（ √(x1 - x2)2 + (y1 - y2)2 ）。
 * 你可以按 任何顺序 返回答案。除了点坐标的顺序之外，答案 确保 是 唯一 的。
 * 提示：
 * 1、1 <= k <= points.length <= 10^4
 * 2、-10^4 < xi, yi < 10^4
 * 链接：https://leetcode-cn.com/problems/k-closest-points-to-origin
 */
public class Q973 {

    public static void main(String[] args) {
        // [[-2,2]]
        System.out.println(int2dArrayToString(new Q973().kClosest(stringToInt2dArray("[[1,3],[-2,2]]"), 1)));
        // [[3,3],[-2,4]]
        System.out.println(int2dArrayToString(new Q973().kClosest(stringToInt2dArray("[[3,3],[5,-1],[-2,4]]"), 2)));
    }

    public int[][] kClosest(int[][] points, int k) {
        int[][] ret = new int[k][];
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
        for (int i = 0; i < points.length; i++) {
            int[] point = points[i];
            q.add(new int[]{i, point[0] * point[0] + point[1] * point[1]});
        }
        for (int i = 0; i < k && !q.isEmpty(); i++) {
            int[] p = q.poll();
            ret[i] = points[p[0]];
        }
        return ret;
    }
}
