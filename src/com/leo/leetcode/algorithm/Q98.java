package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;
import org.junit.Test;

import java.util.Stack;

public class Q98 {
    @Test
    public void TestOJ() {
        System.out.println(isValidBST(LCUtil.stringToTreeNode("[1,1]"))); // false
        System.out.println(isValidBST(LCUtil.stringToTreeNode("[5,1,4,null,null,3,6]"))); // false
        System.out.println(isValidBST(LCUtil.stringToTreeNode("[10,5,15,null,null,6,20]"))); // false
        System.out.println(isValidBST(LCUtil.stringToTreeNode("[-2147483648]"))); // t
        System.out.println(isValidBST(LCUtil.stringToTreeNode("[-2147483648, null, 2147483647]"))); // t
        System.out.println(isValidBST(LCUtil.stringToTreeNode("[2, 1, 3]"))); // t
    }

    public boolean isValidBST(TreeNode root) {
        TreeNode p = root;
        if (p == null) {
            return true;
        }
        Stack<TreeNode> s = new Stack<>();
        TreeNode limit = null;
        while (p != null || !s.empty()) {
            while (p != null) {
                s.push(p);
                p = p.left;
            }
            p = s.pop();
            if (limit != null && p != limit && p.val <= limit.val) {
                return false;
            }
            limit = p;
            p = p.right;
        }

        return true;
    }
}
