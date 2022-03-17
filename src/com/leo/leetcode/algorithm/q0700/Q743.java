package com.leo.leetcode.algorithm.q0700;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 有 n 个网络节点，标记为 1 到 n。
 * 给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。
 * 现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。
 * 提示：
 * 1、1 <= k <= n <= 100
 * 2、1 <= times.length <= 6000
 * 3、times[i].length == 3
 * 4、1 <= ui, vi <= n
 * 5、ui != vi
 * 6、0 <= wi <= 100
 * 7、所有 (ui, vi) 对都 互不相同（即，不含重复边）
 * 链接：https://leetcode-cn.com/problems/network-delay-time
 */
public class Q743 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q743().networkDelayTime(stringToInt2dArray("[[2,1,1],[2,3,1],[3,4,1]]"), 4, 2));
        // 1
        System.out.println(new Q743().networkDelayTime(stringToInt2dArray("[[1,2,1]]"), 2, 1));
        // -1
        System.out.println(new Q743().networkDelayTime(stringToInt2dArray("[[1,2,1]]"), 2, 2));
    }

    public int networkDelayTime(int[][] times, int n, int k) {
        final int INF = Integer.MAX_VALUE;
        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        boolean[] visited = new boolean[n];
        List<List<int[]>> nextList = new ArrayList<>(n);
        for (int i = 0; i < n; i++) nextList.add(new ArrayList<>());
        for (int[] edge : times) nextList.get(edge[0] - 1).add(new int[]{edge[1] - 1, edge[2]});
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
        q.add(new int[]{k - 1, 0}); // path-weight
        dist[k - 1] = 0;
        while (!q.isEmpty()) {
            int[] edge = q.poll();
            int idx = edge[0], minNext = edge[1];
            if (visited[idx]) continue;
            for (int[] next : nextList.get(idx)) {
                if (dist[next[0]] > next[1] + minNext) {
                    dist[next[0]] = next[1] + minNext;
                    q.add(new int[]{next[0], dist[next[0]]});
                }
            }
            visited[idx] = true;
        }
        int ret = 0;
        for (int d : dist) ret = Math.max(ret, d);
        return ret == INF ? -1 : ret;
    }
}
