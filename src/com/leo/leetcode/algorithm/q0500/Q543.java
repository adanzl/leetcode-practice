package com.leo.leetcode.algorithm.q0500;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
 * 注意：两结点之间的路径长度是以它们之间边的数目表示。
 *
 * 链接：https://leetcode-cn.com/problems/diameter-of-binary-tree/
 */
public class Q543 {
    public static void main(String[] args) {
        // 3
        System.out.println(new Q543().diameterOfBinaryTree(stringToTreeNode("[1,2,3,4,5]")));
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
