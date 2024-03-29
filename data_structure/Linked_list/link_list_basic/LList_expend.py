class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


# 基于节点类LNode定义一个单链表对象的类
class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return None
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def traverse(self):
        p = self._head
        while p:
            yield p.elem
            p = p.next

    def find(self, value):
        p = self._head
        while p is not None:
            if value == p.elem:
                return p.elem
            p = p.next
        else:
            raise LinkedListUnderflow("no item")

    def length(self):
        p, n = self._head, 0
        while p is not None:
            n += 1
            p = p.next
        return n

    def pop_head(self):
        if self._head is None:
            # 无节点引发异常
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def pop_tail(self):
        if self._head is None:  # 空表
            raise LinkedListUnderflow("in pop last")
        p = self._head
        if p.next is None:  # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is None:
                print(',', end='')
            p = p.next
        print('')

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next


class LListExpend(LList):

    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self,elem):
        # self._head = LNode(elem,self._head)
        # if self._rear is None:
        #     self._rear = self._head
        if self._head is None:
            self._head  = LNode(elem,self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem,self._head)

    def append(self,elem):
        if self._head is None:
            self._head = LNode(elem,self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:          # 空表
            raise LinkedListUnderflow("in pop List")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e
















