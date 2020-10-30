我的第一版写法 超时
先找出一个起点 再从起点开始往后计算，一旦为负[1]，从下一个[2]开始做起点rest置0，用取余来实现循环走，直到rest油>=0且和起点重合才停下
也就是从第一个满足要求的点开始做起点，每个满足要求的起点都要尝试走一圈
[1]很好理解，一个站的收益如果小于0，肯定不能作为起点；而连续的多个站也可以等效地看做一个站，如果其累积收益小于0，就跳过，寻找下一个。
[2]如果A站不能到B站，那么A，B之间到任何一个站都不能到B站（b是第一个不能到的点
A不能到B，假设A、B间有个C可以到达B 那么，A不能到C，否则A可以到B。而B是A第一个不能到达的站点，所以不存在C可到B
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length=len(gas)
        if sum(gas)-sum(cost)<0:
            return -1
        for i in range(length):
            if gas[i]-cost[i]>=0:
                start=i
                break
        rest=gas[start]-cost[start]
        while(start<length):
            for i in range(1,length):
                cur=(start+i)%length
                rest+=gas[cur]-cost[cur]
                if rest>=0 and cur==start:
                    return start
                if rest<0:
                    start=cur+1
                    rest=0
                    break

第二版写法 首先不用特地找一个start出来了，在循环里start自己就更新了，完全的把起步写进了循环里，找start&计算rest初始值都写进去
疑问：第一版想通过while实现，每个新start重新开始新循环，为森么可以取缔
官方题解用了一个反证法，评论区看到一个解释：若sum(gas) >= sum(cost)，则必定存在解 
再加上题目条件若有解则唯一，我们只需找到以i开头的总累计油量有剩余cur_tank + gas[i] - cost[i] >= 0即可——这就是本题贪心策略的依据


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length=len(gas)
        if sum(gas)-sum(cost)<0:
            return -1
        # for i in range(length):
        #     if gas[i]-cost[i]>=0:
        #         start=i
        #         break  
        start,rest=0, 0
        for cur in range(length):
            rest+=gas[cur]-cost[cur]
            if rest<0:
                start=cur+1
                rest=0
        return start
        
执行用时：52 ms, 在所有 Python3 提交中击败了44.92%的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了38.78%的用户
