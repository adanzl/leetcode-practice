package com.leo.leetcode.algorithm.q0300;

import java.util.Arrays;
import java.util.List;

/**
 * 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
 * 链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
 */
public class Q315 {

    public static void main(String[] args) {
        System.out.println(new Q315().countSmaller(new int[] { 5, 2, 6, 1 })); // [2,1,1,0]
        System.out.println(new Q315().countSmaller(new int[] { 5, 2, 6, 1 })); // [2,1,1,0]
        System.out.println(new Q315().countSmaller(new int[] { -1, -1 })); // [0,0]
    }

    private static class TreeNode {

        int val;

        TreeNode left;

        TreeNode right;

        int leftCount = 0;

        TreeNode(int val) {
            this.val = val;
        }
    }

    public List<Integer> countSmaller(int[] nums) {
        Integer[] out = new Integer[nums.length];
        Arrays.fill(out, 0);
        TreeNode root = null;
        for (int i = nums.length - 1; i >= 0; i--)
            root = insertTree(root, new TreeNode(nums[i]), out, i);
        return Arrays.asList(out);
    }

    TreeNode insertTree(TreeNode root, TreeNode node, Integer[] outArr, int index) {
        if (root == null) return node;
        if (node.val <= root.val) {
            root.leftCount++;
            root.left = insertTree(root.left, node, outArr, index);
        } else {
            outArr[index] += root.leftCount + 1;
            root.right = insertTree(root.right, node, outArr, index);
        }
        return root;
    }
}
