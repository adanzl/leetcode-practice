package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 给定一个二叉树，原地将它展开为一个单链表。
 * 链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
 */
public class Q114 {

    public static void main(String[] args) {
        new Q114().TestOJ();
    }

    public void TestOJ() {
        // [1, null, 2, null, 3, null, 4, null, 5, null, 6, null, null]
        TreeNode p = LCUtil.stringToTreeNode("[1,2,5,3,4,null,6]");
        flatten(p);
        System.out.println(LCUtil.treeNodeToString(p));
        p = LCUtil.stringToTreeNode("[1]");
        flatten(p);
        System.out.println(LCUtil.treeNodeToString(p));
    }

    public void flatten(TreeNode root) {
        if (root == null) return;
        TreeNode l = root.left;
        TreeNode r = root.right;
        root.left = null;
        root.right = l;
        flatten(l);
        TreeNode last = root;
        while (last.right != null) {
            last = last.right;
        }
        last.right = r;
        flatten(r);
    }
}
