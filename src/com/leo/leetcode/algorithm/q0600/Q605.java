package com.leo.leetcode.algorithm.q0600;

public class Q605 {

    public static void main(String[] args) {
        System.out.println(new Q605().canPlaceFlowers(new int[] { 0, 0 }, 1)); // T
        System.out.println(new Q605().canPlaceFlowers(new int[] { 0, 1, 0 }, 1)); // F
        System.out.println(new Q605().canPlaceFlowers(new int[] { 0, 0, 1, 0, 1 }, 1)); // T
        System.out.println(new Q605().canPlaceFlowers(new int[] { 1, 0, 0, 0, 1 }, 1)); // T
        System.out.println(new Q605().canPlaceFlowers(new int[] { 1, 0, 0, 0, 1 }, 2)); // F
        System.out.println(new Q605().canPlaceFlowers(new int[] { 1 }, 1)); // F
        System.out.println(new Q605().canPlaceFlowers(new int[] { 0 }, 1)); // T
    }

    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) return true;
        if (flowerbed.length == 1) return (flowerbed[0] == 0 && n == 1);
        if (flowerbed.length == 2) return (flowerbed[0] == 0 && flowerbed[1] == 0 && n == 1);
        int[] flags = new int[flowerbed.length];
        if (flowerbed[0] == 0 && flowerbed[1] == 0) {
            flags[0] = 1;
            flags[1] = 1;
        }
        for (int i = 2; i < flowerbed.length; i++) {
            if (flowerbed[i - 1] == 0 && flowerbed[i] == 0 && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
                flags[i] = Math.max(flags[i - 2] + 1, flags[i - 1]);
            } else {
                flags[i] = flags[i - 1];
            }
        }
        return flags[flags.length - 1] >= n;
    }
}
