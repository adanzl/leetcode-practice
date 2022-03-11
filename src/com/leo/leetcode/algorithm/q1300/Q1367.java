package com.leo.leetcode.algorithm.q1300;

import com.leo.utils.ListNode;
import com.leo.utils.TestCase;
import com.leo.utils.TreeNode;


import static com.leo.utils.LCUtil.stringToListNode;
import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。
 * 如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 。
 * 一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。
 * 提示：
 * 1、二叉树和链表中的每个节点的值都满足 1 <= node.val <= 100 。
 * 2、链表包含的节点数目在 1 到 100 之间。
 * 3、二叉树包含的节点数目在 1 到 2500 之间。
 * 链接：https://leetcode-cn.com/problems/linked-list-in-binary-tree
 */
public class Q1367 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q1367().isSubPath(stringToListNode("[4,2,8]"), stringToTreeNode("[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]")));
        // false
        TestCase tc = new TestCase("resources/Q1367/Case001.txt");
        System.out.println(new Q1367().isSubPath(stringToListNode(tc.getData(0)), stringToTreeNode(tc.getData(1))));
        // true
        System.out.println(new Q1367().isSubPath(stringToListNode("[2,2,1]"), stringToTreeNode("[2,null,2,null,2,null,1]")));
        // true
        System.out.println(new Q1367().isSubPath(stringToListNode("[1,10]"), stringToTreeNode("[1,null,1,10,1,9]")));
        // true
        System.out.println(new Q1367().isSubPath(stringToListNode("[1,4,2,6]"), stringToTreeNode("[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]")));
        // false
        System.out.println(new Q1367().isSubPath(stringToListNode("[1,4,2,6,8]"), stringToTreeNode("[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]")));
    }

    public boolean isSubPath(ListNode head, TreeNode root) {
        if (root == null) return false;
        return isSub(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right);
    }

    boolean isSub(ListNode node, TreeNode root) {
        if (node == null) return true;
        if (root == null) return false;
        if (node.val != root.val) return false;
        return isSub(node.next, root.left) || isSub(node.next, root.right);
    }
}
