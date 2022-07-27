package com.leo.leetcode.algorithm.q2300;

import com.leo.utils.Executor;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;

/**
 * 设计一个数字容器系统，可以实现以下功能：
 * 1、在系统中给定下标处 插入 或者 替换 一个数字。
 * 2、返回 系统中给定数字的最小下标。
 * 请你实现一个 NumberContainers 类：
 * 1、NumberContainers() 初始化数字容器系统。
 * 2、void change(int index, int number) 在下标 index 处填入 number 。如果该下标 index 处已经有数字了，那么用 number 替换该数字。
 * 3、int find(int number) 返回给定数字 number 在系统中的最小下标。如果系统中没有 number ，那么返回 -1 。
 * 提示：
 * 1、1 <= index, number <= 10^9
 * 2、调用 change 和 find 的 总次数 不超过 10^5 次。
 * 链接：https://leetcode.cn/problems/design-a-number-container-system
 */
public class Q2349 {

    public static void main(String[] args) {
        NumberContainers nc = new NumberContainers();
        // -1
        System.out.println(nc.find(10)); // 没有数字 10 ，所以返回 -1 。
        nc.change(2, 10); // 容器中下标为 2 处填入数字 10 。
        nc.change(1, 10); // 容器中下标为 1 处填入数字 10 。
        nc.change(3, 10); // 容器中下标为 3 处填入数字 10 。
        nc.change(5, 10); // 容器中下标为 5 处填入数字 10 。
        // 1
        System.out.println(nc.find(10)); // 数字 10 所在的下标为 1 ，2 ，3 和 5 。因为最小下标为 1 ，所以返回 1 。
        nc.change(1, 20); // 容器中下标为 1 处填入数字 20 。注意，下标 1 处之前为 10 ，现在被替换为 20 。
        // 2
        System.out.println(nc.find(10)); // 数字 10 所在下标为 2 ，3 和 5 。最小下标为 2 ，所以返回 2 。

        new Executor(Q2349.class).execute(
                "[\"NumberContainers\",\"find\",\"change\",\"change\",\"change\",\"change\",\"find\",\"change\",\"find\"]",
                "[[],[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]]");
    }

    static class NumberContainers {

        Map<Integer, TreeSet<Integer>> map = new HashMap<>();
        Map<Integer, Integer> records = new HashMap<>();

        public void change(int index, int number) {
            map.putIfAbsent(number, new TreeSet<>());
            if (records.containsKey(index)) {
                int num = records.get(index);
                map.get(num).remove(index);
            }
            map.get(number).add(index);
            records.put(index, number);
        }

        public int find(int number) {
            map.putIfAbsent(number, new TreeSet<>());
            if (map.get(number).isEmpty()) return -1;
            return map.get(number).first();
        }
    }
}
