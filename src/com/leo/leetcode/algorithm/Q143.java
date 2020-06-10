package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import com.leo.utils.ListNode;
import org.junit.Test;

import java.util.HashMap;
import java.util.Map;

public class Q143 {
    @Test
    public void TestOJ() {
        ListNode l = LCUtil.stringToListNode("[1,2,3,4]");
        reorderList(l);
        System.out.println(LCUtil.listNodeToString(l)); // [1,4,2,3]
        l = LCUtil.stringToListNode("[1,2,3,4,5]");
        reorderList(l);
        System.out.println(LCUtil.listNodeToString(l)); // [1,5,2,4,3]
    }

    /**
     * L0→Ln→L1→Ln-1→L2→Ln-2
     */
    public void reorderList(ListNode head) {
        if (head == null) return;
        Map<Integer, ListNode> m = new HashMap<>();
        ListNode p = head;
        int count = 0;
        while (p != null) {
            m.put(count, p);
            count++;
            p = p.next;
        }
        for (int i = 0; i < count; i++) {
            if (i < count / 2) {
                m.get(i).next = m.get(count - 1 - i);
            } else {
                m.get(i).next = m.get(count - 1 - i + 1);
            }
        }
        m.get(count / 2).next = null;
    }

}
