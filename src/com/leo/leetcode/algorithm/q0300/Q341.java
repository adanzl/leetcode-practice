package com.leo.leetcode.algorithm.q0300;

import com.eclipsesource.json.Json;
import com.eclipsesource.json.JsonArray;
import com.eclipsesource.json.JsonValue;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;


/**
 * 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
 * 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
 * <p>
 * 链接：https://leetcode-cn.com/problems/flatten-nested-list-iterator
 */
public class Q341 {

    public static void main(String[] args) {
        NestedIterator obj = new NestedIterator(stringToNestedIntegerList("[[1,1],2,[1,1]]"));
        while (obj.hasNext()) System.out.println(obj.next());
    }

    public interface NestedInteger {
        // @return true if this NestedInteger holds a single integer, rather than a nested list.
        boolean isInteger();

        // @return the single integer that this NestedInteger holds, if it holds a single integer
        // Return null if this NestedInteger holds a nested list
        Integer getInteger();

        // @return the nested list that this NestedInteger holds, if it holds a nested list
        // Return null if this NestedInteger holds a single integer
        List<NestedInteger> getList();
    }

    static class NestedIterator implements Iterator<Integer> {
        private LNode it;
        private LNode p;

        public NestedIterator(List<NestedInteger> nestedList) {
            it = new LNode(null);
            p = it;
            build(nestedList);
            it = it.next;
        }

        void build(List<NestedInteger> nestedList) {
            for (NestedInteger ni : nestedList) {
                if (ni.isInteger()) {
                    LNode node = new LNode(ni);
                    p.next = node;
                    p = node;
                } else {
                    build(ni.getList());
                }
            }
        }

        @Override
        public Integer next() {
            int v = it.data.getInteger();
            it = it.next;
            return v;
        }

        @Override
        public boolean hasNext() {
            return it != null;
        }

        static class LNode {
            LNode next;
            NestedInteger data;

            LNode(NestedInteger data) {
                this.data = data;
            }
        }
    }

    static class IInteger implements NestedInteger {

        private final int value;

        IInteger(int v) {
            this.value = v;
        }

        @Override
        public boolean isInteger() {
            return true;
        }

        @Override
        public Integer getInteger() {
            return value;
        }

        @Override
        public List<NestedInteger> getList() {
            return null;
        }
    }

    static class LInteger implements NestedInteger {

        private final List<NestedInteger> list;

        LInteger(String v) {
            this.list = stringToNestedIntegerList(v);
        }

        @Override
        public boolean isInteger() {
            return false;
        }

        @Override
        public Integer getInteger() {
            return null;
        }

        @Override
        public List<NestedInteger> getList() {
            return list;
        }
    }

    static List<NestedInteger> stringToNestedIntegerList(String input) {
        JsonArray jsonArray = Json.parse(input).asArray();
        List<NestedInteger> ret = new ArrayList<>();
        for (int i = 0; i < jsonArray.size(); i++) {
            JsonValue jd = jsonArray.get(i);
            if (jd.isArray()) ret.add(new LInteger(jd.toString()));
            else ret.add(new IInteger(jd.asInt()));
        }
        return ret;
    }
}
