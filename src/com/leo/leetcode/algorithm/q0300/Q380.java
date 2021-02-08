package com.leo.leetcode.algorithm.q0300;

import java.util.*;

/**
 * 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
 * <p>
 * 1、insert(val)：当元素 val 不存在时，向集合中插入该项。
 * 2、remove(val)：元素 val 存在时，从集合中移除该项。
 * 3、getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
 * <p>
 * 链接：https://leetcode-cn.com/problems/insert-delete-getrandom-o1
 */
public class Q380 {

    public static void main(String[] args) {
        RandomizedSet obj = new RandomizedSet();
        System.out.println(obj.insert(0)); // true
        System.out.println(obj.insert(1)); // true
        System.out.println(obj.remove(0)); // true
        System.out.println(obj.insert(2)); // true
        System.out.println(obj.remove(1)); // true
        System.out.println(obj.getRandom()); // 2
        obj = new RandomizedSet();
        System.out.println(obj.insert(1)); // true
        System.out.println(obj.remove(2)); // false
        System.out.println(obj.insert(2)); // true
        System.out.println(obj.getRandom()); // 1 or 2
        System.out.println(obj.remove(1)); // true
        System.out.println(obj.insert(2)); // false
        System.out.println(obj.getRandom()); // 2
    }

    static class RandomizedSet {

        private final Map<Integer, Integer> map;
        private int index = 0;
        List<Integer> arr;
        Random random = new Random();

        public RandomizedSet() {
            map = new HashMap<>();
            arr = new ArrayList<>();
        }

        public boolean insert(int val) {
            if (map.containsKey(val)) return false;
            map.put(val, index);
            arr.add(val);
            index++;
            return true;
        }

        public boolean remove(int val) {
            int idx = map.getOrDefault(val, -1);
            if (idx == -1) return false;
            int tailValue = arr.get(arr.size() - 1);
            arr.set(idx, tailValue);
            map.put(tailValue, idx);
            arr.remove(arr.size() - 1);
            index--;
            map.remove(val);
            return true;
        }

        public int getRandom() {
            return arr.get(random.nextInt(index));
        }
    }
}
