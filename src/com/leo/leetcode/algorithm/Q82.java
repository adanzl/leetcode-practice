package com.leo.leetcode.algorithm;

import com.leo.utils.ListNode;

import static com.leo.utils.LCUtil.stringToListNode;
import static com.leo.utils.LCUtil.listNodeToString;

/**
 * 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
 * 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
 */
public class Q82 {

    public static void main(String[] args) {
        System.out.println(listNodeToString(new Q82().deleteDuplicates(stringToListNode("[1,2,3,3,4,4,5]")))); // [1->2->5]
        System.out.println(listNodeToString(new Q82().deleteDuplicates(stringToListNode("[1,1,1,2,3]")))); // [2->3]
        System.out.println(listNodeToString(new Q82().deleteDuplicates(stringToListNode("[1,1]")))); // []
        System.out.println(listNodeToString(new Q82().deleteDuplicates(stringToListNode("[1]")))); // [1]
        System.out.println(listNodeToString(new Q82().deleteDuplicates(stringToListNode("[]")))); // []
    }

    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;
        ListNode n = new ListNode(0), pre = n, p = head.next, mem = head;
        n.next = head;
        boolean duplicate = false;
        while (p != null) {
            if (p.val != mem.val) {
                if (!duplicate) {
                    pre.next = mem;
                    pre = pre.next;
                }
                mem = p;
                duplicate = false;
            } else {
                duplicate = true;
            }
            p = p.next;
        }
        if (!duplicate) {
            pre.next = mem;
            pre = pre.next;
        }
        pre.next = null;
        return n.next;
    }
}
