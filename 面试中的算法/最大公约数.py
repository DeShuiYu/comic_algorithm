def getGreatesCommonDivisor(a:int,b:int)-> int:
    big =  a if a>b else b
    small = b if a>b else a

    while 0 != big % small:
        t = big % small
        big = small
        small = t
    return small 


if __name__ == "__main__":
    print(getGreatesCommonDivisor(25,15))
    print(getGreatesCommonDivisor(25,5))
    print(getGreatesCommonDivisor(100,80))
    print(getGreatesCommonDivisor(27,14))
    


