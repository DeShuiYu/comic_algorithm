'''
在一个无序数组里有99个不重复的正整数，范围是1~100，唯独缺少1个1~100中的整数，如何找出这个缺失的整数？
'''

def findLostNum1(array:list):
    return (1+100)*100/2 - sum(array)

'''
一个无序数组里有若干个正整数，范围是1~100，其中99个整数都出现了偶数次，只有1个整数出现了奇数次，如何
找到这个出现奇数次的整数？
'''
def findLostNum2(array:list):
    num = array[0]
    for i in range(1,len(array)):
        num = num ^ array[i]
    return num


'''
假设一个无序数组里有若干个正整数，范围是1~100，其中有98个整数出现了偶数次
，只有两个整数出现了奇数次，如何找到这2个出现奇数次的整数？
'''
def findLostNum(array:list)->None:
    result = [0,0]
    xorResult = array[0]
    for  i in range(1,len(array)):
        xorResult = xorResult ^ array[i]
    if xorResult == 0:
        return None

    separator = 1
    while 0 == (xorResult & separator):
        separator <<= 1

    for i in range(len(array)):
        if 0 == (array[i] & separator):
            result[0] ^= array[i]

        else:
            result[1] ^= array[i]

    return result

if __name__ == "__main__":
    print(findLostNum([4,1,2,2,5,1,4,3]))
