"""
 * 有一个单链表的 head，我们想删除它其中的一个节点 node。
 * 给你一个需要删除的节点 node 。你将 无法访问 第一个节点  head。
 * 链表的所有值都是 唯一的，并且保证给定的节点 node 不是链表中的最后一个节点。
 * 删除给定的节点。注意，删除节点并不是指从内存中删除它。这里的意思是：
 * 1、给定节点的值不应该存在于链表中。
 * 2、链表中的节点数应该减少 1。
 * 3、node 前面的所有值顺序相同。
 * 4、node 后面的所有值顺序相同。
 * 自定义测试：
 * 1、对于输入，你应该提供整个链表 head 和要给出的节点 node。node 不应该是链表的最后一个节点，而应该是链表中的一个实际节点。
 * 2、我们将构建链表，并将节点传递给你的函数。
 * 3、输出将是调用你函数后的整个链表。
 * 提示：
 * 1、链表中节点的数目范围是 [2, 1000]
 * 2、-1000 <= Node.val <= 1000
 * 3、链表中每个节点的值都是 唯一 的
 * 4、需要删除的节点 node 是 链表中的节点 ，且 不是末尾节点
 * 链接：https://leetcode.cn/problems/delete-node-in-a-linked-list/
"""
from typing import List

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def deleteNode(self, node: Optional[ListNode]):
        if node is None or node.next is None: return
        pre, p = node, node.next
        while p:
            pre.val = p.val
            if p.next is None: break
            pre = p
            p = p.next
        pre.next = None
