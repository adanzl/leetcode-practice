package com.leo.leetcode.algorithm.q0500;

import com.leo.utils.Node;

import java.util.*;

import static com.leo.utils.LCUtil.stringToNodeTree;

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
        // [1,3,5,6,2,4]
        System.out.println(new Q589().preorder(stringToNodeTree("[1,null,3,2,4,null,5,6]")));
        // [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
        System.out.println(new Q589().preorder(stringToNodeTree("[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]")));
        // []
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
