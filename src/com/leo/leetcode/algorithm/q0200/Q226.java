package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
 * 提示：
 * 1、树中节点数目范围在 [0, 100] 内
 * 2、-100 <= Node.val <= 100
 * 链接：https://leetcode-cn.com/problems/invert-binary-tree/
 */
public class Q226 {

    public static void main(String[] args) {
        new Q226().TestOJ();
    }

    public void TestOJ() {
        TreeNode head = LCUtil.stringToTreeNode("[4,2,7,1,3,6,9]");
        // [4,7,2,9,6,3,1]
        head = invertTree(head);
        // 6
        System.out.println(LCUtil.treeNodeToString(head));
    }

    public TreeNode invertTree(TreeNode root) {

        if (root == null) return null;
        TreeNode p = root.left;
        root.left = root.right;
        root.right = p;

        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
}
