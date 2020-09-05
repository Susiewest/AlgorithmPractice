#第一版写法 四个测试用例没过
#思路是对的但是对每个数判断的终止条件有点问题 
#首先排除了所有偶数 其次排除了所有被3 5 7 9整除的数
#不对 比如91 3579都不可以整除 但是可以整除13
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3: return 0
        if n==3: return 1
        test_list=[3,5,7,9]
        count=1
        for i in range(3,n):
            prime=True
            if i%2==0: prime=False
            for j in range(len(test_list)):
                if i%test_list[j]==0 and i!=test_list[j]:
                    prime=False
            if prime: count+=1
                    
        return count


#解决方案的思路 对每个小于根号n的数 都拿来做test list（但是写法里舍弃了testlist的存储
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3: return 0
        if n==3: return 1
        prime=[True]*n
        #感觉在很多题里 优化都是把遍历卡在sqrt(n) 有点重要
        for i in range(2,int(sqrt(n))+1):
            for j in range(2*i,n):
                if j%i==0:
                    prime[j]=False
        count=0
        for i in range(2,n):
            if prime[i]: count+=1
        return count
        
 #超时了 第30-31行可以优化 看到别人用c++写的 j每次+i，这样直接跳到倍数标记false 
 #于是我把for循环改写成while了
 class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3: return 0
        if n==3: return 1
        prime=[True]*n
        #感觉在很多题里 优化都是把遍历卡在sqrt(n) 有点重要
        for i in range(2,int(sqrt(n))+1):
            j=2*i
            while(j<n):
                if j%i==0:
                    prime[j]=False
                j+=i
        count=0
        for i in range(2,n):
            if prime[i]: count+=1
        return count
        
'''执行用时：
3004 ms, 在所有 Python3 提交中击败了8.05%的用户
内存消耗：
25.2 MB, 在所有 Python3 提交中击败了81.42%的用户'''
 
