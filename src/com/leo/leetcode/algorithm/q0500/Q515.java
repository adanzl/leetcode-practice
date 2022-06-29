package com.leo.leetcode.algorithm.q0500;

import com.leo.utils.TreeNode;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。
 * 提示：
 * 1、二叉树的节点个数的范围是 [0,10^4]
 * 2、-2^31 <= Node.val <= 2^31 - 1
 * 链接：https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
 */
public class Q515 {

    public static void main(String[] args) {
        // [1,3,9]
        System.out.println(new Q515().largestValues(stringToTreeNode("[1,3,2,5,3,null,9]")));
        // [1,3]
        System.out.println(new Q515().largestValues(stringToTreeNode("[1,2,3]")));
    }

    public List<Integer> largestValues(TreeNode root) {
        List<Integer> ret = new ArrayList<>();
        func(root, ret, 0);
        return ret;
    }

    void func(TreeNode root, List<Integer> ret, int deep) {
        if (root == null) return;
        if (deep >= ret.size()) ret.add(Integer.MIN_VALUE);
        ret.set(deep, Math.max(ret.get(deep), root.val));
        func(root.right, ret, deep + 1);
        func(root.left, ret, deep + 1);
    }
}
