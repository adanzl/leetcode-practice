package com.leo.leetcode.algorithm.q2300;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，每个节点 至多 有一条出边。
 * 有向图用大小为 n 下标从 0 开始的数组 edges 表示，表示节点 i 有一条有向边指向 edges[i] 。如果节点 i 没有出边，那么 edges[i] == -1 。
 * 同时给你两个节点 node1 和 node2 。
 * 请你返回一个从 node1 和 node2 都能到达节点的编号，使节点 node1 和节点 node2 到这个节点的距离 较大值最小化。如果有多个答案，请返回 最小 的节点编号。如果答案不存在，返回 -1 。
 * 注意 edges 可能包含环。
 * 提示：
 * 1、n == edges.length
 * 2、2 <= n <= 10^5
 * 3、-1 <= edges[i] < n
 * 4、edges[i] != i
 * 5、0 <= node1, node2 < n
 * 链接：https://leetcode.cn/problems/find-closest-node-to-given-two-nodes
 */
public class Q2359 {

    public static void main(String[] args) {

        // 1
        System.out.println(new Q2359().closestMeetingNode(stringToIntegerArray("[4,4,8,-1,9,8,4,4,1,1]"), 5, 6));
        // 0
        System.out.println(new Q2359().closestMeetingNode(stringToIntegerArray("[2,0,0]"), 2, 0));
        // 2
        System.out.println(new Q2359().closestMeetingNode(stringToIntegerArray("[1,2,-1]"), 0, 2));
        // 1
        System.out.println(new Q2359().closestMeetingNode(stringToIntegerArray("[4,4,4,5,1,2,2]"), 1, 1));
        // 2
        System.out.println(new Q2359().closestMeetingNode(stringToIntegerArray("[2,2,3,-1]"), 0, 1));
    }

    public int closestMeetingNode(int[] edges, int node1, int node2) {
        int n = edges.length, p1 = node1, pp1 = p1, p2 = node2, pp2 = p2, l1 = 0, l2 = 0, min = Integer.MAX_VALUE, ret = -1;
        int[] len1 = new int[n], len2 = new int[n];
        Arrays.fill(len1, -1);
        Arrays.fill(len2, -1);
        while (p1 != -1) {
            if (len1[p1] == -1) len1[p1] = l1;
            p1 = edges[p1];
            if (pp1 != -1) pp1 = edges[pp1];
            if (pp1 != -1) pp1 = edges[pp1];
            if (pp1 == p1 && l1 != 0 && p1 != -1 && len1[p1] != -1) break;
            l1++;
        }
        while (p2 != -1) {
            if (len2[p2] == -1) len2[p2] = l2;
            p2 = edges[p2];
            if (pp2 != -1) pp2 = edges[pp2];
            if (pp2 != -1) pp2 = edges[pp2];
            if (pp2 == p2 && l2 != 0 && p2 != -1 && len2[p2] != -1) break;
            l2++;
        }
        for (int i = 0; i < n; i++) {
            if (len1[i] != -1 && len2[i] != -1) {
                int v = Math.max(len1[i] , len2[i]);
                if (v < min) {
                    ret = i;
                    min = v;
                }
            }
        }
        return ret;
    }
}
