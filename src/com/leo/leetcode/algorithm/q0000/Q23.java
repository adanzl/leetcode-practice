package com.leo.leetcode.algorithm.q0000;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;

public class Q23 {

    public static void main(String[] args) {
        System.out.println(LCUtil.listNodeToString(new Q23().mergeKLists(LCUtil.stringToListNodeArray("[[1,4,5],[1,3,4],[2,6]]")))); // 1->1->2->3->4->4->5->6
    }

    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0) return null;
        int step = 1;
        while (step < lists.length) {
            int i = 0;
            while (i + step < lists.length) {
                lists[i] = mergeList(lists[i], lists[i + step]);
                i += step + step;
            }
            step <<= 1;
        }
        return lists[0];
    }

    ListNode mergeList(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0), p = head;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                p.next = l1;
                l1 = l1.next;
            } else {
                p.next = l2;
                l2 = l2.next;
            }
            p = p.next;
        }
        if (l1 != null) p.next = l1;
        if (l2 != null) p.next = l2;
        return head.next;
    }
//    public ListNode mergeKLists(ListNode[] lists) {
//        if (lists.length == 0) return null;
//        ListNode ret = null, p = null;
//        for (int i = lists.length; i >= 0; i--) {
//            adjust(lists, i);
//        }
//
//        while (lists[0] != null) {
//            if (ret == null) {
//                ret = lists[0];
//                p = ret;
//            } else {
//                p.next = lists[0];
//                p = p.next;
//            }
//            lists[0] = lists[0].next;
//            adjust(lists, 0);
//        }
//
//        return ret;
//    }
//
//    void adjust(ListNode[] lists, int i) {
//        ListNode l = getNode(lists, 2 * i + 1);
//        ListNode r = getNode(lists, 2 * i + 2);
//        ListNode n = getNode(lists, i);
//        if (l == null && r == null) return;
//        if ((r == null && compear(n, l)) || ((n == null || compear(n, l)) && compear(r, l))) {
//            lists[2 * i + 1] = n;
//            lists[i] = l;
//            adjust(lists, 2 * i + 1);
//        } else if ((compear(n, r)) && !compear(r, l)) {
//            lists[2 * i + 2] = n;
//            lists[i] = r;
//            adjust(lists, 2 * i + 2);
//        }
//    }
//
//    boolean compear(ListNode l1, ListNode l2) {
//        if (l1 == null) return true;
//        if (l2 == null) return false;
//        return l1.val > l2.val;
//    }
//
//    ListNode getNode(ListNode[] lists, int i) {
//        if (i < 0 || i >= lists.length) return null;
//        return lists[i];
//    }
}
