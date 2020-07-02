package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

/**
 * 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
 * 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
 * 链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
 */
public class Q108 {
    public static void main(String[] args) {
        System.out.println(LCUtil.treeNodeToString(new Q108().sortedArrayToBST(new int[]{-10, -3, 0, 5, 9}))); // [0,-3,9,-10,null,5]
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        return buildBST(nums, 0, nums.length);
    }

    TreeNode buildBST(int[] nums, int s, int e) {
        if (s >= e) return null;
        int mid = s + ((e - s) >> 1);
        TreeNode out = new TreeNode(nums[mid]);
        out.left = buildBST(nums, s, mid);
        out.right = buildBST(nums, mid + 1, e);
        return out;
    }
}
