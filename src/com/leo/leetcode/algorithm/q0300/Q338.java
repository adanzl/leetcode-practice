package com.leo.leetcode.algorithm.q0300;

import java.util.Arrays;

/**
 * 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
 * <p>
 * 进阶:
 * 1、给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
 * 2、要求算法的空间复杂度为O(n)。
 * 3、你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
 * <p>
 * 链接：https://leetcode-cn.com/problems/counting-bits
 */
public class Q338 {

    public static void main(String[] args) {
        // []
        System.out.println(Arrays.toString(new Q338().countBits(0)));
        // [0,1,1]
        System.out.println(Arrays.toString(new Q338().countBits(2)));
        // [0,1,1,2,1,2]
        System.out.println(Arrays.toString(new Q338().countBits(5)));
    }

    public int[] countBits(int num) {
        int[] ret = new int[num + 1];
        ret[0] = 0;
        int v = 1;
        for (int i = 1; i <= num; i++) {
            if (v << 1 == i) v <<= 1;
            ret[i] = ret[i - v] + 1;
        }
        return ret;
    }
}
