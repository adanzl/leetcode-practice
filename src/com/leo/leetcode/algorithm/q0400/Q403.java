package com.leo.leetcode.algorithm.q0400;

import java.util.HashMap;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。
 * 给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。
 * 开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃 1 个单位（即只能从单元格 1 跳至单元格 2 ）。
 * 如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。
 * 提示：
 * 1、2 <= stones.length <= 2000
 * 2、0 <= stones[i] <= 2^31 - 1
 * 3、stones[0] == 0
 * 4、stones 按严格升序排列
 * 链接：https://leetcode.cn/problems/frog-jump
 */
public class Q403 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q403().canCross(stringToIntegerArray("[0,1,2,3,4,8,9,11]")));
        // true
        System.out.println(new Q403().canCross(stringToIntegerArray("[0,1,3,5,6,8,12,17]")));
    }

    public boolean canCross(int[] stones) {
        Map<Integer, Map<Integer, Boolean>> mMap = new HashMap<>();
        for (int stone : stones) mMap.put(stone, new HashMap<>());
        int n = stones.length;
        return func(mMap, stones[0], 0, stones[n - 1]);
    }

    boolean func(Map<Integer, Map<Integer, Boolean>> mMap, int idx, int step, int target) {
        if (idx == target) return true;
        if (idx > target) return false;
        if (!mMap.containsKey(idx)) return false;
        if (!mMap.get(idx).containsKey(step)) {
            boolean v = (step > 0 && func(mMap, idx + step, step, target))
                    || (func(mMap, idx + step + 1, step + 1, target))
                    || (step > 1 && func(mMap, idx + step - 1, step - 1, target));
            mMap.get(idx).put(step, v);
        }
        return mMap.get(idx).get(step);

    }
}
