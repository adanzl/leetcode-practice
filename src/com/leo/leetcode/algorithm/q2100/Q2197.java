package com.leo.leetcode.algorithm.q2100;

import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 。请你对数组执行下述操作：
 * 1、从 nums 中找出 任意 两个 相邻 的 非互质 数。
 * 2、如果不存在这样的数，终止 这一过程。
 * 3、否则，删除这两个数，并 替换 为它们的 最小公倍数（Least Common Multiple，LCM）。
 * 4、只要还能找出两个相邻的非互质数就继续 重复 这一过程。
 * 返回修改后得到的 最终 数组。可以证明的是，以 任意 顺序替换相邻的非互质数都可以得到相同的结果。
 * 生成的测试用例可以保证最终数组中的值 小于或者等于 108 。
 * 两个数字 x 和 y 满足 非互质数 的条件是：GCD(x, y) > 1 ，其中 GCD(x, y) 是 x 和 y 的 最大公约数 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 3、生成的测试用例可以保证最终数组中的值 小于或者等于 10^8。
 * 链接：https://leetcode.cn/problems/replace-non-coprime-numbers-in-array
 */
public class Q2197 {

    public static void main(String[] args) {
        // [2009,20677,825]
        System.out.println(new Q2197().replaceNonCoPrimes(stringToIntegerArray("[287,41,49,287,899,23,23,20677,5,825]")));
        // [31,97561]
        System.out.println(new Q2197().replaceNonCoPrimes(stringToIntegerArray("[31,97561,97561,97561,97561,97561,97561,97561,97561]")));
        // [12,7,6]
        System.out.println(new Q2197().replaceNonCoPrimes(stringToIntegerArray("[6,4,3,2,7,6,2]")));
        // [2,1,1,3]
        System.out.println(new Q2197().replaceNonCoPrimes(stringToIntegerArray("[2,2,1,1,3,3,3]")));
    }

    public List<Integer> replaceNonCoPrimes(int[] nums) {
        Stack<Integer> stack = new Stack<>();
        for (int num : nums) {
            if (!stack.isEmpty()) {
                while (!stack.isEmpty()) {
                    int g = gcd(stack.peek(), num);
                    if (g > 1) num = stack.pop() / g * num;
                    else break;
                }
            }
            stack.push(num);
        }
        return new LinkedList<>(stack);
    }

    // 最大公约数
    int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    // 最小公倍数
    int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }
}
