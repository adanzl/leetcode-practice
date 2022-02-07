package com.leo.leetcode.algorithm.q0300;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;

/**
 * 给你一个单链表，随机选择链表的一个节点，并返回相应的节点值。每个节点 被选中的概率一样 。
 * 实现 Solution 类：
 * Solution(ListNode head) 使用整数数组初始化对象。
 * int getRandom() 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。
 * 提示：
 * 1、链表中的节点数在范围 [1, 10^4] 内
 * 2、-10^4 <= Node.val <= 10^4
 * 3、至多调用 getRandom 方法 10^4 次
 * 进阶：
 * 1、如果链表非常大且长度未知，该怎么处理？
 * 2、你能否在不使用额外空间的情况下解决此问题？
 * <p>
 * 链接：https://leetcode-cn.com/problems/linked-list-random-node
 */
public class Q382 {
    public static void main(String[] args) {
        Solution solution = new Solution(LCUtil.stringToListNode("[1, 2, 3]"));
        System.out.println(solution.getRandom());
        System.out.println(solution.getRandom());
        System.out.println(solution.getRandom());
        System.out.println(solution.getRandom());
        System.out.println(solution.getRandom());
    }

    static class Solution {
        private final ListNode head;

        public Solution(ListNode head) {
            this.head = head;
        }

        public int getRandom() {
            ListNode p = head;
            int value = 0, i = 1;
            while (p != null) {
                if (Math.random() * i < 1) {
                    value = p.val;
                }
                p = p.next;
                i++;
            }
            return value;
        }
    }
}
