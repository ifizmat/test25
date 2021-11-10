#a = input("Type a number: ")
#print("String: {}".format(a))
#a = int(a)
#print("Integer: {}".format(a))
v = []
'''
for i in range(3):
	print(f"Iteration: {i}")
	a = input("Type a number: ")
	a = int(a)
	v.append(a)
'''
#input_list = []
input_list = input("Type numbers with spaces: ").split()
for a in input_list:
	a = int(a)
	v.append(a)
print(f"List: {v}")