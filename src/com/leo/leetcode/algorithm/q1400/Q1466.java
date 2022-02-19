package com.leo.leetcode.algorithm.q1400;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。
 * 去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。
 * 路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。
 * 今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。
 * 请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。
 * 题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。
 * 提示：
 * 1、2 <= n <= 5 * 10^4
 * 2、connections.length == n-1
 * 3、connections[i].length == 2
 * 4、0 <= connections[i][0], connections[i][1] <= n-1
 * 5、connections[i][0] != connections[i][1]
 * 链接：https://leetcode-cn.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero
 */
public class Q1466 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q1466().minReorder(6, stringToInt2dArray("[[0,1],[1,3],[2,3],[4,0],[4,5]]")));
        // 2
        System.out.println(new Q1466().minReorder(5, stringToInt2dArray("[[1,0],[1,2],[3,2],[3,4]]")));
        // 0
        System.out.println(new Q1466().minReorder(3, stringToInt2dArray("[[1,0],[2,0]]")));
    }

    int ret = 0;

    public int minReorder(int n, int[][] connections) {
        List<Set<Integer>> nextList = new ArrayList<>();
        for (int i = 0; i < n; i++) nextList.add(new HashSet<>());
        boolean[] visited = new boolean[n];
        for (int[] connection : connections) {
            nextList.get(connection[0]).add(connection[1]);
            nextList.get(connection[1]).add(-connection[0]);
        }
        dfs(0, nextList, visited);
        return n - ret - 1;
    }

    void dfs(int idx, List<Set<Integer>> nextList, boolean[] visited) {
        int i = idx;
        if (i < 0) i = -i;
        if (visited[i]) return;
        if (idx < 0) ret++;
        visited[i] = true;
        for (int next : nextList.get(i)) {
            dfs(next, nextList, visited);
        }
    }
}
