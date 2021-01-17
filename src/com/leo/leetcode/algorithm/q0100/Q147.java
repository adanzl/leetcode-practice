package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;

public class Q147 {
    public void TestOJ() {
        System.out.println(LCUtil.listNodeToString(insertionSortList(LCUtil.stringToListNode("[4,2,1,3]")))); //
        System.out.println(LCUtil.listNodeToString(insertionSortList(LCUtil.stringToListNode("[-1,5,3,4,0]")))); //
    }

    public ListNode insertionSortList(ListNode head) {
        ListNode out = new ListNode(0);
        while (head != null) {
            ListNode v = head;
            head = head.next;
            ListNode p = out.next, pre = out;
            while (p != null) {
                if (v.val < p.val) {
                    pre.next = v;
                    v.next = p;
                    break;
                }
                pre = p;
                p = p.next;
            }
            if (p == null) {
                pre.next = v;
                v.next = null;
            }
        }
        return out.next;
    }
}
