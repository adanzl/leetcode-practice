package com.leo.leetcode.lcci;

import com.leo.utils.ListNode;

import java.util.HashSet;
import java.util.Set;

import static com.leo.utils.LCUtil.listNodeToString;
import static com.leo.utils.LCUtil.stringToListNode;

/**
 * 编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
 * 链接：https://leetcode-cn.com/problems/remove-duplicate-node-lcci/
 */
public class Q02_01 {
    public static void main(String[] args) {
        System.out.println(listNodeToString(new Q02_01().removeDuplicateNodes(stringToListNode("[1,2,3,3,2,1]")))); // [1,2,3]
        System.out.println(listNodeToString(new Q02_01().removeDuplicateNodes(stringToListNode("[1,1,1,1,1,2]")))); // [1,2]
    }

    public ListNode removeDuplicateNodes(ListNode head) {
        ListNode ret = new ListNode(0), p = ret;
        Set<Integer> s = new HashSet<>();
        while (head != null) {
            if (!s.contains(head.val)) {
                p.next = head;
                s.add(head.val);
                p = p.next;
            }
            head = head.next;
        }
        p.next = null;
        return ret.next;
    }
}
