package com.leo.leetcode.lcof;

import java.util.Stack;

/**
 * 用两个栈实现一个队列。
 * 队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。
 * (若队列中没有元素，deleteHead 操作返回 -1 )
 * 链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
 */
public class Q09 {

    public static void main(String[] args) {
        CQueue obj = new CQueue();
        obj.appendTail(3);
        System.out.println(obj.deleteHead()); // 3
        System.out.println(obj.deleteHead()); // -1

        obj = new CQueue();
        System.out.println(obj.deleteHead()); // -1
        obj.appendTail(5);
        obj.appendTail(2);
        System.out.println(obj.deleteHead()); // 5
        System.out.println(obj.deleteHead()); // 2
    }

    static class CQueue {
        Stack<Integer> s1;
        Stack<Integer> s2;

        public CQueue() {
            s1 = new Stack<>();
            s2 = new Stack<>();
        }

        public void appendTail(int value) {
            s1.push(value);
        }

        public int deleteHead() {
            if (!s2.empty()) {
                return s2.pop();
            }
            if (s1.empty()) return -1;
            while (!s1.empty()) s2.push(s1.pop());
            return s2.pop();
        }
    }
}
