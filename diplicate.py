my_list = [10,20,60,30,20,40,30,60,70,80]
new_list = []
for i in range(len(my_list)):
    if my_list[i] in my_list[i+1:]:
        new_list.append(my_list[i])
print(new_list)