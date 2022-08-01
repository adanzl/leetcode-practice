package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，其中每个节点 至多 有一条出边。
 * 图用一个大小为 n 下标从 0 开始的数组 edges 表示，节点 i 到节点 edges[i] 之间有一条有向边。如果节点 i 没有出边，那么 edges[i] == -1 。
 * 请你返回图中的 最长 环，如果没有任何环，请返回 -1 。
 * 一个环指的是起点和终点是 同一个 节点的路径。
 * 提示：
 * 1、n == edges.length
 * 2、2 <= n <= 10^5
 * 3、-1 <= edges[i] < n
 * 4、edges[i] != i
 * 链接：https://leetcode.cn/problems/longest-cycle-in-a-graph
 */
public class Q2360 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2360().longestCycle(stringToIntegerArray("[3,4,0,2,-1,2]")));
        // -1
        System.out.println(new Q2360().longestCycle(stringToIntegerArray("[2,-1,3,1]")));
        // 3
        System.out.println(new Q2360().longestCycle(stringToIntegerArray("[3,3,4,2,3]")));
    }


    public int longestCycle(int[] edges) {
        int n = edges.length, ret = -1;
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;
            int p1 = i, p2 = edges[p1];
            while (p1 != -1 && !visited[p1]) {
                visited[p1] = true;
                if (p2 != -1) p2 = edges[p2];
                if (p2 != -1) p2 = edges[p2];
                if (p2 == p1) {
                    int p = p1, len1 = 1;
                    while (edges[p] != p1) {
                        p = edges[p];
                        len1++;
                    }
                    ret = Math.max(ret, len1);
                    break;
                }
                p1 = edges[p1];
            }
        }
        return ret;
    }
}
