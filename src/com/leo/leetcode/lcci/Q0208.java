package com.leo.leetcode.lcci;

import com.leo.utils.ListNode;

import static com.leo.utils.LCUtil.stringToListNode;

/**
 * 给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。若环不存在，请返回 null。
 * 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
 * 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
 * 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
 * 进阶：
 * 你是否可以不用额外空间解决此题？
 * 链接：https://leetcode-cn.com/problems/linked-list-cycle-lcci
 */
public class Q0208 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q0208().detectCycle(stringToListNode("[0,1]"), 0));
        // 6
        System.out.println(new Q0208().detectCycle(stringToListNode("[0,1,2,3,4,5,6,7,8,9]"), 6));
        // 1
        System.out.println(new Q0208().detectCycle(stringToListNode("[0,1,2,3]"), 1));
        // null
        System.out.println(new Q0208().detectCycle(stringToListNode("[0]"), -1));
    }

    public ListNode detectCycle(ListNode head, int pos) {
        if (pos == -1) return detectCycle(head);
        ListNode p = head, tail = head;
        while (pos-- > 0) p = p.next;
        while (tail.next != null) tail = tail.next;
        tail.next = p;
        return detectCycle(head);
    }

    public ListNode detectCycle(ListNode head) {
        ListNode p1 = head, p2 = head;
        while (p1 != null) {
            p1 = p1.next;
            if (p1 == null) break;
            p1 = p1.next;
            p2 = p2.next;
            if (p1 == p2) break;
        }
        if (p1 == null) return null;
        p2 = head;
        while (p1 != p2) {
            p1 = p1.next;
            p2 = p2.next;
        }
        return p1;
    }
}
