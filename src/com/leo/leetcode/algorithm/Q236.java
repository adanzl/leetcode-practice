package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

import java.util.Objects;
import java.util.Stack;

/**
 * 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
 * <p>
 * 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
 * <p>
 * 说明:
 * <p>
 * 所有节点的值都是唯一的。
 * p、q 为不同节点且均存在于给定的二叉树中。
 * <p>
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
public class Q236 {
    public void TestOJ() {
        System.out.println(lowestCommonAncestor(
                LCUtil.stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]"),
                Objects.requireNonNull(LCUtil.stringToTreeNode("[5]")),
                Objects.requireNonNull(LCUtil.stringToTreeNode("[1]")))); // 3
        System.out.println(lowestCommonAncestor1(
                LCUtil.stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]"),
                Objects.requireNonNull(LCUtil.stringToTreeNode("[5]")),
                Objects.requireNonNull(LCUtil.stringToTreeNode("[4]")))); // 5
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
