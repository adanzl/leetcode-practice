package com.leo.leetcode.algorithm.q0500;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.treeNodeToString;

/**
 * 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
 * 使每个节点 node的新值等于原树中大于或等于 node.val 的值之和。
 * 提醒一下，二叉搜索树满足下列约束条件：
 * 1、节点的左子树仅包含键 小于 节点键的节点。
 * 2、节点的右子树仅包含键 大于 节点键的节点。
 * 3、左右子树也必须是二叉搜索树。
 * 注意：本题和 1038:https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同
 * 提示：
 * 1、树中的节点数介于 0 和 104 之间。
 * 2、每个节点的值介于 -104 和 104 之间。
 * 3、树中的所有值 互不相同 。
 * 4、给定的树为二叉搜索树。
 * <p>
 * 链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
 */
public class Q538 {
    public static void main(String[] args) {
        // [8,8,4,6,null,7]
        System.out.println(treeNodeToString(new Q538().convertBST(LCUtil.stringToTreeNode("[1,0,4,-2,null,3]"))));
        // [5, 6, 3, 2, 6]
        System.out.println(treeNodeToString(new Q538().convertBST(LCUtil.stringToTreeNode("[2,0,3,-4,1]"))));
        // [18, 20, 13]
        System.out.println(treeNodeToString(new Q538().convertBST(LCUtil.stringToTreeNode("[5,2,13]"))));
    }

    public TreeNode convertBST(TreeNode root) {
        dp(root, 0);
        return root;
    }

    int dp(TreeNode root, int v) {
        if (root == null) return 0;
        if (root.right != null) root.val += dp(root.right, v);
        else root.val += v;
        if (root.left != null) return dp(root.left, root.val);
        else return root.val;
    }
}
