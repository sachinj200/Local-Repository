for i in range(1,7):
    if i == 3:
        continue
    print(f"{i} * {i} = {i*i} ")

even_list =[]
for i in range(0,11):
    if i % 2 == 0 :
        even_list.append(i)
print(even_list)

print (f" Sachin has created an even number list. {even_list}")



