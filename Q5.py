n = int(input("Enter nunber of elements"))
list_number = []

for i in range(0, n):
    list_number.append(int(input()))

if list_number[0] == list_number[-1]:
    print("True")
else:
    print("False")
