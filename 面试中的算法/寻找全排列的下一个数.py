'''
1. 从后向前查看逆序区域，找到逆序区域的前一位，也就是数字置换的边界
2. 让逆序区域的前一位和逆序区域中大于它的最小的数字交换位置
3. 把原来的逆序区域转为顺序状态。
'''

def findNearestNumber(numbers:list):
    index = findTransferPoint(numbers)

    if 0 == index:
        return None # 已经是最大数，无法在继续加大
    numbersCopy = numbers.copy()
    exchangeHead(numbersCopy,index)

    reverse(numbersCopy,index)

    return numbersCopy


def reverse(num,index):
    i = index
    j = len(num) - 1
    while i < j:
        temp = num[i]
        num[i] = num[j]
        num[j] = temp
        i+=1
        j-=1

def exchangeHead(numbers,index:int):
    head = numbers[index - 1]

    for i in range(len(numbers)-1,0,-1):
        if head < numbers[i]:
            numbers[index - 1] = numbers[i]
            numbers[i] = head
            break

    return numbers

def findTransferPoint(numbers:list):
    for i in range(len(numbers)-1,0,-1):
        if numbers[i] > numbers[i-1]:
            return i
    return 0


def output(numbers):
    for i in numbers:
        print(i,end=" ")
    print()

if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    for i in range(10):
        numbers = findNearestNumber(numbers)
        output(numbers)