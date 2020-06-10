package com.leo.leetcode.offer;

import com.leo.utils.LCUtil;

public class Q33 {

    public static void main(String[] args) {
        new Q33().TestOJ();
    }

    public void TestOJ() {
        System.out.println(verifyPostOrder(LCUtil.stringToIntegerArray("[4, 8, 6, 12, 16, 14, 10]"))); // false
        System.out.println(verifyPostOrder(LCUtil.stringToIntegerArray("[7,4,6,5]"))); // false
    }

    public boolean verifyPostOrder(int[] postOrder) {
        return verify(postOrder, 0, postOrder.length);
    }

    boolean verify(int[] order, int s, int e) {
        if (e - s <= 1) return true;
        int root = order[e - 1];
        int p = s;
        while (order[p] < root) p++;
        for (int i = p; i < e; i++) {
            if (order[i] < root) return false;
        }
        return verify(order, s, p) && verify(order, p, e - 1);
    }
}
