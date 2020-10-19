def bigAdd(num1:str,num2:str):
    A = list(map(lambda x:int(x),list(num1)))
    B = list(map(lambda x:int(x),list(num2)))
    length = len(A)+1 if len(A) > len(B) else len(B)+1
    result = [0 for _ in range(length)]
    index = len(result) - 1
    while len(A) > 0 and len(B) > 0:
        result[index] += A.pop() + B.pop()
        if result[index] >= 10:
            result[index-1] = result[index] //10
            result[index] = result[index] % 10
        index -= 1
    while len(A) > 0 :
        result[index] = A.pop()
        index -= 1
    while len(B) > 0:
        result[index] = B.pop()
        index -= 1

    return result[1:] if result[0] == 0 else result


if __name__ == "__main__":
    # bigAdd("123","456")
    # A= [1,2,3]
    # print(A.pop())
    # print(999 + 999)
    print(bigAdd("999","999"))
    print(999 + 999)