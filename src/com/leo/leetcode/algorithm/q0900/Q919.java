package com.leo.leetcode.algorithm.q0900;

import com.leo.utils.Executor;
import com.leo.utils.TreeNode;

import java.util.ArrayDeque;
import java.util.Queue;

import static com.leo.utils.LCUtil.stringToTreeNode;
import static com.leo.utils.LCUtil.treeNodeToString;

/**
 * 完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。
 * 设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。
 * 实现 CBTInserter 类:
 * 1、CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
 * 2、CBTInserter.insert(int v)  向树中插入一个值为 Node.val == val的新节点 TreeNode。使树保持完全二叉树的状态，并返回插入节点 TreeNode 的父节点的值；
 * 3、CBTInserter.get_root() 将返回树的头节点。
 * 提示：
 * 1、树中节点数量范围为 [1, 1000]
 * 2、0 <= Node.val <= 5000
 * 3、root 是完全二叉树
 * 4、0 <= val <= 5000
 * 5、每个测试用例最多调用 insert 和 get_root 操作 10^4 次
 * 链接：https://leetcode.cn/problems/complete-binary-tree-inserter
 */
public class Q919 {

    public static void main(String[] args) {
        CBTInserter cBTInserter = new CBTInserter(stringToTreeNode("[1, 2]"));
        cBTInserter.insert(3);  // 返回 1
        cBTInserter.insert(4);  // 返回 2
        System.out.println(treeNodeToString(cBTInserter.get_root())); // 返回 [1, 2, 3, 4]
        new Executor(Q919.class).execute(
                "[\"CBTInserter\", \"insert\", \"insert\", \"get_root\"]",
                "[[[1, 2]], [3], [4], []]");
    }

    static class CBTInserter {
        Queue<TreeNode> q = new ArrayDeque<>();

        TreeNode root;

        public CBTInserter(TreeNode root) {
            this.root = root;
            q.offer(root);
            TreeNode p;
            while (!q.isEmpty()) {
                p = q.peek();
                if (p.left != null) q.offer(p.left);
                if (p.right != null) q.offer(p.right);
                if (p.left != null && p.right != null) q.poll();
                else break;
            }
        }

        public int insert(int val) {
            if (q.isEmpty()) return -1;
            TreeNode p = q.peek();
            if (p.left == null) {
                p.left = new TreeNode(val);
                q.offer(p.left);
            } else {
                p.right = new TreeNode(val);
                q.offer(p.right);
                q.poll();
            }
            return p.val;
        }

        public TreeNode get_root() {
            return this.root;
        }
    }
}
