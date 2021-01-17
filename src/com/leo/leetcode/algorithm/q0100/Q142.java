package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;

public class Q142 {

    public static void main(String[] args) {
        new Q142().TestOJ();
    }

    public void TestOJ() {
        ListNode p;
        p = LCUtil.stringToListNode("[3,2,0,-4]");
        LCUtil.buildListNode(p, 1);
        System.out.println(detectCycle(p));// {2}
        p = LCUtil.stringToListNode("[1,2]");
        LCUtil.buildListNode(p, 0); // {1}
        System.out.println(detectCycle(p));
        p = LCUtil.stringToListNode("[1]");
        LCUtil.buildListNode(p, -1); // null
        System.out.println(detectCycle(p));
        p = LCUtil.stringToListNode("[-1,-7,7,-4,19,6,-9,-5,-2,-5]");
        LCUtil.buildListNode(p, 9); // {-5}
        System.out.println(detectCycle(p));
    }

    public ListNode detectCycle(ListNode head) {
        ListNode fast = head, slow = head, meetPoint = null;
        while (fast != null && fast.next != null) { // fast超过slow一圈后相遇
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {
                meetPoint = fast;
                break;
            }
        }
        if (meetPoint == null) {
            return null;
        }
        while (head != meetPoint) {
            head = head.next;
            meetPoint = meetPoint.next;
        }
        return meetPoint;
    }
}
