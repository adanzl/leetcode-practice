package com.leo.leetcode.algorithm.q0700;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。
 * 一次交换可选择任意两人，让他们站起来交换座位。
 * 人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)。
 * 这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。
 * <p>
 * 说明:
 * 1、len(row) 是偶数且数值在 [4, 60]范围内。
 * 2、可以保证row 是序列 0...len(row)-1 的一个全排列。
 * <p>
 * 链接：https://leetcode-cn.com/problems/couples-holding-hands
 */
public class Q765 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q765().minSwapsCouples(stringToIntegerArray("[1,4, 0,5, 8,7, 6,3, 2,9]")));
        // 4
        System.out.println(new Q765().minSwapsCouples(stringToIntegerArray("[10,7, 4,2, 3,0, 9,11, 1,5, 6,8, 12,13]")));
        // 1
        System.out.println(new Q765().minSwapsCouples(stringToIntegerArray("[0, 2, 1, 3]")));
        // 0
        System.out.println(new Q765().minSwapsCouples(stringToIntegerArray("[3, 2, 0, 1]")));
    }

    int[] parent;
    int count;

    public int minSwapsCouples(int[] row) {
        int ret = 0;
        parent = new int[row.length];
        count = row.length;
        for (int i = 0; i < row.length; i++) parent[i] = i;
        for (int i = 0; i < row.length >> 1; i++) {
            int idx = i << 1, n0 = row[idx], n1 = row[idx + 1];
            if (Math.abs(n0 - n1) != 1 || Math.min(n0, n1) % 2 == 1) {
                ret++;
                if (n0 % 2 == 0) merge(n0, n0 + 1);
                else merge(n0, n0 - 1);
                if (n1 % 2 == 0) merge(n1, n1 + 1);
                else merge(n1, n1 - 1);
                merge(n0, n1);
            } else {
                count -= 2;
            }
        }
        return ret - count;
    }

    int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }

    void merge(int i0, int i1) {
        int r0 = find(i0), r1 = find(i1);
        if (r0 == r1) return;
        parent[r1] = r0;
        count--;
    }
}
