package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
 * 完全二叉树 的定义如下：
 * 在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。
 * 若最底层为第 h 层，则该层包含 1~ 2^h 个节点。
 * 提示：
 * 1、树中节点的数目范围是[0, 5 * 10^4]
 * 2、0 <= Node.val <= 5 * 10^4
 * 3、题目数据保证输入的树是 完全二叉树
 * 进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
 * 链接：https://leetcode-cn.com/problems/count-complete-tree-nodes
 */
public class Q222 {

    public static void main(String[] args) {
        // 6
        System.out.println(new Q222().countNodes(stringToTreeNode("[1,2,3,4,5,6]")));
        // 0
        System.out.println(new Q222().countNodes(stringToTreeNode("[]")));
        // 1
        System.out.println(new Q222().countNodes(stringToTreeNode("[1]")));
    }

    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        int depth_l = 0, depth_r = 0;
        TreeNode p = root;
        while (p != null) {
            depth_l++;
            p = p.left;
        }
        p = root;
        while (p != null) {
            depth_r++;
            p = p.right;
        }
        if (depth_l == depth_r) return (1 << depth_l) - 1;
        return 1 + countNodes(root.left) + countNodes(root.right);
    }
}
