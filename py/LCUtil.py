import json
from typing import Deque, List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return treeNodeToString(self)

    def __repr__(self):
        return self.__str__()


class ListNode:
    __slots__ = ['val', 'next']

    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return listNodeToString(self)

    def __repr__(self):
        return self.__str__()


def arrayToTreeNode(_input: list[str]) -> Optional[TreeNode]:
    if not _input: return None

    root: TreeNode = TreeNode(int(_input[0]))
    q = Deque()
    q.append(root)

    index: int = 1
    while q:
        node: TreeNode = q.popleft()
        if index == len(_input): break
        item: str = _input[index].strip()
        index += 1
        if "null" != item:
            left_num: int = int(item)
            node.left = TreeNode(left_num)
            q.append(node.left)
        if index == len(_input): break
        item: str = _input[index].strip()
        index += 1
        if "null" != item:
            right_num: int = int(item)
            node.right = TreeNode(right_num)
            q.append(node.right)

    return root


def stringToTreeNode(_input: str) -> Optional[TreeNode]:
    _input = _input.strip()[1:-1]
    if not _input: return None
    return arrayToTreeNode(_input.split(','))


def treeNodeToString(root: TreeNode) -> str:
    if root is None: return "[]"
    ret = []
    q = Deque()
    q.append(root)
    while q:
        node: TreeNode = q.popleft()
        if node is None:
            ret.append("null")
            continue
        ret.append(str(node.val))
        q.append(node.left)
        q.append(node.right)
    for i in range(len(ret) - 1, -1, -1):
        if ret[i] == "null":
            del ret[i]
        else:
            break
    return '[' + ','.join(ret) + ']'


def treeNodeListToString(treeNodeList: List[TreeNode] | None) -> str:
    if treeNodeList is None: return "[]"
    return "[" + ",".join([treeNodeToString(node) for node in treeNodeList]) + "]"


def stringToListNode(_input: str) -> Optional[ListNode]:
    
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for l in json.loads(_input):
        ptr.next = ListNode(int(l))
        ptr = ptr.next
    return dummyRoot.next


def stringToListNodeList(_input: str) -> List[Optional[ListNode]]:
    ret = []
    for l in json.loads(_input):
        ret.append(stringToListNode(str(l)))
    return ret


def listNodeToString(node: Optional[ListNode]) -> str:
    if node is None:
        return "[]"
    ans = []
    while node is not None:
        ans.append(str(node.val))
        node = node.next

    return "[" + ",".join(ans) + "]"


class TestCase:

    def __init__(self, _inputFile: str):
        self.data = []
        with open(_inputFile, 'r') as f:
            for line in f.readlines():
                self.data.append(line.strip())

    def getData(self, lenNum: int = 0) -> str:
        if lenNum >= len(self.data):
            print("lenNum > len(self.data)")
            return ""
        return self.data[lenNum]

    def getDataInt(self, lenNum: int = 0) -> int:
        if lenNum >= len(self.data):
            print("lenNum > len(self.data)")
            return -1
        return int(self.data[lenNum])

    def getDataArray(self, lenNum: int = 0) -> list[str]:
        if lenNum >= len(self.data):
            print("lenNum > len(self.data)")
            return []
        return self.data[lenNum].split(',')

    def getDataIntArray(self, lenNum: int = 0) -> list[int]:
        if lenNum >= len(self.data):
            print("lenNum > len(self.data)")
            return []
        return [int(x) for x in self.data[lenNum][1:-1].split(',')]