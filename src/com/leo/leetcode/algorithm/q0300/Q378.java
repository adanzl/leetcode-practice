package com.leo.leetcode.algorithm.q0300;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Objects;
import java.util.PriorityQueue;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
 * 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
 * 提示：
 * 你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。
 * 链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/
 */
public class Q378 {
    public static void main(String[] args) {
        // 56
        System.out.println(new Q378().kthSmallest(stringToInt2dArray("[[5,9,11,12,14,17,20,22],[6,13,17,22,25,27,27,32],[9,15,22,26,28,31,35,39],[13,16,24,30,30,33,35,44],[16,19,28,34,39,44,47,47],[18,20,30,39,43,48,49,53],[22,25,32,40,48,52,56,59],[25,26,35,44,52,57,58,63]]"), 60));
        System.out.println(new Q378().kthSmallest(stringToInt2dArray("[[1,3,5],[6,7,12],[11,14,14]]"), 6)); // 11
        System.out.println(new Q378().kthSmallest(stringToInt2dArray("[[1,2],[3,3]]"), 2)); // 2
        System.out.println(new Q378().kthSmallest(stringToInt2dArray("[[1,5,9],[10,11,13],[12,13,15]]"), 8)); // 13
    }

    static class QNode {
        int i, j, v;

        QNode(int i, int j, int v) {
            this.i = i;
            this.j = j;
            this.v = v;
        }

        @Override
        public String toString() {
            return "{v=" + v + '}';
        }
    }

    public int kthSmallest(int[][] matrix, int k) {
        PriorityQueue<QNode> q = new PriorityQueue<>(Comparator.comparingInt(o -> o.v));
        int count = 0;
        int[] col = new int[matrix.length], row = new int[matrix[0].length];
        Arrays.fill(col, -1);
        Arrays.fill(row, -1);
        QNode node = new QNode(0, 0, matrix[0][0]);
        q.add(node);
        while (count < k) {
            node = q.poll();
            count++;
            int x = Objects.requireNonNull(node).i + 1, y = node.j + 1;
            if (x < matrix.length && x > col[node.j]) {
                q.add(new QNode(x, node.j, matrix[x][node.j]));
                col[node.j] = x;
                if (node.j > row[x]) row[x] = node.j;
            }

            if (y < matrix[0].length && y > row[node.i]) {
                q.add(new QNode(node.i, node.j + 1, matrix[node.i][y]));
                row[node.i] = y;
                if (node.i > col[y]) col[y] = node.i;
            }
        }
        return node.v;
    }
}
