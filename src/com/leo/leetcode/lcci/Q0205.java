package com.leo.leetcode.lcci;

import com.leo.utils.ListNode;

import static com.leo.utils.LCUtil.stringToListNode;
import static com.leo.utils.LCUtil.listNodeToString;

/**
 * 给定两个用链表表示的整数，每个节点包含一个数位。
 * 这些数位是反向存放的，也就是个位排在链表首部。
 * 编写函数对这两个整数求和，并用链表形式返回结果。
 * 链接：https://leetcode-cn.com/problems/sum-lists-lcci/
 */
public class Q0205 {
    public static void main(String[] args) {
        // [0,0,0]
        System.out.println(listNodeToString(new Q0205().addTwoNumbers(stringToListNode("[0,0,0]"), stringToListNode("[0,0,0]"))));
        // [7,0,8]
        System.out.println(listNodeToString(new Q0205().addTwoNumbers(stringToListNode("[2,4,3]"), stringToListNode("[5,6,4]"))));
        // [2,1,9]
        System.out.println(listNodeToString(new Q0205().addTwoNumbers(stringToListNode("[7,1,6]"), stringToListNode("[5,9,2]"))));
        // [8,0,3,1]
        System.out.println(listNodeToString(new Q0205().addTwoNumbers(stringToListNode("[6,1,7]"), stringToListNode("[2,9,5]"))));
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ret = new ListNode(0), p = ret;
        while (true) {
            int v = p.val + (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val);
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
            p.val = v % 10;
            if (l1 == null && l2 == null && v / 10 == 0) break;
            p.next = new ListNode(v / 10);
            p = p.next;
        }
        return ret;
    }
}
