class MyBitmap():

    def __init__(self,size):
        self.size = size
        self.words = [0 for _ in range(self.getWordIndex(size-1)+1)]
    
    def printBitMap(self):
        print("size:",self.size)
        print("words:",self.words)

    def getWordIndex(self,bitIndex:int):
        return bitIndex >> 6
    

    def getBit(self,bitIndex:int)->None:
        if bitIndex < 0 or bitIndex > (self.size - 1):
            raise Exception("超过BitMap有效范围")
        wordIndex:int = self.getWordIndex(bitIndex)
        return (self.words[wordIndex] & (1 << bitIndex)) !=0

    def setBit(self,bitIndex:int):
        if bitIndex <0 or bitIndex > (self.size - 1):
            raise Exception("超过Bitmap有效范围")
    
        wordIndex:int = self.getWordIndex(bitIndex)
        self.words[wordIndex] |= (1<<bitIndex)

if __name__ == "__main__":

    bitmap = MyBitmap(128)
    bitmap.setBit(126)
    bitmap.setBit(75)

    print(bitmap.getBit(126))
    print(bitmap.getBit(78))
    
