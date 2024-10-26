from datakit import doubly_list
from datakit import node

list_obj = doubly_list.InitDoublyList()
print(list_obj.gethead())
print(list_obj.getsize())
## check insert
list_obj.insert_front(node.DoublyNode(100))
#list_obj.insert_rear(Node.DoublyNode(200))
list_obj.insert_middle(0,node.DoublyNode(300))
list_obj.pprint()
