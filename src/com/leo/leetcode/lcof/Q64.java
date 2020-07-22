package com.leo.leetcode.lcof;

public class Q64 {
    public static void main(String[] args) {
        System.out.println(new Q64().sumNums(3)); // 6
        System.out.println(new Q64().sumNums(9)); // 45
    }

    int sumNums(int n) {
        int ans = n;
        boolean b = (ans > 0 && (ans += sumNums(n - 1)) > 0);
        System.out.println(b);
        return ans; // 短路特性，&&前面为假，后面不计算
    }
}
