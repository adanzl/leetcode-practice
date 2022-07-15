package com.leo.leetcode.algorithm.q0400;

import com.leo.utils.Node4;

import static com.leo.utils.LCUtil.node4ToString;
import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 n * n 矩阵 grid ，矩阵由若干 0 和 1 组成。请你用四叉树表示该矩阵 grid 。
 * 你需要返回能表示矩阵的 四叉树 的根结点。
 * 注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。
 * 四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：
 * 1、val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False；
 * 2、isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。
 * 我们可以按以下步骤为二维区域构建四叉树：
 * 1、如果当前网格的值相同（即，全为 0 或者全为 1），将 isLeaf 设为 True ，将 val 设为网格相应的值，并将四个子节点都设为 Null 然后停止。
 * 2、如果当前网格的值不同，将 isLeaf 设为 False， 将 val 设为任意值，然后如下图所示，将当前网格划分为四个子网格。
 * 3、使用适当的子网格递归每个子节点。
 * 如果你想了解更多关于四叉树的内容，可以参考 https://en.wikipedia.org/wiki/Quadtree 。
 * 四叉树格式：
 * 输出为使用层序遍历后四叉树的序列化形式，其中 null 表示路径终止符，其下面不存在节点。
 * 它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 [isLeaf, val] 。
 * 如果 isLeaf 或者 val 的值为 True ，则表示它在列表 [isLeaf, val] 中的值为 1 ；如果 isLeaf 或者 val 的值为 False ，则表示值为 0 。
 * 提示：
 * 1、n == grid.length == grid[i].length
 * 2、n == 2^x 其中 0 <= x <= 6
 * 链接：https://leetcode-cn.com/problems/construct-quad-tree
 */
public class Q427 {

    public static void main(String[] args) {
        // [[0,1],[0,1],[0,1],[0,1],[0,1],[1,1],[1,1],[1,0],[1,0],[1,0],[1,0],[1,1],[1,1],[1,1],[1,1],[1,0],[1,0],[1,0],[1,0],[1,1],[1,1]]
        System.out.println(node4ToString(new Q427().construct(stringToInt2dArray("[[1,1,0,0],[0,0,1,1],[1,1,0,0],[0,0,1,1]]"))));
        // [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
        System.out.println(node4ToString(new Q427().construct(stringToInt2dArray("[[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]"))));
        // [[0,1],[1,0],[1,1],[1,1],[1,0]]
        System.out.println(node4ToString(new Q427().construct(stringToInt2dArray("[[0,1],[1,0]]"))));
        // [[1,1]]
        System.out.println(node4ToString(new Q427().construct(stringToInt2dArray("[[1,1],[1,1]]"))));
        // [[1,0]]
        System.out.println(node4ToString(new Q427().construct(stringToInt2dArray("[[0]]"))));
        // [[0,1],[1,1],[1,0],[1,0],[1,1]]
        System.out.println(node4ToString(new Q427().construct(stringToInt2dArray("[[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]"))));
    }

    public Node construct(int[][] grid) {
        int n = grid.length;
        return build4Tree(grid, 0, n - 1, 0, n - 1);
    }

    Node build4Tree(int[][] grid, int r0, int r1, int c0, int c1) {
        if (r0 == r1) return new Node(grid[r0][c0] == 1, true);
        Node ret;
        Node topLeft = build4Tree(grid, r0, (r0 + r1) / 2, c0, (c0 + c1) / 2);
        Node topRight = build4Tree(grid, r0, (r0 + r1) / 2, (c0 + c1) / 2 + 1, c1);
        Node bottomLeft = build4Tree(grid, (r0 + r1) / 2 + 1, r1, c0, (c0 + c1) / 2);
        Node bottomRight = build4Tree(grid, (r0 + r1) / 2 + 1, r1, (c0 + c1) / 2 + 1, c1);
        if (topLeft.val == topRight.val && topRight.val == bottomLeft.val && bottomLeft.val == bottomRight.val &&
                topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf) {
            ret = new Node(true, topLeft.val);
        } else {
            ret = new Node(false, true, topLeft, topRight, bottomLeft, bottomRight);
        }
        return ret;
    }

    static class Node extends Node4 {
        public Node(boolean isLeaf, boolean val) {
            super(isLeaf, val);
        }

        public Node(boolean isLeaf, boolean val, Object topLeft, Object topRight, Object bottomLeft, Object bottomRight) {
            super(isLeaf, val, (Node4) topLeft, (Node4) topRight, (Node4) bottomLeft, (Node4) bottomRight);
        }
    }

}
