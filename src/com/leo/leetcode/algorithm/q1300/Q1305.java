package com.leo.leetcode.algorithm.q1300;

import com.leo.utils.TreeNode;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。
 * 提示：
 * 1、每棵树的节点数在 [0, 5000] 范围内
 * 2、-10^5 <= Node.val <= 10^5
 * 链接：https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/
 */
public class Q1305 {

    public static void main(String[] args) {
        // [0,1,1,2,3,4]
        System.out.println(new Q1305().getAllElements(stringToTreeNode("[2,1,4]"), stringToTreeNode("[1,0,3]")));
        // [1,1,8,8]
        System.out.println(new Q1305().getAllElements(stringToTreeNode("[1,null,8]"), stringToTreeNode("[8,1]")));
    }

    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> nums1 = new ArrayList<>();
        List<Integer> nums2 = new ArrayList<>();
        inorder(root1, nums1);
        inorder(root2, nums2);

        List<Integer> ret = new ArrayList<>();
        int p1 = 0, p2 = 0;
        while (p1 < nums1.size() && p2 < nums2.size()) {
            if (nums1.get(p1) < nums2.get(p2)) ret.add(nums1.get(p1++));
            else ret.add(nums2.get(p2++));
        }
        while (p1 < nums1.size()) ret.add(nums1.get(p1++));
        while (p2 < nums2.size()) ret.add(nums2.get(p2++));
        return ret;
    }

    public void inorder(TreeNode node, List<Integer> res) {
        if (null == node) return;
        inorder(node.left, res);
        res.add(node.val);
        inorder(node.right, res);
    }
}
