
def count_substring(str_x):
    cnt = 0
    for i in range(0, len(str_x)):
        if str_x[i: i+4] == "Emma":
            cnt += 1
    return cnt

str = "Emma is good developer. Emma is a writer"
print(count_substring(str))

#print(str.count("Emma"))
