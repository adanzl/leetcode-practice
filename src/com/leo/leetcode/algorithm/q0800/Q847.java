package com.leo.leetcode.algorithm.q0800;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。
 * 给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。
 * 返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。
 * 提示：
 * 1、n == graph.length
 * 2、1 <= n <= 12
 * 3、0 <= graph[i].length < n
 * 4、graph[i] 不包含 i
 * 5、如果 graph[a] 包含 b ，那么 graph[b] 也包含 a
 * 6、输入的图总是连通图
 * 链接：https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes
 */
public class Q847 {

    public static void main(String[] args) {
        // 14
        System.out.println(new Q847().shortestPathLength(stringToInt2dArray("[[2,3,5,7],[2,3,7],[0,1],[0,1],[7],[0],[10],[9,10,0,1,4],[9],[7,8],[7,6]]")));
        // 4
        System.out.println(new Q847().shortestPathLength(stringToInt2dArray("[[1,2,3],[0],[0],[0]]")));
        // 4
        System.out.println(new Q847().shortestPathLength(stringToInt2dArray("[[1],[0,2,4],[1,3,4],[2],[1,2]]")));
    }

    public int shortestPathLength(int[][] graph) {
        int n = graph.length, END = (1 << n) - 1;
        int[] ret = new int[n];
        boolean[][] marks = new boolean[n][1 << n];
        List<Queue<Integer>> qList = new ArrayList<>(n);
        List<Queue<Integer>> markList = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            Queue<Integer> q = new ArrayDeque<>();
            q.add(i);
            qList.add(q);
            Queue<Integer> m = new ArrayDeque<>();
            m.add(1 << i);
            markList.add(m);
        }
        while (true) {
            for (int i = 0; i < n; i++) {
                Queue<Integer> qMark = markList.get(i);
                Queue<Integer> q = qList.get(i);
                int size = q.size();
                while (size-- > 0 && !q.isEmpty()) {
                    int node = q.poll();
                    int mark = !qMark.isEmpty() ? qMark.poll() : 0;
                    if (mark == END) return ret[i];
                    for (int next : graph[node]) {
                        int nMark = mark | (1 << next);
                        if (marks[next][nMark]) continue;
                        marks[next][nMark] = true;
                        q.add(next);
                        qMark.add(nMark);
                    }
                }
                ret[i]++;
            }
        }
    }
}
