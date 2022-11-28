def divisible(list_num):
    for i in range(0, len(list_num)):
        if list_num[i] % 5 == 0:
            print(list_num[i])


list_number = [90, 45, 6, 67, 354, 10, 55]
divisible(list_number)
