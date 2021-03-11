package com.leo.leetcode.algorithm.q0300;

import java.util.*;

import static com.leo.utils.LCUtil.stringToDoubleArray;
import static com.leo.utils.LCUtil.stringToListListString;

/**
 * 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。
 * 每个 Ai 或 Bi 是一个表示单个变量的字符串。
 * 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。
 * 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。
 * 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。
 * <p>
 * 提示：
 * 1、1 <= equations.length <= 20
 * 2、equations[i].length == 2
 * 3、1 <= Ai.length, Bi.length <= 5
 * 4、values.length == equations.length
 * 5、0.0 < values[i] <= 20.0
 * 6、1 <= queries.length <= 20
 * 7、queries[i].length == 2
 * 8、1 <= Cj.length, Dj.length <= 5
 * 9、Ai, Bi, Cj, Dj 由小写英文字母与数字组成
 * <p>
 * 链接：https://leetcode-cn.com/problems/evaluate-division
 */
public class Q399 {

    public static void main(String[] args) {
        // [6.0, 0.5, -1.0, 1.0, -1.0 ]
        System.out.println(Arrays.toString(new Q399().calcEquation(
                stringToListListString("[[\"a\",\"b\"],[\"b\",\"c\"]]"),
                stringToDoubleArray("[2.0,3.0]"),
                stringToListListString("[[\"a\",\"c\"],[\"b\",\"a\"],[\"a\",\"e\"],[\"a\",\"a\"],[\"x\",\"x\"]]")
        )));
    }

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        // build map
        Map<String, List<String>> map = new HashMap<>();
        Map<String, Double> mValues = new HashMap<>();
        int index = 0;
        for (List<String> l : equations) {
            if (!map.containsKey(l.get(0))) {
                List<String> nL = new ArrayList<>();
                map.put(l.get(0), nL);
                mValues.put(l.get(0) + l.get(0), 1.0);
            }
            if (!map.containsKey(l.get(1))) {
                List<String> nL = new ArrayList<>();
                map.put(l.get(1), nL);
                mValues.put(l.get(1) + l.get(1), 1.0);
            }
            map.get(l.get(0)).add(l.get(1));
            map.get(l.get(1)).add(l.get(0));
            // build values
            mValues.put(l.get(0) + l.get(1), values[index]);
            mValues.put(l.get(1) + l.get(0), 1.0f / values[index]);
            index++;
        }
        double[] out = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            List<String> way = findAWay(map, new String[]{
                    queries.get(i).get(0), queries.get(i).get((1))
            }, new HashSet<>());
            if (way.isEmpty()) {
                out[i] = -1;
                continue;
            }
            double va = 1.0f;
            for (String v : way) {
                va *= mValues.get(v);
            }
            out[i] = va;
        }
        return out;
    }

    List<String> findAWay(Map<String, List<String>> map, String[] query, Set<String> mark) {
        if (!map.containsKey(query[0]) || !map.containsKey(query[1])) {
            return new ArrayList<>();
        }
        List<String> out = new ArrayList<>();
        if (query[0].equals(query[1])) {
            out.add(query[0] + query[1]);
            return out;
        }
        List<String> subValues = map.get(query[0]);
        for (String next : subValues) {
            if (next.equals(query[1])) {
                out.add(query[0] + next);
                return out;
            }
            String markKey = query[0] + next;
            if (mark.contains(markKey)) {
                continue;
            }
            mark.add(markKey);
            out = findAWay(map, new String[]{next, query[1]}, mark);
            if (!out.isEmpty()) {
                out.add(0, query[0] + next);
                return out;
            }
            mark.remove(markKey);
        }
        return new ArrayList<>();
    }
}
