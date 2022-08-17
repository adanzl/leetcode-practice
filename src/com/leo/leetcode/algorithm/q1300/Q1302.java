package com.leo.leetcode.algorithm.q1300;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。
 * 提示：
 * 1、树中节点数目在范围 [1, 10^4] 之间。
 * 2、1 <= Node.val <= 100
 * 链接：https://leetcode.cn/problems/deepest-leaves-sum/
 */
public class Q1302 {

    public static void main(String[] args) {
        // 15
        System.out.println(new Q1302().deepestLeavesSum(stringToTreeNode("[1,2,3,4,5,null,6,7,null,null,null,null,8]")));
        // 19
        System.out.println(new Q1302().deepestLeavesSum(stringToTreeNode("[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]")));
    }

    int maxDepth = 0;
    int sum = 0;

    public int deepestLeavesSum(TreeNode root) {
        dfs(root, 0);
        return sum;
    }

    void dfs(TreeNode root, int depth) {
        if (root == null) return;
        if (depth > this.maxDepth) {
            sum = root.val;
            this.maxDepth = depth;
        } else if (depth == this.maxDepth) {
            sum += root.val;
        }
        dfs(root.left, depth + 1);
        dfs(root.right, depth + 1);
    }
}
