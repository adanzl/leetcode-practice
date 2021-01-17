package com.leo.leetcode.algorithm.q0400;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

public class Q437 {
    public static void main(String[] args) {
        new Q437().TestOJ();
    }

    public void TestOJ() {
        System.out.println(pathSum(LCUtil.stringToTreeNode("[10,5,-3,3,2,null,11,3,-2,null,1]"), 8)); // 3
    }

    public int pathSum(TreeNode root, int sum) {
        return pathSum(root, sum, new int[100], 0);
    }

    public int pathSum(TreeNode root, int sum, int[] array/*保存路径*/, int p/*指向路径终点*/) {
        if (root == null) {
            return 0;
        }
        int tmp = root.val;
        int n = root.val == sum ? 1 : 0;
        for (int i = p - 1; i >= 0; i--) {
            tmp += array[i];
            if (tmp == sum) {
                n++;
            }
        }
        array[p] = root.val;
        int n1 = pathSum(root.left, sum, array, p + 1);
        int n2 = pathSum(root.right, sum, array, p + 1);
        return n + n1 + n2;
    }

}
