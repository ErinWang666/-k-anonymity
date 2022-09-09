def count_same_modify(same_value, k):#检查相同有多少，6项
    for i in range(len(same_value)):
        if same_value[i] < k:
            break

    return i

