package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Q148 {
    @Test
    public void TestOJ() {
        System.out.println(sortList1(LCUtil.stringToListNode("[4,2,1,3]"))); //
        System.out.println(sortList1(LCUtil.stringToListNode("[-1,5,3,4,0]"))); //
    }

    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        // 没有条件，创造条件。自己添加头节点，最后返回时去掉即可。
        ListNode newHead = new ListNode(-1);
        newHead.next = head;
        return quickSort(newHead, null);
    }

    // 小机灵鬼
    public ListNode sortList1(ListNode head) {
        if (head == null) return null;
        ListNode curr = head;
        List<Integer> l = new ArrayList<>();
        while (curr != null) {
            l.add(curr.val);
            curr = curr.next;
        }
        Integer[] arr = l.toArray(new Integer[0]);
        Arrays.sort(arr);
        curr = head;
        for (Integer integer : arr) {
            curr.val = integer;
            curr = curr.next;
        }
        return head;
    }

    // 带头结点的链表快速排序
    private ListNode quickSort(ListNode head, ListNode end) {
        if (head == end || head.next == end || head.next.next == end) return head;
        // 将小于划分点的值存储在临时链表中
        ListNode tmpHead = new ListNode(-1);
        // partition为划分点，p为链表指针，tp为临时链表指针
        ListNode partition = head.next, p = partition, tp = tmpHead;
        // 将小于划分点的结点放到临时链表中
        while (p.next != end) {
            if (p.next.val < partition.val) {
                tp.next = p.next;
                tp = tp.next;
                p.next = p.next.next;
            } else {
                p = p.next;
            }
        }
        // 合并临时链表和原链表，将原链表接到临时链表后面即可
        tp.next = head.next;
        // 将临时链表插回原链表，注意是插回！（不做这一步在对右半部分处理时就断链了）
        head.next = tmpHead.next;
        quickSort(head, partition);
        quickSort(partition, end);
        // 题目要求不带头节点，返回结果时去除
        return head.next;
    }
}
