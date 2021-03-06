package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.TreeNode;

import java.util.Objects;
import java.util.Stack;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
 * 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
 * <p>
 * 说明:
 * 1、所有节点的值都是唯一的。
 * 2、p、q 为不同节点且均存在于给定的二叉树中。
 * <p>
 * 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
 */
public class Q236 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q236().lowestCommonAncestor(
                stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]"),
                stringToTreeNode("[5]"),
                stringToTreeNode("[1]")));
        // 5
        System.out.println(new Q236().lowestCommonAncestor1(
                stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]"),
                Objects.requireNonNull(stringToTreeNode("[5]")),
                Objects.requireNonNull(stringToTreeNode("[4]"))));
    }

    public TreeNode lowestCommonAncestor1(TreeNode root, TreeNode p, TreeNode q) {
        Stack<TreeNode> s1 = new Stack<>(), s2 = new Stack<>();
        postOrder(root, s1, p.val);
        postOrder(root, s2, q.val);
        for (int i = 1; i < s1.size() || i < s2.size(); i++) {
            if (i >= s1.size() || i >= s2.size() || s1.elementAt(i) != s2.elementAt(i)) {
                return s1.elementAt(i - 1);
            }
        }
        return root;
    }

    //
    boolean postOrder(TreeNode root, Stack<TreeNode> s, int v) {
        if (root == null) return false;
        s.push(root);
        if (root.val == v) return true;
        if (postOrder(root.left, s, v)) return true;
        if (postOrder(root.right, s, v)) return true;
        s.pop();
        return false;
    }

    // !!!!!!!!!!!!!!!!!!!!!!!!!!所有节点的值都是唯一的!!!!!!!!!!!!!!!!!!!!!!!!!!
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root;
        return left != null ? left : right;
    }
}
