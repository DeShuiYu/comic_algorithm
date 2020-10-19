

def isPowerOf2(num:int)->bool:
    return True if num &(num -1) == 0 else False

if __name__ == "__main__":
    print(isPowerOf2(8))
    print(isPowerOf2(16))
    print(isPowerOf2(9))