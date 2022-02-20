package com.leo.leetcode.algorithm.q1100;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 在一个有向图中，节点分别标记为 0, 1, ..., n-1。这个图中的每条边不是红色就是蓝色，且存在自环或平行边。
 * red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的蓝色有向边。
 * 返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。
 * 如果不存在这样的路径，那么 answer[x] = -1。
 * 提示：
 * 1、1 <= n <= 100
 * 2、red_edges.length <= 400
 * 3、blue_edges.length <= 400
 * 4、red_edges[i].length == blue_edges[i].length == 2
 * 5、0 <= red_edges[i][j], blue_edges[i][j] < n
 * 链接：https://leetcode-cn.com/problems/shortest-path-with-alternating-colors
 */
public class Q1129 {

    public static void main(String[] args) {
        // [0,1,2,3,7]
        System.out.println(Arrays.toString(new Q1129().shortestAlternatingPaths(5, stringToInt2dArray("[[0,1],[1,2],[2,3],[3,4]]"), stringToInt2dArray("[[1,2],[2,3],[3,1]]"))));
        // [0,1,-1]
        System.out.println(Arrays.toString(new Q1129().shortestAlternatingPaths(3, stringToInt2dArray("[[0,1],[1,2]]"), stringToInt2dArray("[]"))));
        // [0,1,-1]
        System.out.println(Arrays.toString(new Q1129().shortestAlternatingPaths(3, stringToInt2dArray("[[0,1]]"), stringToInt2dArray("[[2,1]]"))));
        // [0,-1,-1]
        System.out.println(Arrays.toString(new Q1129().shortestAlternatingPaths(3, stringToInt2dArray("[[1,0]]"), stringToInt2dArray("[[2,1]]"))));
        // [0,1,2]
        System.out.println(Arrays.toString(new Q1129().shortestAlternatingPaths(3, stringToInt2dArray("[[0,1]]"), stringToInt2dArray("[[1,2]]"))));
        // [0,1,1]
        System.out.println(Arrays.toString(new Q1129().shortestAlternatingPaths(3, stringToInt2dArray("[[0,1],[0,2]]"), stringToInt2dArray("[[1,2]]"))));
    }

    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        int[] ret = new int[n];
        boolean[][] visited = new boolean[n][2];
        Arrays.fill(ret, 1, n, -1);
        List<List<Integer>> redEdge = new ArrayList<>(), blueEdge = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            redEdge.add(new ArrayList<>());
            blueEdge.add(new ArrayList<>());
        }
        int len = 0;
        Queue<int[]> q = new ArrayDeque<>();
        for (int[] edge : redEdges) {
            redEdge.get(edge[0]).add(edge[1]);
            if (edge[0] == 0) q.add(new int[]{0, 1}); // I'm blue
        }
        for (int[] edge : blueEdges) {
            blueEdge.get(edge[0]).add(edge[1]);
            if (edge[0] == 0) q.add(new int[]{0, 0}); // I'm red
        }
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0 && !q.isEmpty()) {
                int[] p = q.poll();
                int flag = p[1] == 0 ? 1 : 0;
                List<Integer> nextList = p[1] == 0 ? blueEdge.get(p[0]) : redEdge.get(p[0]);
                for (int next : nextList) {
                    if (visited[next][flag]) continue;
                    q.add(new int[]{next, flag});
                    visited[next][flag] = true;
                    if (ret[next] != -1) ret[next] = Math.min(ret[next], len + 1);
                    else ret[next] = len + 1;
                }
            }
            ++len;
        }
        return ret;
    }
}
