package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

public class Q226 {

    public static void main(String[] args) {
        new Q226().TestOJ();
    }

    public void TestOJ() {
        TreeNode head = LCUtil.stringToTreeNode("[4,2,7,1,3,6,9]"); // [4,7,2,9,6,3,1]
        invertTree(head);
        System.out.println(LCUtil.treeNodeToString(head)); // 6
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
