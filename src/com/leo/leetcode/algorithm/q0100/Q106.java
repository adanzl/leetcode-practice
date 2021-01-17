package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 根据一棵树的中序遍历与后序遍历构造二叉树。
 * 注意:
 * 你可以假设树中没有重复的元素。
 * 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
 */
public class Q106 {

    public static void main(String[] args) {
        // [3,9,20,null,null,15,7]
        System.out.println(LCUtil.treeNodeToString(new Q106().buildTree(new int[]{9, 3, 15, 20, 7}, new int[]{9, 15, 7, 20, 3})));
    }

    public TreeNode buildTree(int[] inOrder, int[] postOrder) {
        return build(inOrder, 0, inOrder.length, postOrder, 0, postOrder.length);
    }

    TreeNode build(int[] inOrder, int il, int ir, int[] postOrder, int pl, int pr) {
        if (pl == pr) return null;
        int rootValue = postOrder[pr - 1];
        TreeNode node = new TreeNode(rootValue);
        for (int i = il; i < ir; i++) {
            if (inOrder[i] == rootValue) {
                node.left = build(inOrder, il, i, postOrder, pl, i - il + pl);
                node.right = build(inOrder, i + 1, ir, postOrder, i - il + pl, pr - 1);
                break;
            }
        }
        return node;
    }
}
