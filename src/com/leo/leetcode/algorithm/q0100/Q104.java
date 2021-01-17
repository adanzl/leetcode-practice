package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 给定一个二叉树，找出其最大深度。
 * 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
 * 说明: 叶子节点是指没有子节点的节点。
 * 链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
 */
public class Q104 {

    public static void main(String[] args) {
        new Q104().TestOJ();
    }

    public void TestOJ() {
        System.out.println(maxDepth(LCUtil.stringToTreeNode("[3,9,20,null,null,15,7]"))); // 3
    }

    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
