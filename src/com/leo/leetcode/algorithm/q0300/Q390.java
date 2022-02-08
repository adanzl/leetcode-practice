package com.leo.leetcode.algorithm.q0300;

/**
 * 列表 arr 由在范围 [1, n] 中的所有整数组成，并按严格递增排序。请你对 arr 应用下述算法：
 * 从左到右，删除第一个数字，然后每隔一个数字删除一个，直到到达列表末尾。
 * 重复上面的步骤，但这次是从右到左。也就是，删除最右侧的数字，然后剩下的数字每隔一个删除一个。
 * 不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
 * 给你整数 n ，返回 arr 最后剩下的数字。
 * 提示：
 * 1 <= n <= 10^9
 * <p>
 * 链接：https://leetcode-cn.com/problems/elimination-game
 */
public class Q390 {

    public static void main(String[] args) {
        // 534765398
        System.out.println(new Q390().lastRemaining(1000000000));
        // 8
        System.out.println(new Q390().lastRemaining(10));
        // 6
        System.out.println(new Q390().lastRemaining(9));
        // 1
        System.out.println(new Q390().lastRemaining(1));
    }

    public int lastRemaining(int n) {
        int a1 = 1;
        int k = 0, cnt = n, step = 1;
        while (cnt > 1) {
            if (k % 2 == 0) a1 += step;
            else a1 = (cnt % 2 == 0) ? a1 : a1 + step;
            k++;
            cnt >>= 1;
            step <<= 1;
        }
        return a1;
    }
}
