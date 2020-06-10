package com.leo.leetcode.algorithm;

public class Q202 {
    public static void main(String[] args) {
        System.out.println(new Q202().isHappy(10)); // true
        System.out.println(new Q202().isHappy(19)); // true
        System.out.println(new Q202().isHappy(1)); // true
    }

    public boolean isHappy(int n) {
        int slow = n, fast = nextInt(n);
        while (slow != 1 && fast != 1) {
            fast = nextInt(fast);
            fast = nextInt(fast);
            slow = nextInt(slow);
            if (slow == fast) return false;
        }
        return true;
    }

    int nextInt(int n) {
        int out = 0;
        while (n != 0) {
            int v = n % 10;
            out += v * v;
            n /= 10;
        }
        return out;
    }
}
