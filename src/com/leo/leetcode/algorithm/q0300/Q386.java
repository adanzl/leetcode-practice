package com.leo.leetcode.algorithm.q0300;

import java.util.ArrayList;
import java.util.List;

/**
 * 给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。
 * 你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。
 * 提示：1 <= n <= 5 * 10^4
 * 链接：https://leetcode-cn.com/problems/lexicographical-numbers/
 */
public class Q386 {

    public static void main(String[] args) {
        // [1,10,11,12,13,2,3,4,5,6,7,8,9]
        System.out.println(new Q386().lexicalOrder(13));
        // [1,2]
        System.out.println(new Q386().lexicalOrder(2));
    }

    public List<Integer> lexicalOrder(int n) {
        List<Integer> ret = new ArrayList<>(n);
        for (int i = 1; i < 10; i++) {
            buildRet(i, ret, n);
        }
        return ret;
    }

    void buildRet(int base, List<Integer> out, int n) {
        if (base > n) return;
        out.add(base);
        for (int i = 0; i < 10; i++) {
            buildRet(base * 10 + i, out, n);
        }
    }
}
