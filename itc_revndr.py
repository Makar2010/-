def itc_revndr(num):
    ch1= num//100
    ch2= (num%100)//10
    ch3=(num%100)%10
    b=(str(ch3)+str(ch2)+str(ch1))
    num =int(b)
    return num



