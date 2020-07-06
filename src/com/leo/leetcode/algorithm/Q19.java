package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;

/**
 * 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
 * 说明：
 * 给定的 n 保证是有效的。
 * 进阶：
 * 你能尝试使用一趟扫描实现吗？
 * 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
 */
public class Q19 {

    public static void main(String[] args) {
        // 1->2->3->5
        System.out.println(LCUtil.listNodeToString(new Q19().removeNthFromEnd(LCUtil.stringToListNode("[1,2,3,4,5]"), 2)));
    }

    static class LNode {
        ListNode val;
        LNode pre;
        LNode next;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode p = head;
        LNode rHead = new LNode();
        rHead.val = null;
        LNode pR = rHead;
        while (p != null) {
            LNode nNode = new LNode();
            nNode.pre = pR;
            nNode.val = p;
            pR.next = nNode;
            pR = pR.next;
            p = p.next;
        }

        while (--n > 0) {
            pR = pR.pre;
        }
        assert pR.val != null;
        if (pR.pre.val == null) {
            head = pR.val.next;
        } else {
            pR.pre.val.next = pR.val.next;
        }
        return head;
    }
}
