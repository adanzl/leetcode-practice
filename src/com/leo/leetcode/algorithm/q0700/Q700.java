package com.leo.leetcode.algorithm.q0700;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;
import static com.leo.utils.LCUtil.treeNodeToString;

/**
 * 给定二叉搜索树（BST）的根节点 root 和一个整数值 val。
 * 你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。
 * 提示：
 * 1、数中节点数在 [1, 5000] 范围内
 * 2、1 <= Node.val <= 10^7
 * 3、root 是二叉搜索树
 * 4、1 <= val <= 10^7
 * 链接：https://leetcode-cn.com/problems/search-in-a-binary-search-tree
 */
public class Q700 {

    public static void main(String[] args) {
        // [2,1,3]
        System.out.println(treeNodeToString(new Q700().searchBST(stringToTreeNode("[4,2,7,1,3]"), 2)));
        // []
        System.out.println(treeNodeToString(new Q700().searchBST(stringToTreeNode("[4,2,7,1,3]"), 5)));
    }

    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null) return null;
        if (root.val == val) return root;
        if (root.val < val) return searchBST(root.right, val);
        return searchBST(root.left, val);
    }
}
