package com.leo.leetcode.algorithm.q1500;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：
 * <p>
 * 类型 1：只能由 Alice 遍历。
 * 类型 2：只能由 Bob 遍历。
 * 类型 3：Alice 和 Bob 都可以遍历。
 * 给你一个数组 edges ，其中 edges[i] = [type_i, ui, vi] 表示节点 ui 和 vi 之间存在类型为 type_i 的双向边。
 * 请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。
 * 如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。
 * <p>
 * 返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
 * 3、edges[i].length == 3
 * 4、1 <= edges[i][0] <= 3
 * 5、1 <= edges[i][1] < edges[i][2] <= n
 * 6、所有元组 (type_i, ui, vi) 互不相同
 * <p>
 * 链接：https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable
 */
public class Q1579 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q1579().maxNumEdgesToRemove(4, stringToInt2dArray("[[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]")));
        // 0
        System.out.println(new Q1579().maxNumEdgesToRemove(4, stringToInt2dArray("[[3,1,2],[3,2,3],[1,1,4],[2,1,4]]")));
        // -1
        System.out.println(new Q1579().maxNumEdgesToRemove(4, stringToInt2dArray("[[3,2,3],[1,1,2],[2,3,4]]")));
    }

    int[] alice;
    int[] bob;

    public int maxNumEdgesToRemove(int n, int[][] edges) {
        int ret = 0, cAlice = 0, cBob = 0;
        alice = new int[n];
        bob = new int[n];
        for (int i = 0; i < n; i++) {
            alice[i] = i;
            bob[i] = i;
        }
        for (int[] edge : edges) {
            if (edge[0] == 3) {
                // both
                if (merge(edge[1], edge[2], alice)) {
                    merge(edge[1], edge[2], bob);
                    cAlice++;
                    cBob++;
                } else {
                    ret++;
                }
            }
        }
        for (int[] edge : edges) {
            if (edge[0] == 1) {
                // Alice
                if (merge(edge[1], edge[2], alice)) cAlice++;
                else ret++;
            } else if (edge[0] == 2) {
                // bob
                if (merge(edge[1], edge[2], bob)) cBob++;
                else ret++;
            }
        }
        return cBob < n - 1 || cAlice < n - 1 ? -1 : ret;
    }

    int find(int x, int[] parent) {
        return parent[x] == x ? x : (parent[x] = find(parent[x], parent));
    }

    boolean merge(int i0, int i1, int[] parent) {
        int r0 = find(i0 - 1, parent), r1 = find(i1 - 1, parent);
        if (r0 == r1) return false;
        parent[r1] = r0;
        return true;
    }
}
