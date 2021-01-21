package com.leo.leetcode.algorithm.q0900;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.ArrayList;
import java.util.List;

/**
 * 对于非负整数  X  而言，X  的数组形式是每位数字按从左到右的顺序形成的数组。
 * 例如，如果  X = 1231，那么其数组形式为  [1,2,3,1]。
 * 给定非负整数 X 的数组形式  A，返回整数  X+K  的数组形式。
 * <p>
 * 提示：
 * 1、1 <= A.length <= 10000
 * 2、0 <= A[i] <= 9
 * 3、0 <= K <= 10000
 * 4、如果  A.length > 1，那么  A[0] != 0
 * <p>
 * 链接：https://leetcode-cn.com/problems/add-to-array-form-of-integer
 */

public class Q989 {

    public static void main(String[] args) {
        // [1]
        System.out.println(new Q989().addToArrayForm(stringToIntegerArray("[1]"), 0));
        // [3,4]
        System.out.println(new Q989().addToArrayForm(stringToIntegerArray("[]"), 34));
        // [1,2,3,4]
        System.out.println(new Q989().addToArrayForm(stringToIntegerArray("[1,2,0,0]"), 34));
        // [4,5,5]
        System.out.println(new Q989().addToArrayForm(stringToIntegerArray("[2,7,4]"), 181));
        // [1,0,2,1]
        System.out.println(new Q989().addToArrayForm(stringToIntegerArray("[2,1,5]"), 806));
        // [1,0,0,0,0,0,0,0,0,0,0]
        System.out.println(new Q989().addToArrayForm(stringToIntegerArray("[9,9,9,9,9,9,9,9,9,9]"), 1));
    }

    public List<Integer> addToArrayForm(int[] A, int K) {
        List<Integer> ret = new ArrayList<>();
        for (int i = A.length - 1; i >= 0; i--) {
            K += A[i];
            ret.add(K % 10);
            K /= 10;
        }
        while (K != 0) {
            ret.add(K % 10);
            K /= 10;
        }
        for (int i = 0; i < ret.size() / 2; i++) {
            int v = ret.get(i), li = ret.size() - 1 - i;
            ret.set(i, ret.get(li));
            ret.set(li, v);
        }
        return ret;
    }


}
