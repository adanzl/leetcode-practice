package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
 * 说明: 叶子节点是指没有子节点的节点。
 * 链接：https://leetcode-cn.com/problems/path-sum/
 */
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
