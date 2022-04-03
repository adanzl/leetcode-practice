package com.leo.leetcode.algorithm.q0900;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。
 * 提示：
 * 1、0 <= arr.length <= 3 * 10^4
 * 2、arr.length 是偶数
 * 3、-10^5 <= arr[i] <= 10^5
 * 链接：https://leetcode-cn.com/problems/array-of-doubled-pairs
 */
public class Q954 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q954().canReorderDoubled(stringToIntegerArray("[-5,-2]")));
        // true
        System.out.println(new Q954().canReorderDoubled(stringToIntegerArray("[4,-2,2,-4]")));
        // false
        System.out.println(new Q954().canReorderDoubled(stringToIntegerArray("[3,1,3,6]")));
        // false
        System.out.println(new Q954().canReorderDoubled(stringToIntegerArray("[2,1,2,6]")));
    }

    public boolean canReorderDoubled(int[] arr) {
        Arrays.sort(arr);
        Map<Integer, Integer> iMap = new HashMap<>();
        for (int num : arr) iMap.put(num, iMap.getOrDefault(num, 0) + 1);
        int count = 0;
        for (int i = 0; i < arr.length && count < arr.length >> 1; i++) {
            int num = arr[i], newNum;
            if (iMap.getOrDefault(num, 0) <= 0) continue;
            iMap.put(num, iMap.get(num) - 1);
            if (num > 0) newNum = num * 2;
            else {
                if ((num & 1) == 1) return false;
                newNum = num / 2;
            }
            if (iMap.getOrDefault(newNum, 0) <= 0) return false;
            iMap.put(newNum, iMap.get(newNum) - 1);
            count++;
        }
        return true;
    }
}
