str = input("Enter a string")
n = int(input("Enter a number"))


for i in range(n+1, len(str)):
    print(str[i], end="")
