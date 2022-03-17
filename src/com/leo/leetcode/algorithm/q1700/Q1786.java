package com.leo.leetcode.algorithm.q1700;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 现有一个加权无向连通图。给你一个正整数 n ，表示图中有 n 个节点，并按从 1 到 n 给节点编号；
 * 另给你一个数组 edges ，其中每个 edges[i] = [ui, vi, weight_i] 表示存在一条位于节点 ui 和 vi 之间的边，这条边的权重为 weight_i 。
 * 从节点 start 出发到节点 end 的路径是一个形如 [z0, z1, z2, ..., zk] 的节点序列，
 * 满足 z0 = start 、zk = end 且在所有符合 0 <= i <= k-1 的节点 zi 和 zi+1 之间存在一条边。
 * 路径的距离定义为这条路径上所有边的权重总和。用 distanceToLastNode(x) 表示节点 n 和 x 之间路径的最短距离。
 * 受限路径 为满足 distanceToLastNode(zi) > distanceToLastNode(zi+1) 的一条路径，其中 0 <= i <= k-1 。
 * 返回从节点 1 出发到节点 n 的 受限路径数 。由于数字可能很大，请返回对 10^9 + 7 取余 的结果。
 * 提示：
 * 1、1 <= n <= 2 * 10^4
 * 2、n - 1 <= edges.length <= 4 * 10^4
 * 3、edges[i].length == 3
 * 4、1 <= ui, vi <= n
 * 5、ui != vi
 * 6、1 <= weight_i <= 10^5
 * 7、任意两个节点之间至多存在一条边
 * 8、任意两个节点之间至少存在一条路径
 * 链接：https://leetcode-cn.com/problems/number-of-restricted-paths-from-first-to-last-node
 */
public class Q1786 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q1786().countRestrictedPaths(5, stringToInt2dArray("[[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]")));
        // 1
        System.out.println(new Q1786().countRestrictedPaths(7, stringToInt2dArray("[[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]")));
    }

    public int countRestrictedPaths(int n, int[][] edges) {
        int INF = Integer.MAX_VALUE;
        List<List<int[]>> nextList = new ArrayList<>();
        for (int i = 0; i < n; i++) nextList.add(new ArrayList<>());
        for (int[] edge : edges) {
            nextList.get(edge[1] - 1).add(new int[]{edge[0] - 1, edge[2]});
            nextList.get(edge[0] - 1).add(new int[]{edge[1] - 1, edge[2]});
        }
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
        q.add(new int[]{n - 1, 0});
        boolean[] visited = new boolean[n];
        int[] distArr = new int[n], countArr = new int[n];
        Arrays.fill(distArr, INF);
        Arrays.fill(countArr, -1);
        distArr[n - 1] = 0;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int idx = cur[0], dist = cur[1];
            if (visited[idx]) continue;
            for (int[] next : nextList.get(idx)) {
                if (distArr[next[0]] > dist + next[1]) {
                    distArr[next[0]] = dist + next[1];
                    q.add(new int[]{next[0], dist + next[1]});
                }
            }
            visited[idx] = true;
        }
        return countPath(0, nextList, distArr, countArr);
    }

    int countPath(int idx, List<List<int[]>> nextList, int[] distArr, int[] countArr) {
        if (idx == distArr.length - 1) return 1;
        if (countArr[idx] != -1) return countArr[idx];
        int ret = 0;
        for (int[] next : nextList.get(idx)) {
            if (distArr[idx] > distArr[next[0]]) {
                ret = (ret + countPath(next[0], nextList, distArr, countArr)) % 1000000007;
            }
        }
        countArr[idx] = ret;
        return ret;
    }

}
