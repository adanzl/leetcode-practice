package com.leo.leetcode.algorithm.q0300;

import com.leo.utils.ListNode;

import static com.leo.utils.LCUtil.stringToListNode;
import static com.leo.utils.LCUtil.listNodeToString;

/**
 * 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
 * 请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
 * 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
 * <p>
 * 说明:
 * 1、应当保持奇数节点和偶数节点的相对顺序。
 * 2、链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
 * <p>
 * 链接：https://leetcode-cn.com/problems/odd-even-linked-list
 */
public class Q328 {

    public static void main(String[] args) {
        // 1->3->5->2->4->NULL
        System.out.println(listNodeToString(new Q328().oddEvenList(stringToListNode("[1,2,3,4,5]"))));
        // 2->3->6->7->1->5->4->NULL
        System.out.println(listNodeToString(new Q328().oddEvenList(stringToListNode("[2,1,3,5,6,4,7]"))));
    }

    public ListNode oddEvenList(ListNode head) {
        ListNode p = head, hOdd = new ListNode(-1), hEven = new ListNode(-1);
        ListNode[] arr = new ListNode[]{hOdd, hEven};
        int i = 0;
        while (p != null) {
            arr[i].next = p;
            arr[i] = p;
            p = p.next;
            i = (i + 1) % 2;
        }
        arr[0].next = hEven.next;
        arr[1].next = null;
        return hOdd.next;
    }
}
