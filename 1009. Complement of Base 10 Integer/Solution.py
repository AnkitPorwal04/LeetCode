class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=bin(n)[2:]
        arr=''
        for i in s:
            if i=='0':
                arr+='1'
            else:
                arr+='0' 
        res=0
        for i in range(len(arr)-1,-1,-1):
            res=res+(int(arr[i])* 2**(len(arr)-i-1))
        return res
