num_list = [10,20,30,40,50,60,70,80,90,100]
my_list=[]
for i in range(len(num_list)):
    if num_list[i]<=50:
        my_list.append(num_list[i])
print(my_list)