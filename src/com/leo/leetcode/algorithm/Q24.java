package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;

/**
 * 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
 * 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
 * 链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs/
 */

public class Q24 {
    public static void main(String[] args) {
        System.out.println(new Q24().swapPairs(LCUtil.stringToListNode("[1,2,3,4]"))); // [2,1,4,3]
    }

    public ListNode swapPairs(ListNode head) {
        ListNode h = new ListNode(0);
        h.next = head;
        ListNode p = h;
        while (true) {
            ListNode n1 = p.next;
            if (n1 == null) break;
            ListNode n2 = n1.next;
            if (n2 == null) break;
            ListNode n3 = n2.next;
            p.next = n2;
            n2.next = n1;
            n1.next = n3;
            p = n1;
        }

        return h.next;
    }
}
