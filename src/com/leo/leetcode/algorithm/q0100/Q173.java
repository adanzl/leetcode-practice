package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.TreeNode;

import java.util.Stack;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
 * 调用 next() 将返回二叉搜索树中的下一个最小的数。
 * <p>
 * 提示：
 * 1、next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
 * 2、你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
 * <p>
 * 链接：https://leetcode-cn.com/problems/binary-search-tree-iterator
 */
public class Q173 {

    public static void main(String[] args) {
        BSTIterator obj = new BSTIterator(stringToTreeNode("[7,3,15,null,null,9,20]"));
        System.out.println(obj.next());  // 3
        System.out.println(obj.next()); // 7
        System.out.println(obj.hasNext()); // true
        System.out.println(obj.next()); // 9
        System.out.println(obj.hasNext()); // true
        System.out.println(obj.next()); // 15
        System.out.println(obj.hasNext()); // true
        System.out.println(obj.next());// 20
        System.out.println(obj.hasNext()); // false
    }

    static class BSTIterator {

        Stack<TreeNode> s = new Stack<>();

        public BSTIterator(TreeNode root) {
            while (root != null) {
                s.push(root);
                root = root.left;
            }
        }

        public int next() {
            TreeNode node = s.pop(), p = node.right;
            while (p != null) {
                s.push(p);
                p = p.left;
            }
            return node.val;
        }

        public boolean hasNext() {
            return !s.isEmpty();
        }
    }
}
