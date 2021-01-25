package com.leo.leetcode.algorithm.q1300;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。
 * 线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。
 * 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。
 * 给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。
 * 请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。
 * <p>
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、1 <= connections.length <= min(n*(n-1)/2, 10^5)
 * 3、connections[i].length == 2
 * 4、0 <= connections[i][0], connections[i][1] < n
 * 5、connections[i][0] != connections[i][1]
 * 6、没有重复的连接。
 * 7、两台计算机不会通过多条线缆连接。
 * <p>
 * 链接：https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected
 */
public class Q1319 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q1319().makeConnected(12, stringToInt2dArray("[[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]")));
        // 1
        System.out.println(new Q1319().makeConnected(4, stringToInt2dArray("[[0,1],[0,2],[1,2]]")));
        // 2
        System.out.println(new Q1319().makeConnected(6, stringToInt2dArray("[[0,1],[0,2],[0,3],[1,2],[1,3]]")));
        // -1
        System.out.println(new Q1319().makeConnected(6, stringToInt2dArray("[[0,1],[0,2],[0,3],[1,2]]")));
        // 0
        System.out.println(new Q1319().makeConnected(5, stringToInt2dArray("[[0,1],[0,2],[3,4],[2,3]]")));
    }

    int[] parent;

    public int makeConnected(int n, int[][] connections) {
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int group = n, duplicated = 0;
        for (int[] con : connections) {
            if (merge(con[0], con[1])) group--;
            else duplicated++;
        }
        return duplicated >= group - 1 ? group - 1 : -1;
    }

    int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }

    boolean merge(int i0, int i1) {
        int r0 = find(i0), r1 = find(i1);
        if (r0 == r1) return false;
        parent[r1] = r0;
        return true;
    }
}
