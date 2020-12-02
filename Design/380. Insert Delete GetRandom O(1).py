#要在O(1)时间内的插入删除，肯定要利用哈希表的 
#与之相对的要用list保存数据，因为如果用set无法实现随机访问
#常数删除的解决方法是，每次将要删除的元素换到最后一个位置，pop
#也不是换到最后一个位置，把最后一个位置的元素覆盖掉前面要删除的元素，然后把最后一个元素处理掉
#原来删除不一定要删除指定元素，覆盖掉要删除的，再删除覆盖别人的元素也行
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random_set = []
        self.dict_index = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        #if val not in random_set: 在list里找可能不是常数级 要在dict里找
        if val not in self.dict_index:
            self.dict_index[val]=len(self.random_set)
            self.random_set.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict_index:
            last_element, remove_idx = self.random_set[-1], self.dict_index[val]
            #emmmm不用交换其实，把最后一个原本存的放到前面需要删除的元素覆盖掉，后面的直接remove，没必要一定把要删除的元素换到最后
            # self.random_set[-1], self.random_set[remove_idx]= self.random_set(remove_idx), last_element
            # self.dict_index[last_element] = remove_idx
            self.random_set[remove_idx], self.dict_index[last_element] = last_element, remove_idx
            self.random_set.pop()
            del self.dict_index[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.random_set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

执行用时：128 ms, 在所有 Python3 提交中击败了68.60%的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了73.14%的用户
