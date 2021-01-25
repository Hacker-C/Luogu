class Solution {
public:
    /**
     * @param a: An integer
     * @param b: An integer
     * @return: The sum of a and b 
     */
    int aplusb(int a, int b) {
        // write your code here
        while(b!=0) //判断是否还有进位
        {
        int _a=a^b;  //异或运算
        int _b=(a&b)<<1;//与运算+移位运算
        a=_a;
        b=_b;
        }
    return a;
    }
};