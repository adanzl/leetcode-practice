package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

public class Q111 {

    public static void main(String[] args) {
        new Q111().TestOJ();
    }

    public void TestOJ() {
        System.out.println(minDepth(LCUtil.stringToTreeNode("[1,2]"))); // 2
        System.out.println(minDepth(LCUtil.stringToTreeNode("[]"))); // 0
    }

    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        return fun(root, 1);
    }

    private int fun(TreeNode p, int deep) {
        if (p == null) return Integer.MAX_VALUE;
        if (p.left == null && p.right == null) return deep;
        return Math.min(fun(p.left, deep + 1), fun(p.right, deep + 1));
    }
}