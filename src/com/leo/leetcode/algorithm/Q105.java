package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

import java.util.HashMap;

public class Q105 {
    public void TestOJ() {
        System.out.println(LCUtil.treeNodeToString(buildTree(LCUtil.stringToIntegerArray("[3,9,20,15,7]"), LCUtil.stringToIntegerArray("[9,3,15,20,7]")))); // [3, 9, 20, 15, 7]
        System.out.println(LCUtil.treeNodeToString(buildTree(LCUtil.stringToIntegerArray("[]"), LCUtil.stringToIntegerArray("[]"))));
    }

//    private int iPre = 0;

    //    public TreeNode buildTree(int[] preOrder, int[] inOrder) {
//        return build(preOrder, inOrder, 0, inOrder.length);
//    }
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
//    TreeNode build(int[] preOrder, int[] inOrder, int l, int r) {
//        if (iPre >= preOrder.length || l >= r) {
//            return null;
//        }
//        TreeNode ret = new TreeNode(preOrder[iPre++]);
//        int iRoot = f(inOrder, ret.val);
//        ret.left = build(preOrder, inOrder, l, iRoot);
//        ret.right = build(preOrder, inOrder, iRoot + 1, r);
//
//        return ret;
//    }
//
//    int f(int[] arr, int value) {
//        for (int i = 0; i < arr.length; i++) {
//            if (arr[i] == value) {
//                return i;
//            }
//        }
//        return -1;
//    }
}
