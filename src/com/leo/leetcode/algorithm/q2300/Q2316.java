package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToInt2dArray;

import java.util.*;

/**
 * 给你一个整数 n ，表示一张 无向图 中有 n 个节点，编号为 0 到 n - 1 。
 * 同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边。
 * 请你返回 无法互相到达 的不同 点对数目 。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、0 <= edges.length <= 2 * 10^5
 * 3、edges[i].length == 2
 * 4、0 <= ai, bi < n
 * 5、ai != bi
 * 6、不会有重复边。
 * 链接：https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph
 */
public class Q2316 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q2316().countPairs(3, stringToInt2dArray("[[0,1],[0,2],[1,2]]")));
        // 14
        System.out.println(new Q2316().countPairs(7, stringToInt2dArray("[[0,2],[0,5],[2,4],[1,6],[5,4]]")));
    }

    int[] parent;

    public long countPairs(int n, int[][] edges) {
        this.parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int[] edge : edges) merge(edge[0], edge[1]);
        Map<Integer, Integer> cMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int r = find(i);
            cMap.put(r, cMap.getOrDefault(r, 0) + 1);
        }
        long ret = 0, sum = 0;
        for (int v : cMap.values()) sum += v;
        for (int v : cMap.values()) ret += v * (sum - v);
        return ret / 2;
    }

    void merge(int i_0, int i_1) {
        int r_0 = find(i_0), r_1 = find(i_1);
        if (r_0 != r_1) parent[r_1] = r_0;
    }

    int find(int x) {
        return parent[x] == x ? parent[x] : (parent[x] = find(parent[x]));
    }
}
