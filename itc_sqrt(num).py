def itc_sqrt(num):
    if (num**0.5)%1==0:
        return num**0.5
    else:
        return -1
    

num=int(input())
print(itc_sqrt(num))
