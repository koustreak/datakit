from datakit import stack

#create stack_object
stack_obj = stack.InitStack(10)

#print stack size
print('Stack Size is ',stack_obj.get_stack_size(),'a')

#insert into stack
stack_obj.push(100)
stack_obj.push(200)
stack_obj.push(300)
stack_obj.push(400)
stack_obj.push(5005)

print(stack_obj.get_stack_size())
print(stack_obj.get_top())
stack_obj.print_stack()

stack_obj.pop()
stack_obj.pop()
stack_obj.pop()
stack_obj.print_stack()

print('------------------------')
print(stack_obj.get_top())
print(stack_obj.spaces_left())
# need to delete the stack object
del stack_obj