package com.leo.leetcode.algorithm;

import java.util.*;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 给定一个二叉树，返回它的 后序 遍历。 递归算法很简单，你可以通过迭代算法完成吗？
 * https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
 **/
public class Q145 {
    public static void main(String[] args) {
        System.out.println(new Q145().postOrderTraversalNoRecur(LCUtil.stringToTreeNode("[1,null,2,3]"))); // [3,2,1]
        System.out.println(new Q145().postOrderTraversalNoRecur(LCUtil.stringToTreeNode("[]"))); // []
        System.out.println(new Q145().postOrderTraversal(LCUtil.stringToTreeNode("[1,null,2,3]"))); // [3,2,1]
    }

    public List<Integer> postOrderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        recur(root, out);
        return out;
    }

    void recur(TreeNode root, List<Integer> out) {
        if (root == null)
            return;
        recur(root.left, out);
        recur(root.right, out);
        out.add(root.val);
    }

    /**
     * 需要判断上次访问的节点是位于左子树，还是右子树。若是位于左子树，则需跳过根节点，先进入右子树，再回头访问根节点；若是位于右子树，则直接访问根节点。
     */
    public List<Integer> postOrderTraversalNoRecur(TreeNode root) {
        Stack<TreeNode> s = new Stack<>();
        LinkedList<Integer> out = new LinkedList<>();
        if (root != null) s.push(root);
        while (!s.empty()) {
            TreeNode p = s.pop();
            out.addFirst(p.val);
            if (p.left != null) s.push(p.left);
            if (p.right != null) s.push(p.right);
        }
        return out;
    }
}
