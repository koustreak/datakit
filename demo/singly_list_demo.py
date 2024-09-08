from datakit import SinglyList
from datakit import Node

singlylist = SinglyList.InitSinglyList()
print(singlylist.gethead())
print(singlylist.getsize())
singlylist.insert_front(Node.SinglyNode(100))
singlylist.insert_rear(Node.SinglyNode(103))
singlylist.insert_middle(1,Node.SinglyNode(200))
singlylist.insert_middle(2,Node.SinglyNode(300))
singlylist.insert_middle(4,Node.SinglyNode(400))
singlylist.pprint()
# check for delete
singlylist.delete_front()
singlylist.delete_rear()
singlylist.pprint()
singlylist.delete_middle(2)
singlylist.pprint()
'''
singlylist.pprint()
print(singlylist.gethead().getdata())
print(singlylist.getsize())
singlylist.insert_middle(0,Node.SinglyNode(105))
print(singlylist.getsize())
singlylist.pprint()
singlylist.update_by_value(103,1033)
singlylist.pprint()
singlylist.update_by_pos(3,10000)
singlylist.pprint()
singlylist.delete_front()
singlylist.pprint()
singlylist.delete_rear()
singlylist.pprint()
print('*****************')
singlylist.insert_front(Node.SinglyNode(500))
singlylist.insert_front(Node.SinglyNode(501))
#singlylist.delete_middle(1)
#singlylist.pprint()
print(singlylist.gethead().getdata())
pp = singlylist.reversed()
print('*******************')
pp.pprint()
ll = [1,2,3,4,5]
new_list = SinglyList.InitSinglyList.from_list(ll)
print(new_list.gethead().getdata())
print(new_list.getsize())
print(new_list.getmax())
print(new_list.getmin())
print(new_list.getavg())
'''