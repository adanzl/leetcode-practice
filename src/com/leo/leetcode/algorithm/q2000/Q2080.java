package com.leo.leetcode.algorithm.q2000;

import java.util.HashMap;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率 。
 * 子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。
 * 请你实现 RangeFreqQuery 类：
 * 1、RangeFreqQuery(int[] arr) 用下标从 0 开始的整数数组 arr 构造一个类的实例。
 * 2、int query(int left, int right, int value) 返回子数组 arr[left...right] 中 value 的 频率 。
 * 一个 子数组 指的是数组中一段连续的元素。arr[left...right] 指的是 nums 中包含下标 left 和 right 在内 的中间一段连续元素。
 * 提示：
 * 1、1 <= arr.length <= 10^5
 * 2、1 <= arr[i], value <= 10^4
 * 3、0 <= left <= right < arr.length
 * 4、调用 query 不超过 10^5 次。
 * 链接：https://leetcode-cn.com/problems/range-frequency-queries
 */
public class Q2080 {

    public static void main(String[] args) {
        RangeFreqQuery rangeFreqQuery = new RangeFreqQuery(stringToIntegerArray("[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]"));
        System.out.println(rangeFreqQuery.query(1, 2, 4)); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
        System.out.println(rangeFreqQuery.query(0, 11, 33)); // 返回 2 。33 在整个子数组中出现 2 次。
    }

    static class RangeFreqQuery {
        Node head;

        public RangeFreqQuery(int[] arr) {
            head = new Node(0, arr.length - 1);
            addNode(head, arr);
        }

        Node addNode(Node root, int[] arr) {
            if (root.l == root.r) {
                root.iMap.put(arr[root.l], 1);
                return root;
            }
            int mid = root.l + ((root.r - root.l) >> 1);
            root.left = addNode(new Node(root.l, mid), arr);
            root.right = addNode(new Node(mid + 1, root.r), arr);
            Map<Integer, Integer> iMap = root.iMap;
            for (Map.Entry<Integer, Integer> entry : root.left.iMap.entrySet())
                iMap.put(entry.getKey(), iMap.getOrDefault(entry.getKey(), 0) + entry.getValue());
            for (Map.Entry<Integer, Integer> entry : root.right.iMap.entrySet())
                iMap.put(entry.getKey(), iMap.getOrDefault(entry.getKey(), 0) + entry.getValue());
            return root;
        }

        public int query(int left, int right, int value) {
            return query(head, left, right, value);
        }

        int query(Node root, int l, int r, int value) {
            if (l == root.l && root.r == r) return root.iMap.getOrDefault(value, 0);
            int mid = root.l + ((root.r - root.l) >> 1);
            if (mid + 1 <= l) return query(root.right, l, r, value);
            if (mid >= r) return query(root.left, l, r, value);
            return query(root.left, l, mid, value) + query(root.right, mid + 1, r, value);
        }

        static class Node {
            int l, r;
            Node left, right;
            Map<Integer, Integer> iMap = new HashMap<>();

            Node(int l, int r) {
                this.l = l;
                this.r = r;
            }
        }
    }
}
