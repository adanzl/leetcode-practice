package com.leo.leetcode.algorithm.q0300;

/**
 * 序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。
 * 如果它是一个空节点，我们可以使用一个标记值记录，例如 #。
 * 例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。
 * 给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。
 * 每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。
 * 你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。
 * <p>
 * 链接：https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree
 */
public class Q331 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q331().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"));
        // false
        System.out.println(new Q331().isValidSerialization("1,#"));
        // false
        System.out.println(new Q331().isValidSerialization("9,#,#,1"));
        // true
        System.out.println(new Q331().isValidSerialization("#"));
    }

    public boolean isValidSerialization(String preorder) {
        String[] orders = preorder.split(",");
        int i = parseNode(orders, 0);
        return i == orders.length;
    }

    int parseNode(String[] orders, int i) {
        if (i > orders.length - 1) return i;
        if (orders[i].equals("#")) return i + 1;
        int l = parseNode(orders, i + 1);
        if (l == i + 1) return i;
        int r = parseNode(orders, l);
        if (r == l) return i;
        return r;
    }
}
