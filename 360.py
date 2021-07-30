# import math
# data = input().split()
# =  [int(i) for i in input().split()]
# input_str = str(input())
# need_move_length, times = 0, 0
# for i in range(len(input_str)-1, -1, -1):
#     if input_str[i] == 'b':
#         need_move_length += 1
#     elif input_str[i] == 'a':
#         times += need_move_length
#         need_move_length *= 2
# print(times)

num = input()
length = len(num)
add = [100, 200, 360, 220]
delete = [120, 350, 200, 320]
dp = [[0]*length for _ in range(length)]
for i in range(length-1, -1, -1):
    for j in range(i+1, length):
        if num[i]==num[j]:
            dp[i][j] = dp[i+1][j-1]
        else:
            add_begin = dp[i+1][j] + add[int(num[i])-1]
            delete_front = dp[i+1][j] + delete[int(num[i])-1]
            add_end = dp[i][j-1] + add[int(num[j])-1]
            delete_after = dp[i][j-1] + delete[int(num[j])-1]
            dp[i][j] = min(add_begin, delete_front, add_end, delete_after)
print(dp[0][-1])
