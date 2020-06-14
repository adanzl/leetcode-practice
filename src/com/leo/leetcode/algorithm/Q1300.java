package com.leo.leetcode.algorithm;

import java.util.Arrays;

public class Q1300 {

    public static void main(String[] args) {
        System.out.println(new Q1300().findBestValue(new int[]{2, 3, 5}, 11)); // 5
        System.out.println(new Q1300().findBestValue(new int[]{1547, 83230, 57084, 93444, 70879}, 71237)); // 17422
        System.out.println(new Q1300().findBestValue(new int[]{2, 3, 5}, 10)); // 5
        System.out.println(new Q1300().findBestValue(new int[]{60864, 25176, 27249, 21296, 20204}, 56803)); // 11361
        System.out.println(new Q1300().findBestValue(new int[]{4, 9, 3}, 10)); // 3
    }

    public int findBestValue(int[] arr, int target) {
        Arrays.sort(arr);
        int average;
        for (int i = 0; i < arr.length; i++) {
            average = (int) Math.round((double) target / (arr.length - i) - 0.0001);
            if (average <= arr[i]) return average;
            if (target < arr[i]) return target;
            target -= arr[i];
        }
        return arr[arr.length - 1];
    }
}
