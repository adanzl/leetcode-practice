package com.leo.leetcode.algorithm.q0500;

import com.leo.utils.Node4;

import static com.leo.utils.LCUtil.node4ToString;
import static com.leo.utils.LCUtil.stringToNode4Tree;

/**
 * 二进制矩阵中的所有元素不是 0 就是 1 。
 * 给你两个四叉树，quadTree1 和 quadTree2。其中 quadTree1 表示一个 n * n 二进制矩阵，而 quadTree2 表示另一个 n * n 二进制矩阵。
 * 请你返回一个表示 n * n 二进制矩阵的四叉树，它是 quadTree1 和 quadTree2 所表示的两个二进制矩阵进行 按位逻辑或运算 的结果。
 * 注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。
 * 四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：
 * 1、val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False；
 * 2、isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。
 * 我们可以按以下步骤为二维区域构建四叉树：
 * 1、如果当前网格的值相同（即，全为 0 或者全为 1），将 isLeaf 设为 True ，将 val 设为网格相应的值，并将四个子节点都设为 Null 然后停止。
 * 2、如果当前网格的值不同，将 isLeaf 设为 False， 将 val 设为任意值，然后如下图所示，将当前网格划分为四个子网格。
 * 3、使用适当的子网格递归每个子节点。
 * 如果你想了解更多关于四叉树的内容，可以参考 wiki 。
 * 四叉树格式：
 * 输出为使用层序遍历后四叉树的序列化形式，其中 null 表示路径终止符，其下面不存在节点。
 * 它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 [isLeaf, val] 。
 * 如果 isLeaf 或者 val 的值为 True ，则表示它在列表 [isLeaf, val] 中的值为 1 ；如果 isLeaf 或者 val 的值为 False ，则表示值为 0 。
 * 提示：
 * 1、quadTree1 和 quadTree2 都是符合题目要求的四叉树，每个都代表一个 n * n 的矩阵。
 * 2、n == 2^x ，其中 0 <= x <= 9.
 * 链接：https://leetcode.cn/problems/logical-or-of-two-binary-grids-represented-as-quad-trees
 */
public class Q558 {

    public static void main(String[] args) {
        // [[0,0],[0,0],[0,0],[0,0],[0,0],[1,1],[0,0],[0,0],[0,0],[1,1],[1,1],[0,0],[0,0],[1,1],[0,0],[1,1],[1,1],[0,0],[0,0],[0,0],[0,0],null,null,null,null,[1,0],[1,1],[1,0],[1,0],[1,0],[1,1],[1,0],[1,1],[1,1],[1,1],[1,0],[1,0],null,null,null,null,null,null,null,null,[1,0],[1,0],[1,1],[1,1],[1,1],[1,0],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[1,1],[1,1],null,null,null,null,null,null,null,null,[1,0],[1,1],[1,0],[1,1],[1,1],[1,1],[1,0],[1,1],[1,1],[1,1],[1,0],[1,0],[1,1],[1,0],[1,1],[1,1]]
        System.out.println(node4ToString(new Q558().intersect(
                Node.Create(stringToNode4Tree("[[0,0],[0,0],[0,0],[0,0],[0,0],[1,1],[0,0],[0,0],[0,0],[1,1],[0,0],[0,0],[0,0],[1,1],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],null,null,null,null,[1,0],[1,1],[1,0],[1,0],[1,0],[1,1],[1,0],[1,1],[1,1],[1,1],[1,0],[1,0],null,null,null,null,[1,1],[1,1],[1,0],[1,0],[1,0],[1,0],[1,1],[1,1],[1,1],[1,0],[1,0],[1,1],null,null,null,null,[1,0],[1,0],[1,1],[1,0],[1,1],[1,0],[1,1],[1,1],[1,1],[1,1],[1,0],[1,1],null,null,null,null,[1,1],[1,1],[1,0],[1,1],[1,1],[1,1],[1,0],[1,0],[1,1],[1,0],[1,1],[1,1]]"))
                , Node.Create(stringToNode4Tree("[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,1],[1,0],[0,0],[1,1],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[1,1],[1,1],[1,0],[1,0],[1,0],[1,1],[1,0],[1,0],[1,0],[1,0],[1,0],[1,1],[1,1],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1],[1,0],null,null,null,null,null,null,null,null,[1,0],[1,0],[1,1],[1,0],null,null,null,null,[1,1],[1,0],[1,1],[1,1],[1,1],[1,1],[1,0],[1,0],[1,1],[1,1],[1,1],[1,0],[1,0],[1,1],[1,0],[1,1],[1,0],[1,1],[1,0],[1,0],null,null,null,null,[1,0],[1,0],[1,0],[1,1]]"))).toNode4()));
        // [[0,0],[0,1],[0,1],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1],[1,0],[1,0],[1,1],[1,1]]
        System.out.println(node4ToString(new Q558().intersect(
                Node.Create(stringToNode4Tree("[[0,1],[1,0],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]"))
                , Node.Create(stringToNode4Tree("[[0,1],[0,1],[1,0],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1]]"))).toNode4()));
        // [[0,0],[1,1],[0,1],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[1,0],[1,1]]
        System.out.println(node4ToString(new Q558().intersect(
                Node.Create(stringToNode4Tree("[[0,0],[1,1],[1,0],[1,1],[1,1]]"))
                , Node.Create(stringToNode4Tree("[[0,0],[1,1],[0,1],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[1,0],[1,1]]"))).toNode4()));
        // [[0,0],[1,1],[1,1],[1,1],[1,0]]
        System.out.println(node4ToString(new Q558().intersect(
                Node.Create(stringToNode4Tree("[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]"))
                , Node.Create(stringToNode4Tree("[[0,1],[1,1],[1,1],[1,0],[1,0]]"))).toNode4()));
        // [[1,0]]
        System.out.println(node4ToString(new Q558().intersect(
                Node.Create(stringToNode4Tree("[[1,0]]"))
                , Node.Create(stringToNode4Tree("[[1,0]]"))).toNode4()));
    }

