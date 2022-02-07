package com.leo.leetcode.algorithm.q0800;

import java.util.List;

import com.leo.utils.LCUtil;

/**
 * 有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。
 * 在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 
 * 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。最初，除 0 号房间外的其余所有房间都被锁住。
 * 你可以自由地在房间之间来回走动。
 * 如果能进入每个房间返回 true，否则返回 false。
 * 提示：
 *      1 <= rooms.length <= 1000
 *      0 <= rooms[i].length <= 1000
 *      所有房间中的钥匙数量总计不超过 3000。
 * 链接：https://leetcode-cn.com/problems/keys-and-rooms
 */
public class Q841 {

    public static void main(String[] args) {
        System.out.println(new Q841().canVisitAllRooms(LCUtil.stringToListListInt("[[1],[2],[3],[]]"))); // true
        System.out.println(new Q841().canVisitAllRooms(LCUtil.stringToListListInt("[[1,3],[3,0,1],[2],[0]]"))); // false
        System.out.println(new Q841().canVisitAllRooms(LCUtil.stringToListListInt("[[0]]"))); // true
        System.out.println(new Q841().canVisitAllRooms(LCUtil.stringToListListInt("[[1],[]]"))); // true
        System.out.println(new Q841().canVisitAllRooms(LCUtil.stringToListListInt("[[],[]]"))); // false
    }

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] mark = new boolean[rooms.size()];
        mark[0] = true;
        return walk(rooms, 0, mark) + 1 == rooms.size();
    }

    int walk(List<List<Integer>> rooms, int index, boolean[] mark) {
        List<Integer> room = rooms.get(index);
        int ret = 0;
        for (int k : room) {
            if (!mark[k]) {
                mark[k] = true;
                ret += 1 + walk(rooms, k, mark);
            }
        }
        return ret;
    }
}