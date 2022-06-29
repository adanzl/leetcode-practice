package com.leo.leetcode.algorithm.q2300;

import java.util.Arrays;

/**
 * 给你两个整数 num 和 k ，考虑具有以下属性的正整数多重集：
 * 1、每个整数个位数字都是 k 。
 * 2、所有整数之和是 num 。
 * 返回该多重集的最小大小，如果不存在这样的多重集，返回 -1 。
 * 注意：
 * 1、多重集与集合类似，但多重集可以包含多个同一整数，空多重集的和为 0 。
 * 2、个位数字 是数字最右边的数位。
 * 提示：
 * 1、0 <= num <= 3000
 * 2、0 <= k <= 9
 * 链接：https://leetcode.cn/problems/sum-of-numbers-with-units-digit-k
 */
public class Q2310 {

    public static void main(String[] args) {
        // -1
        System.out.println(new Q2310().minimumNumbers(4, 0));
        // -1
        System.out.println(new Q2310().minimumNumbers(2, 9));
        // 2
        System.out.println(new Q2310().minimumNumbers(58, 9));
        // -1
        System.out.println(new Q2310().minimumNumbers(37, 2));
        // 0
        System.out.println(new Q2310().minimumNumbers(0, 7));
    }

    int INF = Integer.MAX_VALUE / 2;

    public int minimumNumbers(int num, int k) {
        int[] cnt = new int[num + 1];
        Arrays.fill(cnt, INF);
        int ret = func(cnt, num, k);
        if (INF == ret) ret = -1;
        return ret;
    }

    int func(int[] cnt, int num, int k) {
        if (cnt[num] != INF) return cnt[num];
        if (num == 0) return 0;
        if (k > num) return INF;
        int v = num % 10, next10;
        if (v >= k) next10 = (num / 10);
        else next10 = (num / 10 - 1);
        int ret = INF, limit = k == 0 ? 1 : 0;
        for (int i = next10; i >= limit; i--) {
            int nextNum = i * 10 + k;
            int next = func(cnt, num - nextNum, k);
            if (next != -1) ret = Math.min(ret, next + 1);
        }
        if (INF == ret) ret = -1;
        cnt[num] = ret;
        return ret;
    }
}
