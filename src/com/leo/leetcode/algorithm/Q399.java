package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

import java.util.*;

public class Q399 {
    public void TestOJ() {
        System.out.println(Arrays.toString(calcEquation(
                LCUtil.stringToListListString("[[\"a\",\"b\"],[\"b\",\"c\"]]"),
                LCUtil.stringToDoubleArray("[2.0,3.0]"),
                LCUtil.stringToListListString("[[\"a\",\"c\"],[\"b\",\"a\"],[\"a\",\"e\"],[\"a\",\"a\"],[\"x\",\"x\"]]") // [6.0, 0.5, -1.0, 1.0, -1.0 ]
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
