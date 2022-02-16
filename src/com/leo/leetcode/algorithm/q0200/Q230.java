package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

import java.util.Stack;

/**
 * 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
 * 说明：
 * 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
 * 链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
 */
public class Q230 {

    public static void main(String[] args) {
        System.out.println(new Q230().kthSmallest(LCUtil.stringToTreeNode("[3,1,4,null,2]"), 1)); // 1
        System.out.println(new Q230().kthSmallest(LCUtil.stringToTreeNode("[5,3,6,2,4,null,null,1]"), 3)); // 3
    }

    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> s = new Stack<>();
        TreeNode p = root;
        int count = 0;
        while (!s.empty() || p != null) {
            if (p != null) {
                s.push(p);
                p = p.left;
            } else {
                p = s.pop();
                count++;
                if (count == k) {
                    return p.val;
                }
                p = p.right;
            }
        }
        return -1;
    }
}
