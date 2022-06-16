package com.leo.leetcode.algorithm.q6000;

import com.leo.utils.ListNode;

import static com.leo.utils.LCUtil.stringToListNode;

/**
 * 给你一个链表的头节点 head ，该链表包含由 0 分隔开的一连串整数。链表的 开端 和 末尾 的节点都满足 Node.val == 0 。
 * 对于每两个相邻的 0 ，请你将它们之间的所有节点合并成一个节点，其值是所有已合并节点的值之和。然后将所有 0 移除，修改后的链表不应该含有任何 0 。
 * 返回修改后链表的头节点 head 。
 * 提示：
 * 1、列表中的节点数目在范围 [3, 2 * 10^5] 内
 * 2、0 <= Node.val <= 1000
 * 3、不 存在连续两个 Node.val == 0 的节点
 * 4、链表的 开端 和 末尾 节点都满足 Node.val == 0
 * 链接：https://leetcode.cn/problems/merge-nodes-in-between-zeros
 */
public class Q2181 {

    public static void main(String[] args) {
        // [4,11]
        System.out.println(new Q2181().mergeNodes(stringToListNode("[0,3,1,0,4,5,2,0]")));
        // [1,3,4]
        System.out.println(new Q2181().mergeNodes(stringToListNode("[0,1,0,3,0,2,2,0]")));
    }

    public ListNode mergeNodes(ListNode head) {
        ListNode h = new ListNode(-1), p = head, cur = new ListNode(0), pre = cur;
        h.next = cur;
        while (p != null) {
            if (p.val == 0) {
                cur.next = new ListNode(0);
                pre = cur;
                cur = cur.next;
            } else {
                cur.val += p.val;
            }
            p = p.next;
        }
        pre.next = null;
        return h.next.next;
    }
}
