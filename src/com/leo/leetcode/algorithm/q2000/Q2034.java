package com.leo.leetcode.algorithm.q2000;

import java.util.*;

/**
 * 给你一支股票价格的数据流。数据流中每一条记录包含一个 时间戳 和该时间点股票对应的 价格 。
 * 不巧的是，由于股票市场内在的波动性，股票价格记录可能不是按时间顺序到来的。
 * 某些情况下，有的记录可能是错的。如果两个有相同时间戳的记录出现在数据流中，前一条记录视为错误记录，后出现的记录 更正 前一条错误的记录。
 * 请你设计一个算法，实现：
 * 1、更新 股票在某一时间戳的股票价格，如果有之前同一时间戳的价格，这一操作将 更正 之前的错误价格。
 * 2、找到当前记录里 最新股票价格 。最新股票价格 定义为时间戳最晚的股票价格。
 * 3、找到当前记录里股票的 最高价格 。
 * 4、找到当前记录里股票的 最低价格 。
 * 请你实现 StockPrice 类：
 * 1、StockPrice() 初始化对象，当前无股票价格记录。
 * 2、void update(int timestamp, int price) 在时间点 timestamp 更新股票价格为 price 。
 * 3、int current() 返回股票 最新价格 。
 * 4、int maximum() 返回股票 最高价格 。
 * 5、int minimum() 返回股票 最低价格 。
 * <p>
 * 提示：
 * 1、1 <= timestamp, price <= 10^9
 * 2、update，current，maximum 和 minimum 总 调用次数不超过 10^5 。
 * 3、current，maximum 和 minimum 被调用时，update 操作 至少 已经被调用过 一次 。
 * <p>
 * 链接：https://leetcode-cn.com/problems/stock-price-fluctuation
 */
public class Q2034 {

    public static void main(String[] args) {
        StockPrice obj = new StockPrice();
        obj.update(1, 10);
        obj.update(2, 5);
        System.out.println(obj.current()); // 5
        System.out.println(obj.maximum()); // 10
        obj.update(1, 3);
        System.out.println(obj.maximum()); // 5
        obj.update(4, 2); // 2
        System.out.println(obj.minimum());
    }

    static class StockPrice {
        private int _current = 0;
        private int lastTs = -1;
        private final TreeMap<Integer, Integer> tree = new TreeMap<>();
        private final Map<Integer, Integer> pMap = new HashMap<>();

        public void update(int timestamp, int price) {
            if (timestamp >= this.lastTs) {
                this.lastTs = timestamp;
                this._current = price;
            }
            if (pMap.containsKey(timestamp)) {
                int prePrice = pMap.get(timestamp);
                int count = tree.get(prePrice);
                if (count == 1) tree.remove(prePrice);
                else tree.put(prePrice, count - 1);

            }
            pMap.put(timestamp, price);
            tree.put(price, tree.getOrDefault(price, 0) + 1);
        }

        public int current() {
            return this._current;
        }

        public int maximum() {
            return tree.lastKey();
        }

        public int minimum() {
            return tree.firstKey();
        }
    }
}
