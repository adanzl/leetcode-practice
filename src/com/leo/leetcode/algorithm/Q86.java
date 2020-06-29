package com.leo.leetcode.algorithm;

import com.leo.utils.ListNode;

import static com.leo.utils.LCUtil.listNodeToString;
import static com.leo.utils.LCUtil.stringToListNode;

/**
 * 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
 * 你应当保留两个分区中每个节点的初始相对位置。
 * 链接：https://leetcode-cn.com/problems/partition-list/
 */
public class Q86 {

    public static void main(String[] args) {
        System.out.println(listNodeToString(new Q86().partition(stringToListNode("[1,4,3,2,5,2]"), 3))); // 1->2->2->4->3->5
    }

    public ListNode partition(ListNode head, int x) {
        ListNode l1 = new ListNode(0), l2 = new ListNode(0), p = head, p1 = l1, p2 = l2;
        while (p != null) {
            if (p.val < x) {
                p1.next = p;
                p1 = p1.next;
            } else {
                p2.next = p;
                p2 = p2.next;
            }
            p = p.next;
        }
        p2.next = null;
        if (l1.next == null) return l2.next;
        p1.next = l2.next;
        return l1.next;
    }
}
