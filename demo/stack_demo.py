from datakit.stack import InitStack

#create stack_object
stack_obj = InitStack(10)

#print stack size
print('Stack Size is ',stack_obj.get_stack_size())

#insert into stack
stack_obj.push(100)
stack_obj.push(200)
stack_obj.push(300)
stack_obj.push(400)
stack_obj.push(5005)

print(stack_obj.get_stack_size())
print(stack_obj.get_top())
stack_obj.print_stack()

x = InitStack.stack_from_list([1,2,3,4])
x.print_stack()