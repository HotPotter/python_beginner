class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def removeDuplicates(self,head):
        if head == None:
            return None
        if head.next == None:
            return head
        else:
            cur = head
            while cur.next:
                if cur.data == cur.next.data:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            return head

            # cur_list=[]
            # no_dup = []
            # current = head
            # while current:
            #     cur_list.append(current.data)
            #     current = current.next
            # for i in cur_list:
            #     if i not in no_dup:
            #         no_dup.append(i)








mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);