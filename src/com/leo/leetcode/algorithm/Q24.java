package com.leo.leetcode.algorithm;

import com.leo.utils.ListNode;

public class Q24 {
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
