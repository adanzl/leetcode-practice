package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

public class Q114 {
    public static void main(String[] args) {
        new Q114().TestOJ();
    }

    public void TestOJ() {
//        TreeNode p = LCUtil.stringToTreeNode("[1,2,5,3,4,null,6]");
        TreeNode p = LCUtil.stringToTreeNode("[1]");
        flatten(p);
        System.out.println(LCUtil.treeNodeToString(p));
    }

    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }
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
