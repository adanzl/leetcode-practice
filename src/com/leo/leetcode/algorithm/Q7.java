package com.leo.leetcode.algorithm;

public class Q7 {
    public int reverse(int x) {
        int ret = 0;
        while (x != 0) {
            int ext = x % 10;
            if (ext > 0 && ret > (Integer.MAX_VALUE - ext) / 10 || (ext < 0 && ret < (Integer.MIN_VALUE - ext) / 10)) {
                return 0;
            }
            ret = ret * 10 + ext;
            x /= 10;
        }
        return ret;
    }
}
