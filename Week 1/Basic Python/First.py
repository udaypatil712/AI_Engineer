n = 5

for i in range(n):
    star = ""
    for j in range(n-i-1):
        star += "  " 
    for j in range(i):
        star += "* "
    print(star)


    