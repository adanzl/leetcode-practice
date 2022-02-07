package com.leo.leetcode.algorithm.q0800;

import java.util.Arrays;

/**
 * 爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 根糖果棒的大小，B[j] 是鲍勃拥有的第 j 根糖果棒的大小。
 * 因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
 * 返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。
 * 如果有多个答案，你可以返回其中任何一个。保证答案存在。
 * <p>
 * 提示：
 * 1、1 <= A.length <= 10000
 * 2、1 <= B.length <= 10000
 * 3、1 <= A[i] <= 100000
 * 4、1 <= B[i] <= 100000
 * 5、保证爱丽丝与鲍勃的糖果总量不同。
 * 6、答案肯定存在。
 * <p>
 * 链接：https://leetcode-cn.com/problems/fair-candy-swap
 */
public class Q888 {

    public static void main(String[] args) {
        // [26,11]
        System.out.println(Arrays.toString(new Q888().fairCandySwap(new int[]{1, 17, 14, 1, 16}, new int[]{26, 11})));
        // [1,2]
        System.out.println(Arrays.toString(new Q888().fairCandySwap(new int[]{1, 1}, new int[]{2, 2})));
        // [1,2]
        System.out.println(Arrays.toString(new Q888().fairCandySwap(new int[]{1, 2}, new int[]{2, 3})));
        // [2,3]
        System.out.println(Arrays.toString(new Q888().fairCandySwap(new int[]{2}, new int[]{1, 3})));
        // [5,4]
        System.out.println(Arrays.toString(new Q888().fairCandySwap(new int[]{1, 2, 5}, new int[]{2, 4})));
    }

    public int[] fairCandySwap(int[] A, int[] B) {
        int sum = 0;
        boolean[] flag = new boolean[100001];
        for (int n : A) sum += n;
        for (int n : B) {
            sum -= n;
            flag[n] = true;
        }
        sum /= 2;
        for (int a : A) {
            int diff = a - sum;
            if (diff >= 0 && diff < flag.length && flag[diff]) return new int[]{a, a - sum};
        }
        return new int[]{0, 0};
    }
}
