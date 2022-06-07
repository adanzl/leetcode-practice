package com.leo.leetcode.algorithm.q0600;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 在无限长的数轴（即 x 轴）上，我们根据给定的顺序放置对应的正方形方块。
 * 第 i 个掉落的方块（positions[i] = (left, side_length)）是正方形，其中 left 表示该方块最左边的点位置(positions[i][0])，side_length 表示该方块的边长(positions[i][1])。
 * 每个方块的底部边缘平行于数轴（即 x 轴），并且从一个比目前所有的落地方块更高的高度掉落而下。在上一个方块结束掉落，并保持静止后，才开始掉落新方块。
 * 方块的底边具有非常大的粘性，并将保持固定在它们所接触的任何长度表面上（无论是数轴还是其他方块）。
 * 邻接掉落的边不会过早地粘合在一起，因为只有底边才具有粘性。
 * 返回一个堆叠高度列表 ans 。
 * 每一个堆叠高度 ans[i] 表示在通过 positions[0], positions[1], ..., positions[i] 表示的方块掉落结束后，目前所有已经落稳的方块堆叠的最高高度。
 * 注意:
 * 1、1 <= positions.length <= 1000.
 * 2、1 <= positions[i][0] <= 10^8.
 * 3、1 <= positions[i][1] <= 10^6.
 * 链接：https://leetcode-cn.com/problems/falling-squares
 */
public class Q699 {

    public static void main(String[] args) {
        // [2,5]
        System.out.println(new Q699().fallingSquares(stringToInt2dArray("[[1,2],[1,3]]")));
        // [7,16,17]
        System.out.println(new Q699().fallingSquares(stringToInt2dArray("[[9,7],[1,9],[3,1]]")));
        // [2, 5, 5]
        System.out.println(new Q699().fallingSquares(stringToInt2dArray("[[1, 2], [2, 3], [6, 1]]")));
        // [100, 100]
        System.out.println(new Q699().fallingSquares(stringToInt2dArray("[[100, 100], [200, 100]]")));
    }
    // 线段树
    public List<Integer> fallingSquares(int[][] positions) {
        Node head = new Node(0, 1_000_000_000);
        List<Integer> ret = new ArrayList<>();
        for (int[] pos : positions) {
            int h = query(head, pos[0], pos[0] + pos[1] - 1);
            addNode(head, pos[0], pos[0] + pos[1] - 1, h + pos[1]);
            ret.add(head.v);
        }
        return ret;
    }

    void addNode(Node root, int l, int r, int v) {
        int mid = (root.l + root.r) >> 1;
        if (root.left == null) root.left = new Node(root.l, mid);
        if (root.right == null) root.right = new Node(mid + 1, root.r);
        if (root.l == l && r == root.r) {
            root.dirty = v;
            root.v = v;
            return;
        }
        pushDown(root);
        if (r <= mid) {
            addNode(root.left, l, r, v);
        } else if (l >= mid + 1) {
            addNode(root.right, l, r, v);
        } else {
            addNode(root.left, l, mid, v);
            addNode(root.right, mid + 1, r, v);
        }
        root.v = Math.max(root.left.v, root.right.v);
    }

    void pushDown(Node root) {
        if (root.dirty == 0) return;
        addNode(root.left, root.left.l, root.left.r, root.dirty);
        addNode(root.right, root.right.l, root.right.r, root.dirty);
        root.dirty = 0;
    }

    int query(Node root, int l, int r) {
        if (root == null) return 0;
        if (root.l == l && root.r == r) return root.v;
        pushDown(root);
        int mid = (root.l + root.r) >> 1;
        if (r <= mid) return query(root.left, l, r);
        if (l >= mid + 1) return query(root.right, l, r);
        return Math.max(query(root.left, l, mid), query(root.right, mid + 1, r));
    }

    static class Node {
        Node left, right;
        int l, r, v, dirty;

        Node(int l, int r) {
            this.l = l;
            this.r = r;
        }
    }
}
