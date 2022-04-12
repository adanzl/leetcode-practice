package com.leo.leetcode.algorithm.q0900;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

/**
 * 设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。
 * 实现 TimeMap 类：
 * 1、TimeMap() 初始化数据结构对象
 * 2、void set(String key, String value, int timestamp) 存储键 key、值 value，以及给定的时间戳 timestamp。
 * 3、String get(String key, int timestamp)
 * 1）返回先前调用 set(key, value, timestamp_prev) 所存储的值，其中 timestamp_prev <= timestamp 。
 * 2）如果有多个这样的值，则返回对应最大的  timestamp_prev 的那个值。
 * 3）如果没有值，则返回空字符串（""）。
 * 提示：
 * 1、1 <= key.length, value.length <= 100
 * 2、key 和 value 由小写英文字母和数字组成
 * 3、1 <= timestamp <= 10^7
 * 4、set 操作中的时间戳 timestamp 都是严格递增的
 * 5、最多调用 set 和 get 操作 2 * 10^5 次
 * 链接：https://leetcode-cn.com/problems/time-based-key-value-store
 */
public class Q981 {

    public static void main(String[] args) {
        TimeMap timeMap = new TimeMap();
        timeMap.set("foo", "bar", 1);          // 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1
        System.out.println(timeMap.get("foo", 1));   // 返回 "bar"
        System.out.println(timeMap.get("foo", 3));   // 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 。
        timeMap.set("foo", "bar2", 4);         // 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4
        System.out.println(timeMap.get("foo", 4));   // 返回 "bar2"
        System.out.println(timeMap.get("foo", 5));   // 返回 "bar2"
    }

    static class TimeMap {
        Map<String, TreeMap<Integer, String>> dataMap;

        public TimeMap() {
            dataMap = new HashMap<>();
        }

        public void set(String key, String value, int timestamp) {
            dataMap.putIfAbsent(key, new TreeMap<>());
            dataMap.get(key).put(timestamp, value);
        }

        public String get(String key, int timestamp) {
            if (!dataMap.containsKey(key)) return "";
            TreeMap<Integer, String> treeMap = dataMap.get(key);
            Integer floor = treeMap.floorKey(timestamp);
            if (floor == null) return "";
            return treeMap.get(floor);
        }
    }
}
