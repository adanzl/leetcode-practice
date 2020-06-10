package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;

public class Q22 {
    public List<String> generateParenthesis(int n) {
        List<String> ret = new ArrayList<>();
        buildList(ret, "", n, n);
        return ret;
    }

    void buildList(List<String> out, String str, int L, int R) {
        if (L == 0 && R == 0) {
            out.add(str);
            return;
        }
        if (L > 0) {
            buildList(out, str + "(", L - 1, R);
        }
        if (R > 0 && R - 1 >= L) {
            buildList(out, str + ")", L, R - 1);
        }
    }
}
