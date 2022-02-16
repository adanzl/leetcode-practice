package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;

/**
 * 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
 * 提示：
 * 1、链表中节点数目在范围[1, 105] 内
 * 2、0 <= Node.val <= 9
 * 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
 * 链接：https://leetcode-cn.com/problems/palindrome-linked-list
 */
public class Q234 {

    public static void main(String[] args) {
        new Q234().TestOJ();
    }

    public void TestOJ() {
        // t
        System.out.println(isPalindrome(LCUtil.stringToListNode("[1]")));
        // f
        System.out.println(isPalindrome(LCUtil.stringToListNode("[1,2]")));
        // t
        System.out.println(isPalindrome(LCUtil.stringToListNode("[2,2,2,2,2]")));
        // t
        System.out.println(isPalindrome(LCUtil.stringToListNode("[2,2,2,2]")));
        // t
        System.out.println(isPalindrome(LCUtil.stringToListNode("[1,2,2,1]")));
        // t
        System.out.println(isPalindrome(LCUtil.stringToListNode("[1,2,3,2,1]")));
        // f
        System.out.println(isPalindrome(LCUtil.stringToListNode("[1,2,3,2,2]")));
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
