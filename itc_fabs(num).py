def itc_fabs(num):
    if num < 0:
        num = - num
    else:
        num = num
    return num


num = float(input())
print(itc_fabs(num))