    public Node intersect(Node quadTree1, Node quadTree2) {
        if (quadTree1 == null || quadTree2 == null) return null;
        if (quadTree1.isLeaf && quadTree2.isLeaf) {
            quadTree1.val |= quadTree2.val;
        } else if (quadTree1.isLeaf) {
            quadTree1.topLeft = intersect(new Node(quadTree1.val, true, null, null, null, null), quadTree2.topLeft);
            quadTree1.topRight = intersect(new Node(quadTree1.val, true, null, null, null, null), quadTree2.topRight);
            quadTree1.bottomLeft = intersect(new Node(quadTree1.val, true, null, null, null, null), quadTree2.bottomLeft);
            quadTree1.bottomRight = intersect(new Node(quadTree1.val, true, null, null, null, null), quadTree2.bottomRight);
        } else if (quadTree2.isLeaf) {
            quadTree1.topLeft = intersect(quadTree1.topLeft, new Node(quadTree2.val, true, null, null, null, null));
            quadTree1.topRight = intersect(quadTree1.topRight, new Node(quadTree2.val, true, null, null, null, null));
            quadTree1.bottomLeft = intersect(quadTree1.bottomLeft, new Node(quadTree2.val, true, null, null, null, null));
            quadTree1.bottomRight = intersect(quadTree1.bottomRight, new Node(quadTree2.val, true, null, null, null, null));
        } else {
            quadTree1.topLeft = intersect(quadTree1.topLeft, quadTree2.topLeft);
            quadTree1.topRight = intersect(quadTree1.topRight, quadTree2.topRight);
            quadTree1.bottomLeft = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft);
            quadTree1.bottomRight = intersect(quadTree1.bottomRight, quadTree2.bottomRight);
        }
        if (quadTree1.topLeft == null ||
                (quadTree1.topLeft.isLeaf
                        &&quadTree1.topRight.isLeaf
                        &&quadTree1.bottomLeft.isLeaf
                        &&quadTree1.bottomRight.isLeaf
                        &&quadTree1.topLeft.val == quadTree1.topRight.val
                        && quadTree1.topLeft.val == quadTree1.bottomLeft.val
                        && quadTree1.topLeft.val == quadTree1.bottomRight.val)) {
            if (quadTree1.topLeft != null) quadTree1.val = quadTree1.topLeft.val;
            quadTree1.topLeft = null;
            quadTree1.topRight = null;
            quadTree1.bottomLeft = null;
            quadTree1.bottomRight = null;
            quadTree1.isLeaf = true;
        } else {
            quadTree1.isLeaf = false;
            quadTree1.val = false;
        }
        return quadTree1;
    }

    static class Node {
        public boolean val;
        public boolean isLeaf;
        public Node topLeft;
        public Node topRight;
        public Node bottomLeft;
        public Node bottomRight;

        public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
            this.val = val;
            this.isLeaf = isLeaf;
            this.topLeft = topLeft;
            this.topRight = topRight;
            this.bottomLeft = bottomLeft;
            this.bottomRight = bottomRight;
        }

        public Node(Node4 node) {
            this(node.val, node.isLeaf, Node.Create(node.topLeft), Node.Create(node.topRight), Node.Create(node.bottomLeft), Node.Create(node.bottomRight));
        }

        static Node Create(Node4 node) {
            if (null == node) return null;
            return new Node(node);
        }

        public Node4 toNode4() {
            Node4 node = new Node4(isLeaf, val);
            if (topLeft != null) node.topLeft = topLeft.toNode4();
            if (topRight != null) node.topRight = topRight.toNode4();
            if (bottomLeft != null) node.bottomLeft = bottomLeft.toNode4();
            if (bottomRight != null) node.bottomRight = bottomRight.toNode4();
            return node;
        }

    }
}
