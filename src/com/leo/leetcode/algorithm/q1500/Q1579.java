package com.leo.leetcode.algorithm.q1500;

import static com.leo.utils.LCUtil.stringToInt2dArray;

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
