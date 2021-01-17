package com.leo.leetcode.algorithm.q0200;

import java.util.HashMap;
import java.util.Map;

/**
 * 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
 */
public class Q208 {
    public void TestOJ() {
        Trie trie = new Trie();

        trie.insert("apple");
        System.out.println(trie.search("apple"));   // 返回 true
        System.out.println(trie.search("app"));     // 返回 false
        System.out.println(trie.startsWith("app")); // 返回 true
        trie.insert("app");
        System.out.println(trie.search("app"));     // 返回 true

    }

    class Trie {

        class TNode {
            char c;
            Map<Character, TNode> children;

            TNode(char c) {
                this.c = c;
                this.children = new HashMap<>();
            }

            TNode findChild(char c) {
                return this.children.get(c);
            }
        }

        private TNode head;

        /**
         * Initialize your data structure here.
         */
        public Trie() {
            head = new TNode(' ');
        }

        /**
         * Inserts a word into the trie.
         */
        public void insert(String word) {
            TNode p = this.head;
            for (char c : word.toCharArray()) {
                TNode f = p.findChild(c);
                if (f == null) {
                    f = new TNode(c);
                    p.children.put(c, f);
                }
                p = f;
            }
            p.children.put('\n', new TNode('\n'));
        }

        /**
         * Returns if the word is in the trie.
         */
        public boolean search(String word) {
            TNode p = this.head;
            for (char c : word.toCharArray()) {
                TNode f = p.findChild(c);
                if (f == null) {
                    return false;
                }
                p = f;
            }
            return p.children.get('\n') != null;
        }

        /**
         * Returns if there is any word in the trie that starts with the given prefix.
         */
        public boolean startsWith(String prefix) {
            TNode p = this.head;
            for (char c : prefix.toCharArray()) {
                TNode f = p.findChild(c);
                if (f == null) {
                    return false;
                }
                p = f;
            }
            return true;
        }
    }

}
