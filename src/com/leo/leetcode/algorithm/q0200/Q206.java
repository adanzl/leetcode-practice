package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.ListNode;

import static com.leo.utils.LCUtil.listNodeToString;
import static com.leo.utils.LCUtil.stringToListNode;

/**
 * 反转一个单链表。
 * <p>
 * 进阶:
 * 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
 * <p>
 * 链接：https://leetcode-cn.com/problems/reverse-linked-list/
 */
public class Q206 {
    public static void main(String[] args) {
        // [[6]->[5]->[4]->[3]->[2]->[1]]
        System.out.println(listNodeToString(new Q206().reverseList(stringToListNode("[1,2,3,4,5,6]"))));
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
