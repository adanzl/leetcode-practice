package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;

public class Q206 {
    public void TestOJ() {
        System.out.println(reverseList(LCUtil.stringToListNode("[1,2,3,4,5,6]")));
    }

    public ListNode reverseList(ListNode head) {
        ListNode p = head.next;
        head.next = null;
        while (p != null) {
            ListNode next = p.next;
            p.next = head;
            head = p;
            p = next;
        }
        return head;
    }
}
