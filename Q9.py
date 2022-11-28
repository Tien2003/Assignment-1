def reverse(num):
    cnt = 0
    length = int(len(num)/2)
    for i in range(0, int(len(num)/2)):
        if num[i] == num[-i-1]:
            cnt += 1
    if cnt == length:
        return True
    else:
        return False

print(reverse(input("Enter a number")))
