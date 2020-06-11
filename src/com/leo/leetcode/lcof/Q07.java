package com.leo.leetcode.lcof;

import com.leo.utils.TreeNode;

import java.util.HashMap;

public class Q07 {

    public static void main(String[] args) {
        System.out.println(new Q07().buildTree(new int[]{3, 9, 20, 15, 7}, new int[]{9, 3, 15, 20, 7})); //
    }

    HashMap<Integer, Integer> dic = new HashMap<>();
    int[] po;

    public TreeNode buildTree(int[] preOrder, int[] inOrder) {
        po = preOrder;
        for (int i = 0; i < inOrder.length; i++)
            dic.put(inOrder[i], i);
        return recur(0, 0, inOrder.length - 1);
    }

    TreeNode recur(int pre_root, int in_left, int in_right) {
        if (in_left > in_right) return null;
        TreeNode root = new TreeNode(po[pre_root]);
        int i = dic.get(po[pre_root]);
        root.left = recur(pre_root + 1, in_left, i - 1);
        root.right = recur(pre_root + i - in_left + 1, i + 1, in_right);
        return root;
    }
}
