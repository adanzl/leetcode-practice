package com.leo.leetcode.algorithm.q0000;

import com.leo.utils.ListNode;

import static com.leo.utils.LCUtil.stringToListNode;
import static com.leo.utils.LCUtil.listNodeToString;

/**
 * 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
 * 提示：
 * 1、链表中节点数目为 n
 * 2、1 <= n <= 500
 * 3、-500 <= Node.val <= 500
 * 4、1 <= left <= right <= n
 * 进阶： 你可以使用一趟扫描完成反转吗？
 * 链接：https://leetcode.cn/problems/reverse-linked-list-ii
 */
public class Q92 {

    public static void main(String[] args) {
        // {1,4,3,2,5}
        System.out.println(listNodeToString(new Q92().reverseBetween(stringToListNode("[1,2,3,4,5]"), 2, 4)));
        // {5}
        System.out.println(listNodeToString(new Q92().reverseBetween(stringToListNode("[5]"), 1, 1)));
    }

    public ListNode reverseBetween(ListNode head, int m, int n) {
        // write code here
        ListNode h = new ListNode(-1), p1 = h;
        h.next = head;
        int count = 1;
        while (count++ < m) p1 = p1.next;
        ListNode p = p1.next, next = p.next, p2 = p;
        while (count++ <= n) {
            ListNode nNext = next.next;
            next.next = p;
            p = next;
            next = nNext;
        }
        p1.next = p;
        p2.next = next;
        return h.next;
    }
}
