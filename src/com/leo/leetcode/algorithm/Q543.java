package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

public class Q543 {
    public void TestOJ() {
        System.out.println(diameterOfBinaryTree(LCUtil.stringToTreeNode("[1,2,3,4,5]"))); // 3
    }

    private int max;

    public int diameterOfBinaryTree(TreeNode root) {
        this.max = 0;
        dp(root, 0);
        return max;
    }

    int dp(TreeNode root, int deep) {
        if (root == null) return deep;
        int l = dp(root.left, deep);
        int r = dp(root.right, deep);
        this.max = Math.max(this.max, l + r);
        return Math.max(l, r) + 1;
    }
}
