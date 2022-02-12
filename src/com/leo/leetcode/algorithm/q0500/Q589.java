package com.leo.leetcode.algorithm.q0500;

import com.leo.utils.Node;

import java.util.*;


/**
 * 给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。
 * n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
 * 提示：
 * 1、节点总数在范围 [0, 10^4]内
 * 2、0 <= Node.val <= 10^4
 * 3、n 叉树的高度小于或等于 1000
 * 链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal
 */
public class Q589 {

    public static void main(String[] args) {
        System.out.println(new Q589().preorder(null));
    }

    public List<Integer> preorder(Node root) {
        List<Integer> ret = new ArrayList<>();
        visit(root, ret);
        return ret;
    }

    void visit(Node root, List<Integer> out) {
        if (root == null) return;
        out.add(root.val);
        if (root.children != null) {
            for (Node n : root.children) visit(n, out);
        }
    }
}
