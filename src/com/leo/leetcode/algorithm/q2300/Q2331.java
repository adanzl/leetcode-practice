package com.leo.leetcode.algorithm.q2300;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给你一棵 完整二叉树 的根，这棵树有以下特征：
 * 1、叶子节点 要么值为 0 要么值为 1 ，其中 0 表示 False ，1 表示 True 。
 * 2、非叶子节点 要么值为 2 要么值为 3 ，其中 2 表示逻辑或 OR ，3 表示逻辑与 AND 。
 * 计算 一个节点的值方式如下：
 * 1、如果节点是个叶子节点，那么节点的 值 为它本身，即 True 或者 False 。
 * 2、否则，计算 两个孩子的节点值，然后将该节点的运算符对两个孩子值进行 运算 。
 * 返回根节点 root 的布尔运算值。
 * 完整二叉树 是每个节点有 0 个或者 2 个孩子的二叉树。
 * 叶子节点 是没有孩子的节点。
 * 提示：
 * 1、树中节点数目在 [1, 1000] 之间。
 * 2、0 <= Node.val <= 3
 * 3、每个节点的孩子数为 0 或 2 。
 * 4、叶子节点的值为 0 或 1 。
 * 5、非叶子节点的值为 2 或 3 。
 * 链接：https://leetcode.cn/problems/evaluate-boolean-binary-tree
 */
public class Q2331 {
    public static void main(String[] args) {
        // true
        System.out.println(new Q2331().evaluateTree(stringToTreeNode("[2,1,3,null,null,0,1]")));
        // false
        System.out.println(new Q2331().evaluateTree(stringToTreeNode("[0]")));
    }

    public boolean evaluateTree(TreeNode root) {
        if (root == null) return false;
        if (root.left == null && root.right == null) return root.val == 1;
        if (root.val == 2) return evaluateTree(root.left) || evaluateTree(root.right);
        else return evaluateTree(root.left) && evaluateTree(root.right);
    }

}
