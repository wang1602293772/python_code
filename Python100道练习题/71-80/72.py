#创建一个链表。
# 在 Python 中可以使用类来创建链表。一个链表由多个节点组成，每个节点包括两个部分：数据部分和指针部分。
# 数据部分用来存储节点的数据，指针部分用来指向下一个节点。下面是一个简单的链表节点类：

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 其中，val 表示当前节点的数据，next 表示下一个节点的指针，默认值为 None。
# 创建链表的方法可以有多种，例如手动创建、读取文件等。下面演示手动创建一个简单的链表，包含三个节点，节点的值分别为 1、2 和 3，链表的头节点为第一个节点：

# 创建链表
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
head = node1

# 遍历链表
cur = head
while cur:
    print(cur.val)
    cur = cur.next
# 这段代码首先创建了三个节点，然后将它们依次连接起来，形成一个链表。最后使用一个循环遍历链表，并打印每个节点的值。输出结果为：

# 1
# 2
# 3
# 可以看到，我们成功创建了一个简单的链表，并遍历了链表中的所有节点。