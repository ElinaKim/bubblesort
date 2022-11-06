list1 = [1, 2, 5, 9, 10, 12, 16]
list1[0], list1[1] = list1[1], list1[0]
print(list1)

for num1 in range(len(list1)):
    for num in range(len(list1)-1):
        if list1[num] > list1[num+1]:
            list1[num], list1[num+1] = list1[num+1], list1[num]
        else:
            break

print(list1)