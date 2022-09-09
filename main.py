from distortion import distortion
from count_same_person import count_same_person
from nearest_position import nearest_position
from generalizing import generalizing
from check_k import check_k
from count_same_modify import count_same_modify

each_person = []
with open('adult.data.txt', 'r') as f:
    origin_data = f.readlines()
for i in range(len(origin_data)):#将txt写入，并删除\n，每行以, 分割两个字符串
    origin_data[i] = origin_data[i].rstrip('\n')
    each_person += origin_data[i].split(', ')

age = []
workclass = []
education = []
marital_status = []
occupation = []
relationship = []
race = []
sex = []
native_country = []
income = []
for i in range(len(each_person)):
    if i % 15 == 0:
        if each_person[i] == '?':
            age.append('*')
        else:
            age.append(each_person[i])
    elif i % 15 == 1:
        if each_person[i] == '?':
            workclass.append('*')
        else:
            workclass.append(each_person[i])
    elif i % 15 == 3:
        if each_person[i] == '?':
            education.append('*')
        else:
            education.append(each_person[i])
    elif i % 15 == 5:
        if each_person[i] == '?':
            marital_status.append('*')
        else:
            marital_status.append(each_person[i])
    elif i % 15 == 6:
        if each_person[i] == '?':
            occupation.append('*')
        else:
            occupation.append(each_person[i])
    elif i % 15 == 7:
        if each_person[i] == '?':
            relationship.append('*')
        else:
            relationship.append(each_person[i])
    elif i % 15 == 8:
        if each_person[i] == '?':
            race.append('*')
        else:
            race.append(each_person[i])
    elif i % 15 == 9:
        if each_person[i] == '?':
            sex.append('*')
        else:
            sex.append(each_person[i])
    elif i % 15 == 13:
        if each_person[i] == '?':
            native_country.append('*')
        else:
            native_country.append(each_person[i])
    elif i % 15 == 14:
        if each_person[i] == '?':
            income.append('*')
        else:
            income.append(each_person[i])

for i in range(len(age)):#把age泛化
    if 10 <= int(age[i]) and int(age[i]) < 20:
        age[i] = '1*'
    elif 20 <= int(age[i]) and int(age[i]) < 30:
        age[i] = '2*'
    elif 30 <= int(age[i]) and int(age[i]) < 40:
        age[i] = '3*'
    elif 40 <= int(age[i]) and int(age[i]) < 50:
        age[i] = '4*'
    elif 50 <= int(age[i]) and int(age[i]) < 60:
        age[i] = '5*'
    elif 60 <= int(age[i]) and int(age[i]) < 70:
        age[i] = '6*'
    elif 70 <= int(age[i]) and int(age[i]) < 80:
        age[i] = '7*'
    elif 80 <= int(age[i]) and int(age[i]) < 90:
        age[i] = '8*'
    elif 90 <= int(age[i]) and int(age[i]) < 100:
        age[i] = '9*'

each_person_row = []#每人一个列表，再合成一个大列表
for i in range(len(age)):
    temp_each_person = []
    temp_each_person.append(age[i])
    temp_each_person.append(workclass[i])
    temp_each_person.append(education[i])
    temp_each_person.append(marital_status[i])
    temp_each_person.append(occupation[i])
    temp_each_person.append(relationship[i])
    temp_each_person.append(race[i])
    temp_each_person.append(sex[i])
    temp_each_person.append(native_country[i])
    temp_each_person.append(income[i])
    each_person_row.append(temp_each_person)

k = int(input('请输入k值：'))
same_person = count_same_person(each_person_row, k)[0]
not_k_position = count_same_person(each_person_row, k)[1]#找到不满足k匿名的元组 在列表中的位置
same_person_multi = count_same_person(each_person_row, k)[2]#每人10项
same_value = count_same_person(each_person_row, k)[3]

while not check_k(same_person_multi, k):
    print(f'不满足{k}匿名')
    not_k_person = same_person[not_k_position]#不满足k匿名的元组
    ###计算该元组与其他元组的距离
    c_distortion = []#存放距离
    c_distortion_position = []#存放对应的其他元组的位置
    if not_k_position == 0:#位置在第0个
        for i in range(1, len(same_person)):
            c_distortion_position.append(i)
            c_distortion.append(distortion(not_k_person, same_person[i]))
    elif not_k_position == len(same_person) - 1:#位置在最后一个
        for i in range(0, len(same_person) - 1):
            c_distortion_position.append(i)
            c_distortion.append(distortion(not_k_person, same_person[i]))
    else:
        for i in range(0, not_k_position - 1):
            c_distortion_position.append(i)
            c_distortion.append(distortion(not_k_person, same_person[i]))
        for i in range(not_k_position + 1, len(same_person)):
            c_distortion_position.append(i)
            c_distortion.append(distortion(not_k_person, same_person[i]))

    nearest_person_position = nearest_position(c_distortion, c_distortion_position)
    nearest_person = same_person[nearest_person_position]
    nearest_person_multi = same_person_multi[nearest_person_position]
    not_k_multi = same_person_multi[not_k_position]

    same_modify = generalizing(not_k_position, nearest_person_position, same_person, same_person_multi, same_value)
    same_person = same_modify[0]
    same_person_multi = same_modify[1]
    same_value = same_modify[2]
    not_k_position = count_same_modify(same_value, k)  # 找到不满足k匿名的元组 在列表中的位置

for i in range(len(same_person_multi)):
    print(same_value[i])
    print(same_person[i])
    print(f'{same_person_multi[i]}\n')

if check_k(same_person_multi, k) == True:
    print(f'满足{k}匿名')

