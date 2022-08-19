package com.leo.leetcode.algorithm.q0600;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.*;

/**
 * 给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:
 * 1、创建一个根节点，其值为 nums 中的最大值。
 * 2、递归地在最大值 左边 的 子数组前缀上 构建左子树。
 * 3、递归地在最大值 右边 的 子数组后缀上 构建右子树。
 * 返回 nums 构建的 最大二叉树 。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、0 <= nums[i] <= 1000
 * 3、nums 中的所有整数 互不相同
 * 链接：https://leetcode.cn/problems/maximum-binary-tree
 */
public class Q645 {

    public static void main(String[] args) {
        // [6,3,5,null,2,0,null,null,1]
        System.out.println(treeNodeToString(new Q645().constructMaximumBinaryTree(stringToIntegerArray("[3,2,1,6,0,5]"))));
        // [3,null,2,null,1]
        System.out.println(treeNodeToString(new Q645().constructMaximumBinaryTree(stringToIntegerArray("[3,2,1]"))));
    }

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return func(nums, 0, nums.length);
    }

    TreeNode func(int[] nums, int l, int r) {
        if(l >= r) return null;
        int idx = l, max = nums[l];
        for (int i = l + 1; i < r; i++) {
            if (nums[i] > max) {
                max = nums[i];
                idx = i;
            }
        }
        TreeNode root = new TreeNode(max);
        root.left = func(nums, l, idx);
        root.right = func(nums, idx + 1, r);
        return root;
    }
}
