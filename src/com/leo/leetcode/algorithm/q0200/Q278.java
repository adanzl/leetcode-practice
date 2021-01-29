package com.leo.leetcode.algorithm.q0200;

public class Q278 {

    public static void main(String[] args) {
        Q278 obj = new Q278();
        // 1702766719
        obj.badVersion = 1702766719;
        System.out.println(obj.firstBadVersion(2126753390));
        // 4
        obj.badVersion = 4;
        System.out.println(obj.firstBadVersion(100));
        // 4
        obj.badVersion = 4;
        System.out.println(obj.firstBadVersion(5));
    }

    public int firstBadVersion(int n) {
        int l = 0, r = n;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (isBadVersion(mid + 1)) r = mid;
            else l = mid + 1;
        }
        return l + 1;
    }

    int badVersion = 0;

    boolean isBadVersion(int v) {
        return v >= badVersion;
    }
}
