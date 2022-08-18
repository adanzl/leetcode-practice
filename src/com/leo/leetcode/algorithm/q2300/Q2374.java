package com.leo.leetcode.algorithm.q2300;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个有向图，图中有 n 个节点，节点编号从 0 到 n - 1 ，其中每个节点都 恰有一条 出边。
 * 图由一个下标从 0 开始、长度为 n 的整数数组 edges 表示，其中 edges[i] 表示存在一条从节点 i 到节点 edges[i] 的 有向 边。
 * 节点 i 的 边积分 定义为：所有存在一条指向节点 i 的边的节点的 编号 总和。
 * 返回 边积分 最高的节点。如果多个节点的 边积分 相同，返回编号 最小 的那个。
 * 提示：
 * 1、n == edges.length
 * 2、2 <= n <= 10^5
 * 3、0 <= edges[i] < n
 * 4、edges[i] != i
 * 链接：https://leetcode.cn/problems/node-with-highest-edge-score
 */
public class Q2374 {

    public static void main(String[] args) {
        // 7
        System.out.println(new Q2374().edgeScore(stringToIntegerArray("[1,0,0,0,0,7,7,5]")));
        // 0
        System.out.println(new Q2374().edgeScore(stringToIntegerArray("[2,0,0,2]")));
    }

    public int edgeScore(int[] edges) {
        int n = edges.length;
        long[][] sum = new long[n][2];
        for (int i = 0; i < n; i++) sum[i][0] = i;
        for (int i = 0; i < n; i++) {
            sum[edges[i]][1] += i;
        }
        Arrays.sort(sum, (a, b) -> a[1] != b[1] ? Long.compare(b[1], a[1]) : Long.compare(a[0], b[0]));
        return (int) sum[0][0];
    }
}
