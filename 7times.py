x = 7
times = 0
while x <= 7777777:
    tmp = x
    tmplist = list(str(tmp))
    times += tmplist.count("7")
    x += 7 

print(times)

