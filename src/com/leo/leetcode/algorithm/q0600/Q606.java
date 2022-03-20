package com.leo.leetcode.algorithm.q0600;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
 * 空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
 * 链接：https://leetcode-cn.com/problems/construct-string-from-binary-tree
 */
public class Q606 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q606().tree2str(stringToTreeNode("[1]")));
        // 1(2(4))(3)
        System.out.println(new Q606().tree2str(stringToTreeNode("[1,2,3,4]")));
        // 1(2()(4))(3)
        System.out.println(new Q606().tree2str(stringToTreeNode("[1,2,3,null,4]")));
        // 1(2)(3(4))
        System.out.println(new Q606().tree2str(stringToTreeNode("[1,2,3,null,null,4]")));
    }

    public String tree2str(TreeNode root) {
        StringBuilder ret = new StringBuilder();
        visit(root, ret);
        return ret.toString();
    }

    int visit(TreeNode root, StringBuilder out) {
        if (root == null) return 0;
        out.append(root.val).append("(");
        int left = visit(root.left, out);
        if (left != 0 || root.right != null) out.append(")");
        else out.deleteCharAt(out.length() - 1);
        out.append("(");
        int right = visit(root.right, out);
        if (right != 0) out.append(")");
        else out.deleteCharAt(out.length() - 1);
        return 1 + left + right;
    }
}
