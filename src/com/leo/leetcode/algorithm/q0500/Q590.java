package com.leo.leetcode.algorithm.q0500;

import com.leo.utils.Node;

import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

import static com.leo.utils.LCUtil.stringToNodeTree;

/**
 * 给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。
 * n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
 * 提示：
 * 1、节点总数在范围 [0, 10^4] 内
 * 2、0 <= Node.val <= 10^4
 * 3、n 叉树的高度小于或等于 1000
 * 进阶：递归法很简单，你可以使用迭代法完成此题吗?
 * 链接：https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal
 */
public class Q590 {

    public static void main(String[] args) {
        // [5,6,3,2,4,1]
        System.out.println(new Q590().postorder(stringToNodeTree("[1,null,3,2,4,null,5,6]")));
        // [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
        System.out.println(new Q590().postorder(stringToNodeTree("[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]")));
    }

    public List<Integer> postorder(Node root) {
        LinkedList<Integer> ret = new LinkedList<>();
        Stack<Node> stack = new Stack<>();
        if (root != null) stack.push(root);
        while (!stack.empty()) {
            Node n = stack.pop();
            ret.addFirst(n.val);
            if (n.children == null) continue;
            for (Node child : n.children) {
                stack.push(child);
            }
        }
        return ret;
    }
}
