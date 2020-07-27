package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;
import com.leo.utils.TreeNode;

/**
 * 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
 * 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
 * 注：利用中序遍历展开的生成顺序性质
 * 链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
 */
public class Q109 {

    public static void main(String[] args) {
        // [0,-3,9,-10,null,5]
        System.out.println(LCUtil.treeNodeToString(new Q109().sortedListToBST(LCUtil.stringToListNode("[-10,-3,0,5,9]"))));
    }

    ListNode pNode;

    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
        ListNode p = head;
        int count = 0;
        while (p != null) {
            count++;
            p = p.next;
        }
        this.pNode = head;
        return buildTree(0, count);
    }

    TreeNode buildTree(int l, int r) {
        if (l == r) return null;
        int mid = (l + r) >> 1;
        TreeNode root = new TreeNode(0);
        root.left = buildTree(l, mid);
        root.val = this.pNode.val;
        this.pNode = this.pNode.next;
        root.right = buildTree(mid + 1, r);
        return root;
    }
}
