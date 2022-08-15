package com.leo.leetcode.algorithm.q1600;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 有 n 个 (id, value) 对，其中 id 是 1 到 n 之间的一个整数，value 是一个字符串。不存在 id 相同的两个 (id, value) 对。
 * 设计一个流，以 任意 顺序获取 n 个 (id, value) 对，并在多次调用时 按 id 递增的顺序 返回一些值。
 * 实现 OrderedStream 类：
 * OrderedStream(int n) 构造一个能接收 n 个值的流，并将当前指针 ptr 设为 1 。
 * String[] insert(int id, String value) 向流中存储新的 (id, value) 对。存储后：
 * 如果流存储有 id = ptr 的 (id, value) 对，则找出从 id = ptr 开始的 最长 id 连续递增序列 ，并 按顺序 返回与这些 id 关联的值的列表。然后，将 ptr 更新为最后那个  id + 1 。
 * 否则，返回一个空列表。
 * 提示：
 * 1、1 <= n <= 1000
 * 2、1 <= id <= n
 * 3、value.length == 5
 * 4、value 仅由小写字母组成
 * 5、每次调用 insert 都会使用一个唯一的 id
 * 6、恰好调用 n 次 insert
 * 链接：https://leetcode.cn/problems/design-an-ordered-stream
 */
public class Q1656 {

    public static void main(String[] args) {
        OrderedStream os = new OrderedStream(5);
        System.out.println(os.insert(3, "ccccc")); // 插入 (3, "ccccc")，返回 []
        System.out.println(os.insert(1, "aaaaa")); // 插入 (1, "aaaaa")，返回 ["aaaaa"]
        System.out.println(os.insert(2, "bbbbb")); // 插入 (2, "bbbbb")，返回 ["bbbbb", "ccccc"]
        System.out.println(os.insert(5, "eeeee")); // 插入 (5, "eeeee")，返回 []
        System.out.println(os.insert(4, "ddddd")); // 插入 (4, "ddddd")，返回 ["ddddd", "eeeee"]
    }

    static class OrderedStream {
        Map<Integer, String> map;
        int ptr = 1;

        public OrderedStream(int n) {
            map = new HashMap<>(n);
        }

        public List<String> insert(int idKey, String value) {
            List<String> result = new ArrayList<>();
            map.put(idKey, value);
            if (!map.containsKey(ptr)) return result;
            for (int i = idKey; map.containsKey(i); i++) {
                result.add(map.get(i));
                ptr++;
            }
            return result;
        }
    }

}
