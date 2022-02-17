package com.leo.leetcode.algorithm.q0800;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 在有向图中，以某个节点为起始节点，从该点出发，每一步沿着图中的一条有向边行走。如果到达的节点是终点（即它没有连出的有向边），则停止。
 * 对于一个起始节点，如果从该节点出发，无论每一步选择沿哪条有向边行走，最后必然在有限步内到达终点，则将该起始节点称作是 安全 的。
 * 返回一个由图中所有安全的起始节点组成的数组作为答案。答案数组中的元素应当按 升序 排列。
 * 该有向图有 n 个节点，按 0 到 n - 1 编号，其中 n 是 graph 的节点数。
 * 图以下述形式给出：graph[i] 是编号 j 节点的一个列表，满足 (i, j) 是图的一条有向边。
 * 提示：
 * 1、n == graph.length
 * 2、1 <= n <= 10^4
 * 3、0 <= graph[i].length <= n
 * 4、graph[i] 按严格递增顺序排列。
 * 5、图中可能包含自环。
 * 6、图中边的数目在范围 [1, 4 * 10^4] 内。
 * 链接：https://leetcode-cn.com/problems/find-eventual-safe-states
 */
public class Q802 {

    public static void main(String[] args) {
        // [4]
        System.out.println(new Q802().eventualSafeNodes(stringToInt2dArray("[[1,2,3,4],[1,2],[3,4],[0,4],[]]")));
        // [2,4,5,6]
        System.out.println(new Q802().eventualSafeNodes(stringToInt2dArray("[[1,2],[2,3],[5],[0],[5],[],[]]")));
    }

    public List<Integer> eventualSafeNodes(int[][] graph) {
        List<Integer> ret = new ArrayList<>();
        int n = graph.length;
        int[] flags = new int[n];
        Arrays.fill(flags, -1);
        for (int i = 0; i < n; i++) {
            Set<Integer> path = new HashSet<>();
            path.add(i);
            if (checkSafe(graph, flags, i, path)) ret.add(i);
        }
        return ret;
    }

    boolean checkSafe(int[][] graph, int[] flags, int i, Set<Integer> path) {
        if (flags[i] == 0) return true;
        if (flags[i] == 1) return false;
        boolean ret = true;
        for (int next : graph[i]) {
            if (path.contains(next)) {
                ret = false;
                flags[next] = 1;
                break;
            }
            path.add(next);
            if (!checkSafe(graph, flags, next, path)) {
                ret = false;
                break;
            }
            path.remove(next);
        }
        flags[i] = ret ? 0 : 1;
        return ret;
    }
}
