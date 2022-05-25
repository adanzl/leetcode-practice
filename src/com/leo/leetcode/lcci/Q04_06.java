package com.leo.leetcode.lcci;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
 * 如果指定节点没有对应的“下一个”节点，则返回 null。
 * 链接：https://leetcode.cn/problems/successor-lcci/
 */
public class Q04_06 {

    public static void main(String[] args) {
        TreeNode root;
        // 3
        root = stringToTreeNode("[6,2,8,0,4,7,9,null,null,3,5]");
        assert root != null;
        System.out.println(new Q04_06().inorderSuccessor(root, root.left));
        // 2
        root = stringToTreeNode("[2,1,3]");
        assert root != null;
        System.out.println(new Q04_06().inorderSuccessor(root, root.left));
        // null
        root = stringToTreeNode("[5,3,6,2,4,null,null,1]");
        assert root != null;
        System.out.println(new Q04_06().inorderSuccessor(root, root.right));
    }

    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (root == null) return null;
        if (null != p.right) {
            TreeNode node = p.right;
            while (node.left != null) node = node.left;
            return node;
        }
        TreeNode cur = root, parent, lParent = null;
        while (cur != p) {
            parent = cur;
            if (cur.val > p.val) {
                cur = cur.left;
                lParent = parent;
            } else cur = cur.right;
        }
        return lParent;
    }
}
