package com.leo.leetcode.algorithm.q0600;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 在本问题中, 树指的是一个连通且无环的无向图。
 * 输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
 * 附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
 * 结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。
 * 返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。
 * 答案边 [u, v] 应满足相同的格式 u < v。
 * 注意:
 * 1、输入的二维数组大小在 3 到 1000。
 * 2、二维数组中的整数在1到N之间，其中N是输入数组的大小。
 * <p>
 * 链接：https://leetcode-cn.com/problems/redundant-connection
 */
public class Q684 {

    public static void main(String[] args) {
        // [2,3]
        System.out.println(Arrays.toString(new Q684().findRedundantConnection(stringToInt2dArray("[[1,2], [1,3], [2,3]]"))));
        // [1,4]
        System.out.println(Arrays.toString(new Q684().findRedundantConnection(stringToInt2dArray("[[1,2], [2,3], [3,4], [1,4], [1,5]]"))));
    }

    int[] parent;

    public int[] findRedundantConnection(int[][] edges) {
        parent = new int[edges.length + 1];
        for (int i = 0; i < edges.length; i++) parent[i] = i;
        for (int[] edge : edges) {
            if (!merge(edge[0], edge[1]))
                return new int[]{edge[0], edge[1]};
        }
        return new int[2];
    }

    boolean merge(int i_0, int i_1) {
        int r_0 = find(i_0), r_1 = find(i_1);
        if (r_0 != r_1) parent[r_1] = r_0;
        return r_0 != r_1;
    }

    int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }
}
