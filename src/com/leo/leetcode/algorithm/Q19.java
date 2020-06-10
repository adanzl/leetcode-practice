package com.leo.leetcode.algorithm;

import com.leo.utils.ListNode;

public class Q19 {

    class LNode {
        ListNode val;
        LNode pre;
        LNode next;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode p = head;
        LNode rHead = new LNode();
        rHead.val = null;
        LNode pR = rHead;
        while (p != null) {
            LNode nNode = new LNode();
            nNode.pre = pR;
            nNode.val = p;
            pR.next = nNode;

            pR = pR.next;
            p = p.next;
        }

        while (--n > 0) {
            pR = pR.pre;
        }
        if (pR.pre.val == null) {
            head = pR.val.next;
        } else {
            pR.pre.val.next = pR.val.next;
        }
        return head;
    }
}
