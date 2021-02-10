package com.leo.leetcode.algorithm.q0700;

import java.util.PriorityQueue;
import java.util.Queue;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
 * 请实现 KthLargest 类：
 * KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
 * int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
 * <p>
 * 提示：
 * 1、1 <= k <= 10^4
 * 2、0 <= nums.length <= 10^4
 * 3、-10^4 <= nums[i] <= 10^4
 * 4、-10^4 <= val <= 10^4
 * 5、最多调用 add 方法 10^4 次
 * 题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素
 * <p>
 * 链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
 */
public class Q703 {

    public static void main(String[] args) {
        KthLargest obj = new KthLargest(3, stringToIntegerArray("[4, 5, 8, 2]"));
        System.out.println(obj.add(3)); // 4
        System.out.println(obj.add(5)); // 5
        System.out.println(obj.add(10)); // 5
        System.out.println(obj.add(9)); // 8
        System.out.println(obj.add(4)); // 8
    }

    static class KthLargest {
        private final int limit;
        private final Queue<Integer> q;

        public KthLargest(int k, int[] nums) {
            this.limit = k;
            this.q = new PriorityQueue<>(k);
            for (int n : nums) add(n);
        }

        public int add(int val) {
            if (q.size() >= limit) {
                if (q.peek() < val) {
                    q.remove();
                    q.add(val);
                }
            } else {
                q.add(val);
            }
            return q.peek();
        }
    }
}
