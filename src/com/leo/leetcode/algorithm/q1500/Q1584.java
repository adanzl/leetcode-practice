package com.leo.leetcode.algorithm.q1500;

import java.util.Arrays;
import java.util.Comparator;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个points  数组，表示 2D 平面上的一些点，其中  points[i] = [xi, yi]  。
 * 连接点  [xi, yi] 和点  [xj, yj]  的费用为它们之间的 曼哈顿距离  ：|xi - xj| + |yi - yj|  ，其中  |val|  表示  val  的绝对值。
 * 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连
 * 提示：
 * 1、1 <= points.length <= 1000
 * 2、-10^6 <= xi, yi <= 10^6
 * 3、所有点 (xi, yi) 两两不同。
 * <p>
 * 链接：https://leetcode-cn.com/problems/min-cost-to-connect-all-points
 */
public class Q1584 {

    public static void main(String[] args) {
        // 20
        System.out.println(new Q1584().minCostConnectPoints(stringToInt2dArray("[[0,0],[2,2],[3,10],[5,2],[7,0]]")));
        // 18
        System.out.println(new Q1584().minCostConnectPoints(stringToInt2dArray("[[3,12],[-2,5],[-4,1]]")));
        // 4
        System.out.println(new Q1584().minCostConnectPoints(stringToInt2dArray("[[0,0],[1,1],[1,0],[-1,1]]")));
        // 4000000
        System.out.println(new Q1584().minCostConnectPoints(stringToInt2dArray("[[-1000000,-1000000],[1000000,1000000]]")));
        // 0
        System.out.println(new Q1584().minCostConnectPoints(stringToInt2dArray("[[0,0]]")));
    }

    int[] parent;

    public int minCostConnectPoints(int[][] points) {
        int ret = 0, count = 0, ei = 0;
        parent = new int[points.length];
        for (int i = 0; i < points.length; i++) parent[i] = i;
        int n = (points.length - 1) * points.length / 2;
        int[][] edges = new int[n][3];
        for (int i = 0; i < points.length; i++) {
            int[] p0 = points[i];
            for (int j = i + 1; j < points.length; j++) {
                int[] p1 = points[j];
                edges[ei][0] = Math.abs(p0[0] - p1[0]) + Math.abs(p0[1] - p1[1]);
                edges[ei][1] = i;
                edges[ei][2] = j;
                ++ei;
            }
        }
        Arrays.sort(edges, Comparator.comparingInt(o -> o[0]));
        for (int[] edge : edges) {
            if (merge(edge[1], edge[2])) {
                ++count;
                ret += edge[0];
            }
            if (count == points.length - 1) break;
        }
        return ret;
    }

    int find(int x) {
        if (x != parent[x]) parent[x] = find(parent[x]);
        return parent[x];
    }

    boolean merge(int i0, int i1) {
        int r0 = find(i0), r1 = find(i1);
        if (r0 != r1) parent[r1] = r0;
        return r0 != r1;
    }

}
