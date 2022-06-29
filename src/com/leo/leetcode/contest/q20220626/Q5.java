package com.leo.leetcode.contest.q20220626;

import java.util.HashSet;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 链接：https://leetcode.cn/contest/sf-tech/problems/BN8jAm/
 */
public class Q5 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q5().isCompliance(stringToInt2dArray("[[0,1,3], [1,0,3], [3,3,0]]"), 2));
        // false
        System.out.println(new Q5().isCompliance(stringToInt2dArray("[[0,3,3],[3,0,3],[3,3,0]]"), 2));
    }

    public boolean isCompliance(int[][] distance, int n) {
        int nCa = distance.length;
        this.parent = new int[nCa];
        for (int i = 0; i < nCa; i++) parent[i] = i;
        for (int i = 0; i < nCa; i++) {
            for (int j = 0; j < nCa; j++) {
                if (distance[i][j] <= 2) {
                    merge(i, j);
                }
            }
        }
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nCa; i++) {
            set.add(find(i));
        }
        return n >= set.size();
    }

    int[] parent;

    void merge(int i_0, int i_1) {
        int r_0 = find(i_0), r_1 = find(i_1);
        if (r_0 != r_1) parent[r_1] = r_0;
    }

    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
}
