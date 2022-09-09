def count_same_person(each_person_row, k):#检查相同有多少，10项
    temp_row = []
    row_value = []
    each_person_short = []#每人6项
    same_person = []
    for i in range(len(each_person_row)):
        temp_short = []
        for j in range(0, 10):
            if j == 0:
                temp_short.append(each_person_row[i][j])
            elif j == 1:
                temp_short.append(each_person_row[i][j])
            elif j == 2:
                temp_short.append(each_person_row[i][j])
            elif j == 3:
                temp_short.append(each_person_row[i][j])
            elif j == 4:
                temp_short.append(each_person_row[i][j])
            elif j == 8:
                temp_short.append(each_person_row[i][j])
        each_person_short.append(temp_short)
    for i in range(len(each_person_short)):
        temp_same = []
        if each_person_short[i] not in temp_row:
            temp_row.append(each_person_short[i])
            row_value.append(1)
            temp_same.append(each_person_row[i])
            same_person.append(temp_same)
        elif each_person_short[i] in temp_row:
            row_value[temp_row.index(each_person_short[i])] += 1
            temp_same = same_person[temp_row.index(each_person_short[i])]
            temp_same.append(each_person_row[i])
            same_person[temp_row.index(each_person_short[i])] = temp_same

    #print(temp_row)
    #print(row_value)
    for i in range(len(row_value)):
        if row_value[i] < k:
            break
    same_value = [temp_row, i, same_person, row_value]
    return same_value