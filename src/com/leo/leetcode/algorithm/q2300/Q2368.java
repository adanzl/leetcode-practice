package com.leo.leetcode.algorithm.q2300;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 现有一棵由 n 个节点组成的无向树，节点编号从 0 到 n - 1 ，共有 n - 1 条边。
 * 给你一个二维整数数组 edges ，长度为 n - 1 ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。另给你一个整数数组 restricted 表示 受限 节点。
 * 在不访问受限节点的前提下，返回你可以从节点 0 到达的 最多 节点数目。
 * 注意，节点 0 不 会标记为受限节点。
 * 提示：
 * 1、2 <= n <= 10^5
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、0 <= ai, bi < n
 * 5、ai != bi
 * 6、edges 表示一棵有效的树
 * 7、1 <= restricted.length < n
 * 8、1 <= restricted[i] < n
 * 9、restricted 中的所有值 互不相同
 * 链接：https://leetcode.cn/problems/reachable-nodes-with-restrictions
 */
public class Q2368 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q2368().reachableNodes(7
                , stringToInt2dArray("[[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]")
                , stringToIntegerArray("[4,5]")));
        // 3
        System.out.println(new Q2368().reachableNodes(7
                , stringToInt2dArray("[[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]")
                , stringToIntegerArray("[4,2,1]")));
    }

    int[] count, parent;

    public int reachableNodes(int n, int[][] edges, int[] restricted) {
        Set<Integer> set = new HashSet<>(restricted.length);
        for (int v : restricted) set.add(v);
        parent = new int[n];
        count = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        Arrays.fill(count, 1);
        for (int[] edge : edges) {
            if (set.contains(edge[0]) || set.contains(edge[1])) continue;
            merge(edge[0], edge[1]);
        }
        return count[find(0)];
    }

    int find(int v) {
        return parent[v] == v ? v : (parent[v] = find(parent[v]));
    }

    void merge(int v1, int v2) {
        int r1 = find(v1), r2 = find(v2);
        if (r1 == r2) return;
        parent[r2] = r1;
        count[r1] += count[r2];
        count[r2] = 0;
    }
}
