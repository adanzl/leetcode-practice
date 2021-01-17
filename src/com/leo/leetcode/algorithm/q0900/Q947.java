package com.leo.leetcode.algorithm.q0900;

import com.leo.utils.LCUtil;

/**
 * n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。
 * 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。
 * 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。
 * 提示：
 * 1、1 <= stones.length <= 1000
 * 2、0 <= xi, yi <= 10^4
 * 3、不会有两块石头放在同一个坐标点上
 * 链接：https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column
 */
public class Q947 {

    public static void main(String[] args) {
        System.out.println(new Q947().removeStones(LCUtil.stringToInt2dArray("[[0,0],[0,2],[1,1],[2,0],[2,2]]"))); // 3
        System.out.println(new Q947().removeStones(LCUtil.stringToInt2dArray("[[2,5],[4,6],[3,1],[6,0],[2,1],[2,0],[6,2],[1,0],[3,4],[1,1]]"))); // 8
        System.out.println(new Q947().removeStones(LCUtil.stringToInt2dArray("[[0,0],[0,1],[1,0],[1,1],[2,1],[2,2],[3,2],[3,3],[3,4],[4,3],[4,4]]"))); // 10
        System.out.println(new Q947().removeStones(LCUtil.stringToInt2dArray("[[0,1],[1,2],[1,3],[3,3],[2,3],[0,2]]"))); // 5
        System.out.println(new Q947().removeStones(LCUtil.stringToInt2dArray("[[0,0]]"))); // 0
        System.out.println(new Q947().removeStones(LCUtil.stringToInt2dArray("[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]"))); // 5
    }

    public int removeStones(int[][] stones) {
        int count = 0;
        Node head = new Node(null);
        for (int[] pos : stones) {
            Node p = head.next, parent = null, pre = head;
            boolean bFound = false;
            DNode dNode = new DNode(pos);
            while (p != null) {
                DNode pDNode = p.data;
                boolean bRemoveNode = false;
                while (pDNode != null) {
                    if (dNode.x == pDNode.x || dNode.y == pDNode.y) {
                        bFound = true;
                        if (parent == null) {
                            parent = p;
                            p.tail.next = dNode;
                            p.tail = dNode;
                        } else {
                            parent.tail.next = p.data;
                            parent.tail = p.tail;
                            bRemoveNode = true;
                            --count;
                        }
                        break;
                    }
                    pDNode = pDNode.next;
                }
                if (bRemoveNode) pre.next = p.next;
                else pre = p;
                p = p.next;
            }
            if (!bFound) {
                pre.next = new Node(dNode);
                ++count;
            }
        }
        return stones.length - count;
    }


    static class Node {
        DNode data;
        DNode tail;
        Node next;

        Node(DNode data) {
            this.data = data;
            this.tail = data;
        }
    }

    static class DNode {
        DNode next;
        int x;
        int y;

        DNode(int[] pos) {
            this.x = pos[0];
            this.y = pos[1];
        }
    }
}
