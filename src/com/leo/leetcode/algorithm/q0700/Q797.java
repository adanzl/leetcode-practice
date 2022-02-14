package com.leo.leetcode.algorithm.q0700;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
 * graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。
 * 提示：
 * 1、n == graph.length
 * 2、2 <= n <= 15
 * 3、0 <= graph[i][j] < n
 * 4、graph[i][j] != i（即不存在自环）
 * 5、graph[i] 中的所有元素 互不相同
 * 6、保证输入为 有向无环图（DAG）
 * 链接：https://leetcode-cn.com/problems/all-paths-from-source-to-target
 */
public class Q797 {

    public static void main(String[] args) {
        // [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
        System.out.println(new Q797().allPathsSourceTarget(stringToInt2dArray("[[4,3,1],[3,2,4],[3],[4],[]]")));
        // [[0,2,1,3]]
        System.out.println(new Q797().allPathsSourceTarget(stringToInt2dArray("[[2],[3],[1],[]]")));
        // [[0,1,3],[0,2,3]]
        System.out.println(new Q797().allPathsSourceTarget(stringToInt2dArray("[[1,2],[3],[3],[]]")));
    }

    List<List<Integer>> ans = new ArrayList<>();
    Deque<Integer> dq = new ArrayDeque<>();

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        dq.offerLast(0);
        dfs(graph, 0, graph.length - 1);
        return ans;
    }

    public void dfs(int[][] graph, int x, int n) {
        if (x == n) {
            ans.add(new ArrayList<>(dq));
            return;
        }
        for (int v : graph[x]) {
            dq.offerLast(v);
            dfs(graph, v, n);
            dq.pollLast();
        }
    }
}
