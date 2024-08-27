from datakit import stack
from datakit import stackops

#create stack_object
stack_obj = stack.Init(10)

#print stack size
print(stack_obj.get_stack_size(),'a')

#insert into stack
stack_obj.push(100)
stack_obj.push(200)
stack_obj.push(300)
stack_obj.push(400)
stack_obj.push(500)

#print stack operations
stackops.print_stack(stack_obj)

#get current top
print(stack_obj.get_top())

#pop from stack
stack_obj.pop()
stack_obj.pop()
stack_obj.pop()

print(stack_obj.get_top())
stackops.print_stack(stack_obj)

print(stack_obj._Init__stack)

#fetch max , min , average value
print('min value is ',stackops.get_min(stack_obj))
print('max value is ',stackops.get_max(stack_obj))
print('average value is ',stackops.get_average(stack_obj))
print('+++++++++++++++++++++++++++++++++++++')
print(stack_obj._Init__stack)
#increase stack size
stack_obj.increase_size()
print(stack_obj.get_stack_size())
print('***********************')
print(stack_obj._Init__stack)
stack_obj.pop()
stack_obj.pop()
stackops.print_stack(stack_obj)