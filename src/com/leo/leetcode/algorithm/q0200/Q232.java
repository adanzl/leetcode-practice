package com.leo.leetcode.algorithm.q0200;

import java.util.Stack;

/**
 * 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：
 * <p>
 * 实现 MyQueue 类：
 * 1、void push(int x) 将元素 x 推到队列的末尾
 * 2、int pop() 从队列的开头移除并返回元素
 * 3、int peek() 返回队列开头的元素
 * 4、boolean empty() 如果队列为空，返回 true ；否则，返回 false
 * <p>
 * 说明：
 * 1、你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
 * 2、你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
 * <p>
 * 进阶：
 * 你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
 * <p>
 * 提示：
 * 1、1 <= x <= 9
 * 2、最多调用 100 次 push、pop、peek 和 empty
 * 3、假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）
 * <p>
 * 链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
 */
public class Q232 {

    public static void main(String[] args) {
        MyQueue obj;
        obj = new MyQueue();
        obj.push(1);
        obj.push(2);
        System.out.println(obj.peek()); // 1
        System.out.println(obj.pop()); // 1
        System.out.println(obj.empty()); // false
    }

    static class MyQueue {

        Stack<Integer> s1;
        Stack<Integer> s2;

        public MyQueue() {
            s1 = new Stack<>();
            s2 = new Stack<>();
        }

        /**
         * Push element x to the back of queue.
         */
        public void push(int x) {
            s1.push(x);
        }

        /**
         * Removes the element from in front of queue and returns that element.
         */
        public int pop() {
            if (s2.empty()) while (!s1.empty()) s2.push(s1.pop());
            return s2.pop();
        }

        /**
         * Get the front element.
         */
        public int peek() {
            if (s2.empty()) while (!s1.empty()) s2.push(s1.pop());
            return s2.peek();
        }

        /**
         * Returns whether the queue is empty.
         */
        public boolean empty() {
            return s1.empty() && s2.empty();
        }
    }

}
