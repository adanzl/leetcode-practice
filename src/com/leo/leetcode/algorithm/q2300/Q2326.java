package com.leo.leetcode.algorithm.q2300;

import com.leo.utils.ListNode;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToListNode;

/**
 * 给你两个整数：m 和 n ，表示矩阵的维数。
 * 另给你一个整数链表的头节点 head 。
 * 请你生成一个大小为 m x n 的螺旋矩阵，矩阵包含链表中的所有整数。链表中的整数从矩阵 左上角 开始、顺时针 按 螺旋 顺序填充。如果还存在剩余的空格，则用 -1 填充。
 * 返回生成的矩阵。
 * 提示：
 * 1、1 <= m, n <= 10^5
 * 2、1 <= m * n <= 10^5
 * 3、链表中节点数目在范围 [1, m * n] 内
 * 4、0 <= Node.val <= 1000
 * 链接：https://leetcode.cn/problems/spiral-matrix-iv
 */
public class Q2326 {

    public static void main(String[] args) {
        // [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
        System.out.println(Arrays.deepToString(new Q2326().spiralMatrix(3, 5, stringToListNode("[3,0,2,6,8,1,7,9,4,2,5,5,0]"))));
        // [[0,1,2,-1]]
        System.out.println(Arrays.deepToString(new Q2326().spiralMatrix(1, 4, stringToListNode("[0,1,2]"))));
    }

    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int[][] ret = new int[m][n];
        int d = 0; // 0 ->, 1 d, 2 <-, 3 ^
        ListNode p = head;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ret[i][j] = -1;
            }
        }
        int x = 0, y = 0, lLimit = -1, rLimit = n, uLimit = -1, dLimit = m;
        while (p != null) {
            ret[y][x] = p.val;
            p = p.next;
            if (d == 0) {
                if (x < rLimit - 1) x++;
                else {
                    d = 1;
                    uLimit = y;
                    y++;
                }
            } else if (d == 1) {
                if (y < dLimit - 1) y++;
                else {
                    d = 2;
                    rLimit = x;
                    x--;
                }
            } else if (d == 2) {
                if (x > lLimit + 1) x--;
                else {
                    d = 3;
                    dLimit = y;
                    y--;
                }
            } else {
                if (y > uLimit + 1) y--;
                else {
                    d = 0;
                    lLimit = x;
                    x++;
                }
            }
        }
        return ret;
    }
}
