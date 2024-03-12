class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #return str(int(num1)*int(num2))

        n1,n2 = 0,0
        for i in num1:
            n1 = n1*10 + (ord(i)-48)
        for i in num2:
            n2 = n2*10 + (ord(i)-48)
        return f"{n1*n2}"
