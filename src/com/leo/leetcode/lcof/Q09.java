package com.leo.leetcode.lcof;

import java.util.Stack;

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
