package com.leo.leetcode.algorithm.q0700;

import java.util.ArrayList;
import java.util.List;

/**
 * 自除数 是指可以被它包含的每一位数整除的数。
 * 例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
 * 自除数 不允许包含 0 。
 * 给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right] 内所有的 自除数 。
 * 提示：1 <= left <= right <= 10^4
 * 链接：https://leetcode-cn.com/problems/self-dividing-numbers
 */
public class Q728 {

    public static void main(String[] args) {
        // [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        System.out.println(new Q728().selfDividingNumbers(1, 22));
        // [48,55,66,77]
        System.out.println(new Q728().selfDividingNumbers(47, 85));
    }

    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> ans = new ArrayList<>();
        for (int i = left; i <= right; i++) {
            if (isSelfDividing(i)) ans.add(i);
        }
        return ans;
    }

    public boolean isSelfDividing(int num) {
        int temp = num;
        while (temp > 0) {
            int digit = temp % 10;
            if (digit == 0 || num % digit != 0) return false;
            temp /= 10;
        }
        return true;
    }
}
