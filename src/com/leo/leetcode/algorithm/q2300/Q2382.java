package com.leo.leetcode.algorithm.q2300;


import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你两个下标从 0 开始的整数数组 nums 和 removeQueries ，两者长度都为 n 。对于第 i 个查询，nums 中位于下标 removeQueries[i] 处的元素被删除，将 nums 分割成更小的子段。
 * 一个 子段 是 nums 中连续 正 整数形成的序列。子段和 是子段中所有元素的和。
 * 请你返回一个长度为 n 的整数数组 answer ，其中 answer[i]是第 i 次删除操作以后的 最大 子段和。
 * 注意：一个下标至多只会被删除一次。
 * 提示：
 * 1、n == nums.length == removeQueries.length
 * 2、1 <= n <= 10^5
 * 3、1 <= nums[i] <= 10^9
 * 4、0 <= removeQueries[i] < n
 * 5、removeQueries 中所有数字 互不相同 。
 * 链接：https://leetcode.cn/problems/maximum-segment-sum-after-removals
 */
public class Q2382 {

    public static void main(String[] args) {
        // [14,7,2,2,0]
        System.out.println(Arrays.toString(new Q2382().maximumSegmentSum(stringToIntegerArray("[1,2,5,6,1]"), stringToIntegerArray("[0,3,2,4,1]"))));
        // [16,5,3,0]
        System.out.println(Arrays.toString(new Q2382().maximumSegmentSum(stringToIntegerArray("[3,2,11,1]"), stringToIntegerArray("[3,2,1,0]"))));
    }

    Node head;
    long[] ans;

    public long[] maximumSegmentSum(int[] nums, int[] removeQueries) {
        head = new Node(0, nums.length - 1);
        int n = nums.length;
        long[] preSum = new long[n + 1];
        for (int i = 0; i < n; i++) preSum[i + 1] = preSum[i] + nums[i];
        addNode(head, 0, n - 1, preSum[n], 0, n - 1);
        ans = new long[n];
        for (int i = 0; i < n; i++) {
            int idx = removeQueries[i];
            int[] q = query(head, idx, idx);
            int rl = q[0], rr = q[1];
            addNode(head, rl, rr, 0, rl, rr);
            addNode(head, rl, idx - 1, preSum[idx] - preSum[rl], rl, idx - 1);
            addNode(head, idx + 1, rr, preSum[rr + 1] - preSum[idx + 1], idx + 1, rr);
            ans[i] = head.max;
        }
        return ans;
    }

    void addNode(Node root, int l, int r, long v, int rl, int rr) {
        if (l > r) return;
        int mid = root.l + (root.r - root.l) / 2;
        if (root.left == null) root.left = new Node(root.l, mid);
        if (root.right == null) root.right = new Node(mid + 1, root.r);
        if (root.l == l && r == root.r) {
            root.dirty = v;
            root.v = v;
            root.max = v;
            root.rl = rl;
            root.rr = rr;
            return;
        }
        pushDown(root);
        if (r <= mid) {
            addNode(root.left, l, r, v, rl, rr);
        } else if (l >= mid + 1) {
            addNode(root.right, l, r, v, rl, rr);
        } else {
            addNode(root.left, l, mid, v, rl, rr);
            addNode(root.right, mid + 1, r, v, rl, rr);
        }
        root.max = Math.max(root.left.max, root.right.max);
        root.v = v;
    }

    int[] query(Node root, int l, int r) {
        if (root == null || l > r) return new int[]{l, r};
        if (root.l == l && root.r == r) return new int[]{root.rl, root.rr};
        pushDown(root);
        int mid = root.l + (root.r - root.l) / 2;
        if (mid < l) return query(root.right, l, r);
        if (r <= mid) return query(root.left, l, r);
        int[] qLeft = query(root.left, l, mid), qRight = query(root.right, mid + 1, r);
        return new int[]{Math.min(qLeft[0], qRight[0]), Math.max(qLeft[1], qRight[1])};
    }

    void pushDown(Node root) {
        if (root.dirty == -1) return;
        addNode(root.left, root.left.l, root.left.r, root.dirty, root.rl, root.rr);
        addNode(root.right, root.right.l, root.right.r, root.dirty, root.rl, root.rr);
        root.dirty = -1;
    }

    static class Node {
        Node left, right;
        int l, r;
        int rl, rr;
        long v, max, dirty = -1;

        Node(int l, int r) {
            this.l = l;
            this.r = r;
        }
    }
}
