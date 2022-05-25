package com.leo.leetcode.algorithm.q2200;

import com.leo.utils.TestCase;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个整数 n ，它表示一个 带权有向 图的节点数，节点编号为 0 到 n - 1 。
 * 同时给你一个二维整数数组 edges ，其中 edges[i] = [from_i , to_i, weight_i] ，表示从 from_i  到 to_i 有一条边权为 weight_i 的 有向 边。
 * 最后，给你三个 互不相同 的整数 src1 ，src2 和 dest ，表示图中三个不同的点。
 * 请你从图中选出一个 边权和最小 的子图，使得从 src1 和 src2 出发，在这个子图中，都 可以 到达 dest 。如果这样的子图不存在，请返回 -1 。
 * 子图 中的点和边都应该属于原图的一部分。子图的边权和定义为它所包含的所有边的权值之和。
 * 提示：
 * 1、3 <= n <= 10^5
 * 2、0 <= edges.length <= 10^5
 * 3、edges[i].length == 3
 * 4、0 <= from_i , to_i, src1, src2, dest <= n - 1
 * 5、from_i  != to_i
 * 6、src1 ，src2 和 dest 两两不同。
 * 7、1 <= weight[i] <= 10^5
 * 链接：https://leetcode-cn.com/problems/minimum-weighted-subgraph-with-the-required-paths
 */
public class Q2203 {

    public static void main(String[] args) {
        // 9999900000
        TestCase tc = new TestCase("resources/algorithm/q2200/Q2203/Case001.txt");
        System.out.println(new Q2203().minimumWeight(
                Integer.parseInt(tc.getData(0)), stringToInt2dArray(tc.getData(1)),
                Integer.parseInt(tc.getData(2)), Integer.parseInt(tc.getData(3)), Integer.parseInt(tc.getData(4))));
        // 9
        System.out.println(new Q2203().minimumWeight(
                6, stringToInt2dArray("[[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]"),
                0, 1, 5));
        // -1
        System.out.println(new Q2203().minimumWeight(
                3, stringToInt2dArray("[[0,1,1],[2,1,1]]"),
                0, 1, 2));
    }

    long INF = Long.MAX_VALUE;

    public long minimumWeight(int n, int[][] edges, int src1, int src2, int dest) {
        long ret = INF;
        List<List<int[]>> nextVertex = new ArrayList<>();
        List<List<int[]>> reNextVertex = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            nextVertex.add(new ArrayList<>());
            reNextVertex.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            nextVertex.get(edge[0]).add(new int[]{edge[1], edge[2]});
            reNextVertex.get(edge[1]).add(new int[]{edge[0], edge[2]});
        }
        long[] dist1 = dijkstra(n, src1, nextVertex);
        long[] dist2 = dijkstra(n, src2, nextVertex);
        if (dist1[dest] == INF || dist2[dest] == INF) return -1;
        long[] dist3 = dijkstra(n, dest, reNextVertex);
        for (int i = 0; i < n; i++) {
            if (dist1[i] != INF && dist2[i] != INF && dist3[i] != INF) {
                ret = Math.min(ret, dist1[i] + dist2[i] + dist3[i]);
            }
        }
        return ret;
    }

    long[] dijkstra(int n, int src, List<List<int[]>> nextVertex) {
        long[] dist = new long[n];
        boolean[] vis = new boolean[n];
        Arrays.fill(dist, INF);
        dist[src] = 0;
        PriorityQueue<long[]> q = new PriorityQueue<>(Comparator.comparingLong(a -> a[1]));
        q.offer(new long[]{src, 0});
        while (!q.isEmpty()) {
            long[] cur = q.poll();
            long minNext = cur[1];
            int maxIdx = (int) cur[0];
            if (vis[maxIdx]) continue;
            for (int[] m : nextVertex.get(maxIdx)) {
                int nextIdx = m[0];
                if (m[1] + minNext < dist[nextIdx]) {
                    dist[nextIdx] = m[1] + minNext;
                    q.offer(new long[]{m[0], dist[nextIdx]});
                }
            }
            vis[maxIdx] = true;
        }
        return dist;
    }
}
