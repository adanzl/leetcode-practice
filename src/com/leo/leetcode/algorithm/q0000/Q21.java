package com.leo.leetcode.algorithm.q0000;

import com.leo.utils.ListNode;

public class Q21 {

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode ret = null;
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode p = null;
        while (true) {
            ListNode node;
            if (p1.val < p2.val) {
                node = p1;
                p1 = p1.next;
            } else {
                node = p2;
                p2 = p2.next;
            }
            if (ret == null) {
                ret = node;
                p = ret;
            } else {
                p.next = node;
                p = p.next;
            }

            if (p1 == null) {
                p.next = p2;
                break;
            }
            if (p2 == null) {
                p.next = p1;
                break;
            }
        }
        return ret;
    }
}
