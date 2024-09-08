from datakit import DoublyList
from datakit import Node

list_obj = DoublyList.InitDoublyList()
print(list_obj.gethead())
print(list_obj.getsize())
## check insert
list_obj.insert_front(Node.DoublyNode(100))
#list_obj.insert_rear(Node.DoublyNode(200))
list_obj.insert_middle(1,Node.DoublyNode(300))
list_obj.pprint()
