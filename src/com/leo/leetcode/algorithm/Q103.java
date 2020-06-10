package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.TreeNode;

import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

public class Q103 {

    public static void main(String[] args) {
        System.out.println(new Q103().zigzagLevelOrder(LCUtil.stringToTreeNode("[3,9,20,null,null,15,7]"))); // [[3],[20,9],[15,7]]
    }

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> out = new ArrayList<>();
        if (root == null) return out;
        TreeNode p, lEnd = root;
        Deque<TreeNode> q = new LinkedList<>();
        q.add(root);
        List<Integer> line = new ArrayList<>();
        out.add(line);
        int flag = 0;
        while (q.size() != 0) {
            if (flag == 0) p = q.pollFirst();
            else p = q.pollLast();

            if (flag == 0) {
                if (p.left != null) q.addLast(p.left);
                if (p.right != null) q.addLast(p.right);
            } else {
                if (p.right != null) q.addFirst(p.right);
                if (p.left != null) q.addFirst(p.left);
            }
            line.add(p.val);
            if (p == lEnd && q.size() != 0) {
                line = new ArrayList<>();
                out.add(line);
                flag ^= 1;
                if (flag == 0) lEnd = q.getLast();
                else lEnd = q.getFirst();
            }
        }
        return out;
    }
}
