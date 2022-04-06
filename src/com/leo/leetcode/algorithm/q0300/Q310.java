package com.leo.leetcode.algorithm.q0300;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
 * 给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。
 * 给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。
 * 可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。
 * 在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。
 * 请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。
 * 树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。
 * 提示：
 * 1、1 <= n <= 2 * 10^4
 * 2、edges.length == n - 1
 * 3、0 <= ai, bi < n
 * 4、ai != bi
 * 5、所有 (ai, bi) 互不相同
 * 6、给定的输入 保证 是一棵树，并且 不会有重复的边
 * 链接：https://leetcode-cn.com/problems/minimum-height-trees
 */
public class Q310 {
    // 拓扑排序思路
    public static void main(String[] args) {
        // [0]
        System.out.println(new Q310().findMinHeightTrees(1, stringToInt2dArray("[]")));
        //
        System.out.println(new Q310().findMinHeightTrees(2, stringToInt2dArray("[[0,1]]")));
        // [3,4]
        System.out.println(new Q310().findMinHeightTrees(6, stringToInt2dArray("[[3,0],[3,1],[3,2],[3,4],[5,4]]")));
        // [1]
        System.out.println(new Q310().findMinHeightTrees(4, stringToInt2dArray("[[1,0],[1,2],[1,3]]")));
    }


    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Integer> ret = new ArrayList<>();
        if (n == 1) {
            ret.add(0);
            return ret;
        }
        List<List<Integer>> nextList = new ArrayList<>();
        Set<Integer> removed = new HashSet<>();
        int[] nNext = new int[n];
        for (int i = 0; i < n; i++) nextList.add(new ArrayList<>());
        for (int[] edge : edges) {
            nextList.get(edge[0]).add(edge[1]);
            nextList.get(edge[1]).add(edge[0]);
            nNext[edge[0]]++;
            nNext[edge[1]]++;
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
        for (int i = 0; i < n; i++) pq.offer(new int[]{nextList.get(i).size(), i});
        while (removed.size() < n - 2) {
            List<int[]> tmp = new ArrayList<>();
            while (!pq.isEmpty() && pq.peek()[0] == 1) {
                int[] p = pq.poll();
                if (removed.contains(p[1])) continue;
                List<Integer> lNext = nextList.get(p[1]);
                for (int next : lNext) {
                    if (nNext[next] == 1) continue;
                    tmp.add(new int[]{--nNext[next], next});
                }
                removed.add(p[1]);
            }
            pq.addAll(tmp);
        }
        while (!pq.isEmpty() && pq.peek()[0] == 1) ret.add(pq.poll()[1]);
        return ret;
    }

}
