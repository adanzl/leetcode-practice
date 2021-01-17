package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;

public class Q160 {
    public void TestOJ() {
//        ListNode a = LCUtil.stringToListNode("[4,1,8,4,5]");
//        ListNode b = LCUtil.stringToListNode("[5,0,1]");
//        combine(a, b, 5);
//        System.out.println(getIntersectionNode(a, b)); // 8
        ListNode aHead = new ListNode(-1);
        aHead.next = LCUtil.stringToListNode("[2,3]");
        ListNode bHead = new ListNode(-1);
        bHead.next = LCUtil.stringToListNode("[3]");
        combine(aHead, bHead, 1, 0);
        System.out.println(getIntersectionNode(aHead, bHead)); // 3
    }

    void combine(ListNode aHead, ListNode bHead, int iA, int iB) {
        for (int i = 0; i < iA; i++) {
            aHead = aHead.next;
        }
        for (int i = 0; i < iB; i++) {
            bHead = bHead.next;
        }

        bHead.next = aHead.next;
    }

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        ListNode p1 = headA, p2 = headB;
        int flag1 = 0, flag2 = 0;
        while (true) {
            if (p1 == null) {
                if (flag1 == 0) {
                    flag1 = 1;
                    p1 = headB;
                } else {
                    return null;
                }
            }
            if (p2 == null) {
                if (flag2 == 0) {
                    flag2 = 1;
                    p2 = headA;
                } else {
                    return null;
                }
            }
            if (p1 == p2) {
                break;
            }
            p1 = p1.next;
            p2 = p2.next;
        }
        return p1;
    }
}
