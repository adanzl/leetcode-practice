package com.leo.leetcode.contest.q20220313;

import com.leo.utils.ListNode;

import static com.leo.utils.LCUtil.stringToListNode;

/**
 * 给定一个链表的头结点 head，判断链表删除一个节点后是否可以成为「回文链表」。
 * 若可以，则返回 true；否则返回 false
 * 注意：输入用例均保证链表长度 大于等于 3
 * 链接：https://leetcode.cn/contest/cnunionpay-2022spring/problems/D7rekZ/
 */
public class Q1 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q1().isPalindrome(stringToListNode("[5,1,8,8,1,5]")));
        // true
        System.out.println(new Q1().isPalindrome(stringToListNode("[4,8,6,6,6,8,4,8]")));
        // false
        System.out.println(new Q1().isPalindrome(stringToListNode("[7,7,1,5,5,1,7,3]")));
        // true
        System.out.println(new Q1().isPalindrome(stringToListNode("[4,8,6,6,8,4,8]")));
        // true
        System.out.println(new Q1().isPalindrome(stringToListNode("[1,2,2,3,1]")));
        // false
        System.out.println(new Q1().isPalindrome(stringToListNode("[1,2,3,4]")));
    }

    public boolean isPalindrome(ListNode head) {
        int[] data = new int[100_000];
        int r = 0, l = 0;
        ListNode p = head;
        while (p != null) {
            data[r++] = p.val;
            p = p.next;
        }
        return isPalindrome(data, l, r - 1, 0);
    }

    boolean isPalindrome(int[] data, int l, int r, int fit) {
        while (r > l) {
            if (data[l] != data[r]) {
                if (fit == 1)
                    return false;
                return isPalindrome(data, l + 1, r, 1) || isPalindrome(data, l, r - 1, 1);
            }
            l++;
            r--;
        }
        return true;
    }
}
