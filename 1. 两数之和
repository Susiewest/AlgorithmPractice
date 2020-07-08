/*我的天呐 一个世纪没写C++了 基本语法都忘了 vector也不晓得是啥，搜了一下 可以简单的认为，向量是一个能够存放任意类型的动态数组。
增加函数
xx.push_back(x):向量尾部增加一个元素X
删除函数
xx.pop_back(x):删除向量中最后一个元素
xx.clear():清空向量中所有元素
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> output;
        for(int i=0;i<nums.size()-1;i++){
            for(int j=i+1;j<nums.size();j++)
                if(nums[i]+nums[j]==target){
                    output.push_back(i);
                    output.push_back(j);
                }
        
        }
        return output;
    }
};
