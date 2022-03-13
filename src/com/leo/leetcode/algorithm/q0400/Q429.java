package com.leo.leetcode.algorithm.q0400;

import com.leo.utils.Node;

import java.util.*;

import static com.leo.utils.LCUtil.stringToNodeTree;

/**
 * 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
 * 树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
 * 提示：
 * 1、树的高度不会超过 1000
 * 2、树的节点总数在 [0, 10^4] 之间
 * 链接：https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
 */
public class Q429 {

    public static void main(String[] args) {
        // [[1],[3,2,4],[5,6]]
        System.out.println(new Q429().levelOrder(stringToNodeTree("[1,null,3,2,4,null,5,6]")));
        // [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
        System.out.println(new Q429().levelOrder(stringToNodeTree("[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]")));
    }

    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> ret = new ArrayList<>();
        if (null == root) return null;
        List<Integer> line = new ArrayList<>();
        ret.add(line);
        Node end = root;
        Deque<Node> q = new ArrayDeque<>();
        q.add(root);
        while (!q.isEmpty()) {
            Node p = q.poll();
            if (null != p.children) q.addAll(p.children);
            line.add(p.val);
            if (p == end && !q.isEmpty()) {
                line = new ArrayList<>();
                ret.add(line);
                end = q.getLast();
            }
        }
        return ret;
    }
}
