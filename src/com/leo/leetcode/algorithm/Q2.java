package com.leo.leetcode.algorithm;

import com.leo.utils.ListNode;

public class Q2 {

    class Solution {
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            ListNode ret = new ListNode(0);
            ListNode node = ret;
            int ext = 0;
            while (true) {
                int v1 = l1 != null ? l1.val : 0;
                int v2 = l2 != null ? l2.val : 0;
                int v = v1 + v2 + ext;
                node.next = new ListNode(v % 10);
                ext = v / 10;

                l1 = l1 != null ? l1.next : null;
                l2 = l2 != null ? l2.next : null;
                if (ext == 0 && l1 == null && l2 == null) {
                    break;
                }
                node = node.next;
            }
            return ret.next;

        }
    }
}
