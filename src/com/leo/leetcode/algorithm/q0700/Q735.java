package com.leo.leetcode.algorithm.q0700;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数数组 asteroids，表示在同一行的行星。
 * 对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
 * 找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
 * 提示：
 * 1、2 <= asteroids.length <= 10^4
 * 2、-1000 <= asteroids[i] <= 1000
 * 3、asteroids[i] != 0
 * 链接：https://leetcode.cn/problems/asteroid-collision
 */
public class Q735 {

    public static void main(String[] args) {
        // [-2,-2,-2]
        System.out.println(Arrays.toString(new Q735().asteroidCollision(stringToIntegerArray("[-2,-2,1,-2]"))));
        // [5,10]
        System.out.println(Arrays.toString(new Q735().asteroidCollision(stringToIntegerArray("[5,10,-5]"))));
        // []
        System.out.println(Arrays.toString(new Q735().asteroidCollision(stringToIntegerArray("[8,-8]"))));
        // [10]
        System.out.println(Arrays.toString(new Q735().asteroidCollision(stringToIntegerArray("[10,2,-5]"))));

    }

    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack = new ArrayDeque<>(); // 代替Stack
        for (int asteroid : asteroids) {
            while (!stack.isEmpty() && stack.peek() > 0 && asteroid < 0) {
                int v = stack.pop();
                if (Math.abs(v) > Math.abs(asteroid)) {
                    asteroid = 0;
                    stack.push(v);
                } else if (Math.abs(v) == Math.abs(asteroid)) {
                    asteroid = 0;
                }
            }
            if (asteroid != 0) stack.push(asteroid);
        }
        int[] ret = new int[stack.size()];
        for (int i = ret.length - 1; i >= 0; i--) ret[i] = stack.pop();
        return ret;
    }
}
