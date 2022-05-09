package com.leo.leetcode.algorithm.q2200;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给你一棵二叉树的根节点 root ，找出并返回满足要求的节点数，要求节点的值等于其 子树 中值的 平均值 。
 * 注意：
 * 1、n 个元素的平均值可以由 n 个元素 求和 然后再除以 n ，并 向下舍入 到最近的整数。
 * 2、root 的 子树 由 root 和它的所有后代组成。
 * 提示：
 * 1、树中节点数目在范围 [1, 1000] 内
 * 2、0 <= Node.val <= 1000
 * 链接：https://leetcode-cn.com/problems/count-nodes-equal-to-average-of-subtree
 */
public class Q2265 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q2265().averageOfSubtree(stringToTreeNode("[4,8,5,0,1,null,6]")));
        // 1
        System.out.println(new Q2265().averageOfSubtree(stringToTreeNode("[1]")));
    }

    int ret = 0;

    public int averageOfSubtree(TreeNode root) {
        dfs(root);
        return ret;
    }

    int[] dfs(TreeNode root) {
        if (root == null) return new int[]{0, 0}; // sum, count
        int[] left = dfs(root.left);
        int[] right = dfs(root.right);
        int sum = left[0] + right[0] + root.val, count = left[1] + right[1] + 1;
        int v = sum / count;
        if (v == root.val) ret++;
        return new int[]{sum, count};
    }
}
