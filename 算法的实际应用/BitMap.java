package 算法的实际应用;
public class BitMap{

    static class  MyBitmap{
        private long [] words;
        private int size;

        public MyBitmap(int size){
            this.size = size;
            this.words = new long[(getWordIndex(size-1)+1)];
        }

        
        public  int getWordIndex(int bitIndex){
            return bitIndex >> 6;
        }

        public boolean getBit(int bitIndex){
            if(bitIndex < 0 || bitIndex > size-1){
                throw new IndexOutOfBoundsException("超过Bitmap有效范围");

            }

            int wordIndex = getWordIndex(bitIndex);
            return (words[wordIndex] & (1L << bitIndex)) != 0;
        }

        public void setBit(int bitIndex){
            if(bitIndex <0 || bitIndex > size-1){
                throw new IndexOutOfBoundsException("超过Bitmap有效范围");
            }
            int wordIndex = getWordIndex(bitIndex);
            words[wordIndex] |= (1L << bitIndex);

        }
    }


    public static void main(String[] args) {
        MyBitmap bitMap = new MyBitmap(128);
        bitMap.setBit(126);
        bitMap.setBit(75);

        System.out.println(bitMap.getBit(126));
        System.out.println(bitMap.getBit(78));
    }
}