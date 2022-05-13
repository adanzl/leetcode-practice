package com.leo.leetcode.lcci;

import com.leo.utils.ListNode;

import static com.leo.utils.LCUtil.stringToListNode;
import static com.leo.utils.LCUtil.listNodeToString;

/**
 * 编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。
 * 如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。
 * 链接：https://leetcode-cn.com/problems/partition-list-lcci
 */
public class Q0204 {

    public static void main(String[] args) {
        // [2,2,1,5,3,4]
        System.out.println(listNodeToString(new Q0204().partition(stringToListNode("[1,4,3,2,5,2]"), 3)));
        // [3,1,2,10,5,5,8]
        System.out.println(listNodeToString(new Q0204().partition(stringToListNode("[3,5,8,5,10,2,1]"), 5)));
    }

    public ListNode partition(ListNode head, int x) {
        ListNode mid = new ListNode(x), m = mid, p = head, out = new ListNode(0), o = out;
        while (p != null) {
            if (p.val >= x) {
                m.next = p;
                m = p;
            } else {
                o.next = p;
                o = p;
            }
            p = p.next;
        }
        o.next = mid.next;
        m.next = null;
        return out.next;
    }
}
