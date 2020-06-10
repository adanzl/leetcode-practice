package com.leo.leetcode.algorithm;

import java.util.Stack;

import org.junit.Test;

public class Q155 {
    @Test
    public void TestOJ() {
        MinStack minStack = new MinStack();
//        minStack.push(-2);
//        minStack.push(0);
//        minStack.push(-1);
//        System.out.println(minStack.getMin());   //  -2
//        System.out.println(minStack.top());      //  -1
//        minStack.pop();
//        System.out.println(minStack.getMin());   //  -2
        // ==================
//        minStack.push(-2);
//        minStack.push(0);
//        minStack.push(-3);
//        System.out.println(minStack.getMin());   //  -3
//        minStack.pop();
//        System.out.println(minStack.top());      //  0
//        System.out.println(minStack.getMin());   //  -2
        // ==================
        minStack.push(0);
        minStack.push(1);
        minStack.push(0);
        System.out.println(minStack.getMin());   //  0
        minStack.pop();
        System.out.println(minStack.getMin());   //  0

    }

    class MinStack {

        private int minValue = Integer.MAX_VALUE;
        private Stack<Integer> s;

        public MinStack() {
            s = new Stack<>();
        }

        public void push(int x) {
            if (x <= this.minValue) {
                s.push(this.minValue);
                this.minValue = x;
            }
            s.push(x);
        }

        public void pop() {
            if (s.peek() == this.minValue) {
                s.pop();
                this.minValue = s.pop();
            } else {
                s.pop();
            }
        }

        public int top() {
            return s.peek();
        }

        public int getMin() {
            return this.minValue;
        }
    }


}
