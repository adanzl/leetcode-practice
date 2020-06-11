package com.leo.leetcode.lcof;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;

import java.util.Arrays;

public class Q06 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Q06().reversePrint(LCUtil.stringToListNode("[1,3,2]")))); // [2,3,1]
    }

    public int[] reversePrint(ListNode head) {
        int count = 0;
        ListNode p = head, pre = null;
        while (p != null) {
            count++;
            ListNode n = p;
            p = p.next;
            n.next = pre;
            pre = n;
        }
        int[] out = new int[count];
        p = pre;
        while (count > 0 && p != null) {
            out[out.length - count--] = p.val;
            p = p.next;
        }
        return out;
    }
}
