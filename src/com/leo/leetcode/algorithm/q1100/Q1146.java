package com.leo.leetcode.algorithm.q1100;

import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;

/**
 * 实现支持下列接口的「快照数组」- SnapshotArray：
 * 1、SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
 * 2、void set(index, val) - 会将指定索引 index 处的元素设置为 val。
 * 3、int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
 * 4、int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
 * 提示：
 * 1、1 <= length <= 50000
 * 2、题目最多进行50000 次set，snap，和 get的调用 。
 * 3、0 <= index < length
 * 4、0 <= snap_id < 我们调用 snap() 的总次数
 * 5、0 <= val <= 10^9
 * 链接：https://leetcode-cn.com/problems/snapshot-array
 */
public class Q1146 {

    public static void main(String[] args) {
        SnapshotArray snapshotArr = new SnapshotArray(1);
        snapshotArr.set(0, 15);
        // 0
        System.out.println(snapshotArr.snap());
        // 1
        System.out.println(snapshotArr.snap());
        // 2
        System.out.println(snapshotArr.snap());
        // 15
        System.out.println(snapshotArr.get(0, 2));
        // 3
        System.out.println(snapshotArr.snap());
        // 4
        System.out.println(snapshotArr.snap());
        // 15
        System.out.println(snapshotArr.get(0, 0));
    }

    static class SnapshotArray {
        int snap_id = 0;
        List<TreeMap<Integer, Integer>> dataList;

        public SnapshotArray(int length) {
            dataList = new ArrayList<>();
            while (length-- > 0) dataList.add(new TreeMap<>());
        }

        public void set(int index, int val) {
            dataList.get(index).put(snap_id, val);
        }

        public int snap() {
            return snap_id++;
        }

        public int get(int index, int snap_id) {
            Integer key = dataList.get(index).floorKey(snap_id);
            return null == key ? 0 : dataList.get(index).get(key);
        }
    }
}
