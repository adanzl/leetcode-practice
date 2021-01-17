package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;

public class Q234 {

    public static void main(String[] args) {
        new Q234().TestOJ();
    }

    public void TestOJ() {
        System.out.println(isPalindrome(LCUtil.stringToListNode("[1]"))); // t
        System.out.println(isPalindrome(LCUtil.stringToListNode("[1,2]"))); // f
        System.out.println(isPalindrome(LCUtil.stringToListNode("[2,2,2,2,2]"))); // t
        System.out.println(isPalindrome(LCUtil.stringToListNode("[2,2,2,2]"))); // t
        System.out.println(isPalindrome(LCUtil.stringToListNode("[1,2,2,1]"))); // t
        System.out.println(isPalindrome(LCUtil.stringToListNode("[1,2,3,2,1]"))); // t
        System.out.println(isPalindrome(LCUtil.stringToListNode("[1,2,3,2,2]"))); // f
    }

    public boolean isPalindrome(ListNode head) {
        if (head == null) return true;
        ListNode left = null, right = head;
        int count = 0;
        while (right != null) {
            count++;
            right = right.next;
        }
        right = head;
        int c = 0, limit = (count + 1) / 2;
        while (right != null) {
            if (c < limit) {
                ListNode n = right.next;
                right.next = left;
                left = right;
                right = n;
            } else {
                if (c == limit && count % 2 == 1) {
                    assert left != null;
                    left = left.next;
                }
                assert left != null;
                if (left.val != right.val) {
                    return false;
                }
                left = left.next;
                right = right.next;
            }
            c++;
        }
        return true;
    }
}
