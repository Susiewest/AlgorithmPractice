
import operator
T = int(input())
for i in range(T):
    num_sum = int(input())
    data = input()
    data = data.split()
    data = [int(i) for i in data]
    count_chart = {}
    for i in data:
        if i in count_chart:
            count_chart[i] += 1
        else:
            count_chart[i] = 1
    # count_chart = sorted(count_chart.items(), key = operator.itemgetter(1))
    # result = 0
    # for i in range(len(count_chart)):
    #     if count_chart[i][1] == 1:
    #         result = count_chart[i][0]
    #         break
    # if result:
    #     print(result)
    # else:
    #     print(-1)
    result = -1
    data.sort()
    for num in data:
        if count_chart[num] == 1:
            result = num
            break
    print(result)
