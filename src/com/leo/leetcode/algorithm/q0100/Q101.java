package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

public class Q101 {
    public void TestOJ() {
        System.out.println(isSymmetric(LCUtil.stringToTreeNode("[1,2,2,3,4,4,3]"))); // t
        System.out.println(isSymmetric(LCUtil.stringToTreeNode("[1,2,2,null,3,null,3]"))); // f
        System.out.println(isSymmetric(LCUtil.stringToTreeNode("[1]"))); // t
        System.out.println(isSymmetric(LCUtil.stringToTreeNode("[]"))); // t
        System.out.println(isSymmetric(LCUtil.stringToTreeNode("[1,2,2,2,null,2]"))); // f
    }

    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return isMirror(root.left, root.right);
    }

    private boolean isMirror(TreeNode l, TreeNode r) {
        if (l == null && r == null) return true;
        if (l == null || r == null) return false;
        return l.val == r.val && isMirror(l.left, r.right) && isMirror(l.right, r.left);
    }
}
