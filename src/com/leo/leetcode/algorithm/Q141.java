package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;
import org.junit.Test;

public class Q141 {
    @Test
    public void TestOJ() {
        ListNode p = LCUtil.stringToListNode("[3,2,0,-4]");
        LCUtil.buildListNode(p, 1); // t
        System.out.println(hasCycle(p));
        p = LCUtil.stringToListNode("[1,2]");
        LCUtil.buildListNode(p, 0); // t
        System.out.println(hasCycle(p));
        p = LCUtil.stringToListNode("[1]");
        LCUtil.buildListNode(p, -1); // f
        System.out.println(hasCycle(p));
    }

    public boolean hasCycle(ListNode head) {

        ListNode fast = head, slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {
                return true;
            }
        }
        return false;
    }
}
