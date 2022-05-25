package com.leo.leetcode.algorithm.q0900;

import com.leo.utils.TestCase;
import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 给定一个二叉树，我们在树的节点上安装摄像头。
 * 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
 * 计算监控树的所有节点所需的最小摄像头数量。
 * 提示：
 * 1、给定树的节点数的范围是 [1, 1000]。
 * 2、每个节点的值都是 0。
 * 链接：https://leetcode-cn.com/problems/binary-tree-cameras/
 */
public class Q968 {

    public static void main(String[] args) {
        TestCase tc = new TestCase("resources/algorithm/q0900/Q968/Case001.txt");
        // 360
        System.out.println(new Q968().minCameraCover(stringToTreeNode(tc.getData(0))));
        // 1
        System.out.println(new Q968().minCameraCover(stringToTreeNode("[1,2,null,3,4]")));
        // 2
        System.out.println(new Q968().minCameraCover(stringToTreeNode("[0,0,null,0,null,0,null,null,0]")));
    }

    public int minCameraCover(TreeNode root) {
        return dfs(root)[2]; // root必须1-root有人管-root无人管
    }

    int[] dfs(TreeNode root) {
        if (root == null) return new int[]{2000, 0, 0};
        int[] lRet = dfs(root.left), rRet = dfs(root.right); // sign root
        int[] ret = new int[3];
        ret[0] = lRet[1] + rRet[1] + 1; // root必须1
        ret[1] = Math.min(ret[0], lRet[2] + rRet[2]); // root有人管 root=1/0
        ret[2] = Math.min(ret[0], Math.min(lRet[0] + rRet[2], lRet[2] + rRet[0]));  // root无人管 root=1/0
        return ret;
    }

}
