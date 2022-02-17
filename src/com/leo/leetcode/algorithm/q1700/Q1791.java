package com.leo.leetcode.algorithm.q1700;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 有一个无向的 星型 图，由 n 个编号从 1 到 n 的节点组成。星型图有一个 中心 节点，并且恰有 n - 1 条边将中心节点与其他每个节点连接起来。
 * 给你一个二维整数数组 edges ，其中 edges[i] = [ui, vi] 表示在节点 ui 和 vi 之间存在一条边。请你找出并返回 edges 所表示星型图的中心节点。
 * 提示：
 * 1、3 <= n <= 105
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、1 <= ui, vi <= n
 * 5、ui != vi
 * 6、题目数据给出的 edges 表示一个有效的星型图
 * 链接：https://leetcode-cn.com/problems/find-center-of-star-graph
 */
public class Q1791 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q1791().findCenter(stringToInt2dArray("[[1,2],[2,3],[4,2]]")));
        // 1
        System.out.println(new Q1791().findCenter(stringToInt2dArray("[[1,2],[5,1],[1,3],[1,4]]")));
    }

    public int findCenter(int[][] edges) {
        int n = edges.length + 1;
        int[] count = new int[n];
        for (int[] edge : edges) {
            if (++count[edge[0] - 1] > 1) return edge[0];
            if (++count[edge[1] - 1] > 1) return edge[1];
        }
        return -1;
    }
}
