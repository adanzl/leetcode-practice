package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

public class Q112 {
    public static void main(String[] args) {
        new Q112().TestOJ();
    }

    public void TestOJ() {
        System.out.println(hasPathSum(LCUtil.stringToTreeNode("[-2,null,-3]"), -5)); // true
    }

    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) return false;
        if (sum == root.val && root.left == null && root.right == null) return true;
        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }
}
