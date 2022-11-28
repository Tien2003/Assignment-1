def list_number(list1, list2, n1, n2):
    s = []
    for i in range(0, n1):
        if list1[i] % 2 != 0:
            s.append(list1[i])
    for i in range(0, n2):
        if list2[i] % 2 ==0:
            s.append(list2[i])
    return s


n1 = int(input("Enter number of elements list 1"))
n2 = int(input("Enter number of elements list 2"))

list1 = []
list2 = []
for i in range(0, n1):
    list1.append(int(input()))
for i in range(0, n2):
    list2.append(int(input()))

print(list_number(list1, list2, n1, n2))

print("List 1: ", list1)
print("List 2: ", list2)
