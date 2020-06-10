package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;

public class Q25 {

    public static void main(String[] args) {
        System.out.println(LCUtil.listNodeToString(new Q25().reverseKGroup(LCUtil.stringToListNode("[1,2,3,4,5]"), 2))); // [{2}->{1}->{4}->{3}->{5}]
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode p = head, h = new ListNode(0), pre = h;
        h.next = head;
        int i = 0;
        while (p != null) {
            if (i == k - 1) {
                ListNode next = p.next, start = pre.next;
                pre.next = reverse(start, p);
                // fun will reverse start and end
                start.next = next;
                pre = start;
                p = next;
                i = 0;
            } else {
                i++;
                p = p.next;
            }
        }
        return h.next;
    }

    ListNode reverse(ListNode head, ListNode end){
        ListNode p = head, pre = null;
        while(pre != end){
            ListNode next = p.next;
            p.next = pre;
            pre = p;
            p = next;
        }
        return end;
    }
}
