package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.ListNode;

import static com.leo.utils.LCUtil.stringToListNode;
import static com.leo.utils.LCUtil.listNodeToString;

/**
 * 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
 * 链接：https://leetcode-cn.com/problems/remove-linked-list-elements/
 */
public class Q203 {

    public static void main(String[] args) {
        // [1,2,3,4,5]
        System.out.println(listNodeToString(new Q203().removeElements(stringToListNode("[1,2,6,3,4,5,6]"), 6)));
        // []
        System.out.println(listNodeToString(new Q203().removeElements(stringToListNode("[]"), 1)));
        // []
        System.out.println(listNodeToString(new Q203().removeElements(stringToListNode("[7,7,7,7,7,7]"), 7)));
    }

    public ListNode removeElements(ListNode head, int val) {
        ListNode p = head, h = new ListNode(0), pre = h;
        h.next = head;
        while (p != null) {
            if (p.val == val) {
                p = p.next;
                pre.next = p;
            } else {
                pre = p;
                p = p.next;
            }
        }
        return h.next;
    }
}
