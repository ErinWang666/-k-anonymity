def generalizing(not_k_position, nearest_person_position, same_person, same_person_multi, same_value):
    not_k_person = same_person[not_k_position]
    not_k_multi = same_person_multi[not_k_position]
    nearest_person = same_person[nearest_person_position]
    nearest_person_multi = same_person_multi[nearest_person_position]

    ###000
    age_d = {
        '1*': 4, '2*': 4, '3*': 4, '4*': 4, '5*': 4, '6*': 4, '7*': 4, '8*': 4, '9*': 4,
        'below_29': 3, 'between_30_49': 3, 'between_50_69': 3, 'above_70': 3,
        'below_49': 2, 'above_50': 2,
        '*': 1}
    age_generalization = {
        '1*': 'below_29', '2*': 'below_29',
        '3*': 'between_30_49', '4*': 'between_30_49',
        '5*': 'between_50_69', '6*': 'between_50_69',
        '7*': 'above_70', '8*': 'above_70', '9*': 'above_70',
        'below_29': 'below_49', 'between_30_49': 'below_49',
        'between_50_69': 'above_50', 'above_70': 'above_50',
        'below_49': '*', 'above_50': '*'}

    ###111
    workclass_d = {
        'Without-pay': 3, 'Never-worked': 3, 'Federal-gov': 3, 'Local-gov': 3, 'State-gov': 3, 'Private': 3,
        'Self-emp-not-inc': 3, 'Self-emp-inc': 3,
        'no_work': 2, 'in_system': 2, 'outside_system': 2,
        '*': 1}
    workclass_generalization = {
        'Without-pay': 'no_work', 'Never-worked': 'no_work',
        'Federal-gov': 'in_system', 'Local-gov': 'in_system', 'State-gov': 'in_system',
        'Private': 'outside_system', 'Self-emp-not-inc': 'outside_system', 'Self-emp-inc': 'outside_system',
        'no_work': '*', 'in_system': '*', 'outside_system': '*'}

    ###222
    education_d = {
        '9th': 4, '7th-8th': 4, '1st-4th': 4, '5th-6th': 4, 'Preschool': 4, '11th': 4, 'HS-grad': 4, '12th': 4,
        '10th': 4, 'Bachelors': 4, 'Some-college': 4, 'Prof-school': 4, 'Assoc-acdm': 4, 'Assoc-voc': 4, 'Masters': 4,
        'Doctorate': 4,
        'below_high_school': 3, 'high_school': 3, 'college': 3, 'graduate': 3,
        'below_college': 2, 'above_college': 2,
        '*': 1}
    education_generalization = {
        '9th': 'below_high_school', '7th-8th': 'below_high_school', '1st-4th': 'below_high_school',
        '5th-6th': 'below_high_school', 'Preschool': 'below_high_school',
        '11th': 'high_school', 'HS-grad': 'high_school', '12th': 'high_school', '10th': 'high_school',
        'Bachelors': 'college', 'Some-college': 'college', 'Prof-school': 'college', 'Assoc-acdm': 'college',
        'Assoc-voc': 'college',
        'Masters': 'graduate', 'Doctorate': 'graduate',
        'below_high_school': 'below_college', 'high_school': 'below_college',
        'college': 'above_college', 'graduate': 'above_college',
        'below_college': '*', 'above_college': '*'}

    ###333
    marital_status_d = {
        'Divorced': 3, 'Never-married': 3, 'Widowed': 3, 'Married-civ-spouse': 3, 'Separated': 3,
        'Married-spouse-absent': 3, 'Married-AF-spouse': 3,
        'single': 2, 'not_single': 2,
        '*': 1}
    marital_status_generalization = {
        'Divorced': 'single', 'Never-married': 'single', 'Widowed': 'single',
        'Married-civ-spouse': 'not_single', 'Separated': 'not_single', 'Married-spouse-absent': 'not_single',
        'Married-AF-spouse': 'not_single',
        'single': '*', 'not_single': '*'}

    ###444
    occupation_d = {
        'Farming-fishing': 3, 'Machine-op-inspct': 3, 'Transport-moving': 3, 'Tech-support': 3, 'Craft-repair': 3,
        'Other-service': 3, 'Sales': 3, 'Exec-managerial': 3, 'Prof-specialty': 3, 'Handlers-cleaners': 3,
        'Adm-clerical': 3, 'Priv-house-serv': 3, 'Protective-serv': 3, 'Armed-Forces': 3,
        'primary_sector': 2, 'secondary_sector': 2, 'tertiary_industry': 2,
        '*': 1}
    occupation_generalization = {
        'Farming-fishing': 'primary_sector',
        'Machine-op-inspct': 'secondary_sector', 'Transport-moving': 'secondary_sector',
        'Tech-support': 'tertiary_industry', 'Craft-repair': 'tertiary_industry', 'Other-service': 'tertiary_industry',
        'Sales': 'tertiary_industry', 'Exec-managerial': 'tertiary_industry', 'Prof-specialty': 'tertiary_industry',
        'Handlers-cleaners': 'tertiary_industry', 'Adm-clerical': 'tertiary_industry',
        'Priv-house-serv': 'tertiary_industry', 'Protective-serv': 'tertiary_industry',
        'Armed-Forces': 'tertiary_industry',
        'primary_sector': '*', 'secondary_sector': '*', 'tertiary_industry': '*'}

    ###555
    native_country_d = {
        'Cambodia': 4, 'India': 4, 'Japan': 4, 'China': 4, 'Iran': 4, 'Philippines': 4, 'Vietnam': 4, 'Laos': 4,
        'Taiwan': 4, 'Thailand': 4, 'Hong': 4, 'England': 4, 'Germany': 4, 'Greece': 4, 'Italy': 4, 'Poland': 4,
        'Portugal': 4, 'Ireland': 4, 'France': 4, 'Hungary': 4, 'Scotland': 4, 'Yugoslavia': 4, 'Holand-Netherlands': 4,
        'United-States': 4, 'Puerto-Rico': 4, 'Canada': 4, 'Outlying-US(Guam-USVI-etc)': 4, 'Cuba': 4, 'Honduras': 4,
        'Jamaica': 4, 'Mexico': 4, 'Dominican-Republic': 4, 'Ecuador': 4, 'Haiti': 4, 'Columbia': 4, 'Guatemala': 4,
        'Nicaragua': 4, 'El-Salvador': 4, 'Trinadad&Tobago': 4, 'Peru': 4, 'South': 4,
        'asia': 3, 'europe': 3, 'america': 3, 'oceania': 3,
        'asia_oce': 2, 'eur_ame': 2,
        '*': 1}
    native_country_generalization = {
        'Cambodia': 'asia', 'India': 'asia', 'Japan': 'asia', 'China': 'asia', 'Iran': 'asia', 'Philippines': 'asia',
        'Vietnam': 'asia', 'Laos': 'asia', 'Taiwan': 'asia', 'Thailand': 'asia', 'Hong': 'asia',
        'England': 'europe', 'Germany': 'europe', 'Greece': 'europe', 'Italy': 'europe', 'Poland': 'europe',
        'Portugal': 'europe', 'Ireland': 'europe', 'France': 'europe', 'Hungary': 'europe', 'Scotland': 'europe',
        'Yugoslavia': 'europe', 'Holand-Netherlands': 'europe',
        'United-States': 'america', 'Puerto-Rico': 'america', 'Canada': 'america',
        'Outlying-US(Guam-USVI-etc)': 'america', 'Cuba': 'america', 'Honduras': 'america', 'Jamaica': 'america',
        'Mexico': 'america', 'Dominican-Republic': 'america', 'Ecuador': 'america', 'Haiti': 'america',
        'Columbia': 'america', 'Guatemala': 'america', 'Nicaragua': 'america', 'El-Salvador': 'america',
        'Trinadad&Tobago': 'america', 'Peru': 'america',
        'South': 'oceania',
        'asia': 'asia_oce', 'europe': 'asia_oce',
        'america': 'eur_ame', 'oceania': 'eur_ame',
        'eur_ame': '*', 'asia_oce': '*'}

    ###############
    c_distortion = []
    ###############
    for i in range(len(not_k_person)):
        c1 = not_k_person[i]
        c2 = nearest_person[i]
        # print(f'c1 = {c1}')
        # print(f'c2 = {c2}')
        if i == 0:
            c1_status = age_d[c1]
            c2_status = age_d[c2]
            # print(f'c1_status = {c1_status}')
            # print(f'c2_status = {c2_status}')
            c1_upper = c1
            c2_upper = c2
            c1_upper_status = c1_status
            c2_upper_status = c2_status
            while c1_upper != c2_upper:
                # print(f'c1_upper = {c1_upper}')
                # print(f'c2_upper = {c2_upper}')
                # print(f'c1_upper_status = {c1_upper_status}')
                # print(f'c2_upper_status = {c2_upper_status}')
                if c1_upper_status == c2_upper_status and c1_upper != c2_upper:
                    c1_upper = age_generalization[c1_upper]
                    c2_upper = age_generalization[c2_upper]
                    c1_upper_status = age_d[c1_upper]
                    c2_upper_status = age_d[c2_upper]
                elif c1_upper_status > c2_upper_status:  # c1低
                    c1_upper = age_generalization[c1_upper]
                    c1_upper_status = age_d[c1_upper]
                elif c1_upper_status < c2_upper_status:  # c2低
                    c2_upper = age_generalization[c2_upper]
                    c2_upper_status = age_d[c2_upper]
            # print(f'c1_upper = {c1_upper}')
            # print(f'c2_upper = {c2_upper}')
            # print(f'c1_upper_status = {c1_upper_status}')
            # print(f'c2_upper_status = {c2_upper_status}')
        elif i == 1:
            c1_status = workclass_d[c1]
            c2_status = workclass_d[c2]
            c1_upper = c1
            c2_upper = c2
            c1_upper_status = c1_status
            c2_upper_status = c2_status
            while c1_upper != c2_upper:
                if c1_upper_status == c2_upper_status:
                    c1_upper = workclass_generalization[c1_upper]
                    c2_upper = workclass_generalization[c2_upper]
                    c1_upper_status = workclass_d[c1_upper]
                    c2_upper_status = workclass_d[c2_upper]
                elif c1_upper_status > c2_upper_status:  # c1低
                    c1_upper = workclass_generalization[c1_upper]
                    c1_upper_status = workclass_d[c1_upper]
                elif c1_upper_status < c2_upper_status:  # c2低
                    c2_upper = workclass_generalization[c2_upper]
                    c2_upper_status = workclass_d[c2_upper]
        elif i == 2:
            c1_status = education_d[c1]
            c2_status = education_d[c2]
            c1_upper = c1
            c2_upper = c2
            c1_upper_status = c1_status
            c2_upper_status = c2_status
            while c1_upper != c2_upper:
                if c1_upper_status == c2_upper_status:
                    c1_upper = education_generalization[c1_upper]
                    c2_upper = education_generalization[c2_upper]
                    c1_upper_status = education_d[c1_upper]
                    c2_upper_status = education_d[c2_upper]
                elif c1_upper_status > c2_upper_status:  # c1低
                    c1_upper = education_generalization[c1_upper]
                    c1_upper_status = education_d[c1_upper]
                elif c1_upper_status < c2_upper_status:  # c2低
                    c2_upper = education_generalization[c2_upper]
                    c2_upper_status = education_d[c2_upper]
        elif i == 3:
            c1_status = marital_status_d[c1]
            c2_status = marital_status_d[c2]
            c1_upper = c1
            c2_upper = c2
            c1_upper_status = c1_status
            c2_upper_status = c2_status
            while c1_upper != c2_upper:
                if c1_upper_status == c2_upper_status:
                    c1_upper = marital_status_generalization[c1_upper]
                    c2_upper = marital_status_generalization[c2_upper]
                    c1_upper_status = marital_status_d[c1_upper]
                    c2_upper_status = marital_status_d[c2_upper]
                elif c1_upper_status > c2_upper_status:  # c1低
                    c1_upper = marital_status_generalization[c1_upper]
                    c1_upper_status = marital_status_d[c1_upper]
                elif c1_upper_status < c2_upper_status:  # c2低
                    c2_upper = marital_status_generalization[c2_upper]
                    c2_upper_status = marital_status_d[c2_upper]
        elif i == 4:
            c1_status = occupation_d[c1]
            c2_status = occupation_d[c2]
            c1_upper = c1
            c2_upper = c2
            c1_upper_status = c1_status
            c2_upper_status = c2_status
            while c1_upper != c2_upper:
                if c1_upper_status == c2_upper_status:
                    c1_upper = occupation_generalization[c1_upper]
                    c2_upper = occupation_generalization[c2_upper]
                    c1_upper_status = occupation_d[c1_upper]
                    c2_upper_status = occupation_d[c2_upper]
                elif c1_upper_status > c2_upper_status:  # c1低
                    c1_upper = occupation_generalization[c1_upper]
                    c1_upper_status = occupation_d[c1_upper]
                elif c1_upper_status < c2_upper_status:  # c2低
                    c2_upper = occupation_generalization[c2_upper]
                    c2_upper_status = occupation_d[c2_upper]
        elif i == 5:
            c1_status = native_country_d[c1]
            c2_status = native_country_d[c2]
            c1_upper = c1
            c2_upper = c2
            c1_upper_status = c1_status
            c2_upper_status = c2_status
            while c1_upper != c2_upper:
                if c1_upper_status == c2_upper_status:
                    c1_upper = native_country_generalization[c1_upper]
                    c2_upper = native_country_generalization[c2_upper]
                    c1_upper_status = native_country_d[c1_upper]
                    c2_upper_status = native_country_d[c2_upper]
                elif c1_upper_status > c2_upper_status:  # c1低
                    c1_upper = native_country_generalization[c1_upper]
                    c1_upper_status = native_country_d[c1_upper]
                elif c1_upper_status < c2_upper_status:  # c2低
                    c2_upper = native_country_generalization[c2_upper]
                    c2_upper_status = native_country_d[c2_upper]
        ###计算WHD
        if i != 5 and i != 6 and i != 7 and i != 9:
            c = [c1, c2]
            c_status = [c1_status, c2_status]
            c_upper_status = [c1_upper_status, c2_upper_status]
            c_whd = []
            for j in range(len(c)):
                if i == 0 or i == 2 or i == 8:  # 4层
                    if c_status[j] == c_upper_status[j]:  # 计算c到泛化集的距离
                        c_whd.append(0)
                    elif c_status[j] == 4:
                        if c_upper_status[j] == 3:
                            c_whd.append(2 / 11)
                        elif c_upper_status[j] == 2:
                            c_whd.append(5 / 11)
                        elif c_upper_status[j] == 1:
                            c_whd.append(1)
                    elif c_status[j] == 3:
                        if c_upper_status[j] == 2:
                            c_whd.append(3 / 11)
                        elif c_upper_status[j] == 1:
                            c_whd.append(9 / 11)
                    elif c_status[j] == 2:
                        if c_upper_status[j] == 1:
                            c_whd.append(6 / 11)

                elif i == 1 or i == 3 or i == 4:  # 3层
                    if c_status[j] == c_upper_status[j]:  # 计算c到泛化集的距离
                        c_whd.append(0)
                    elif c_status[j] == 3:
                        if c_upper_status[j] == 2:
                            c_whd.append(1 / 3)
                        elif c_upper_status[j] == 1:
                            c_whd.append(1)
                    elif c_status[j] == 2:
                        if c_upper_status[j] == 1:
                            c_whd.append(2 / 3)
            c_distortion.append(sum(c_whd))

    nearest_item = c_distortion[0]
    for i in range(len(c_distortion)):#找出区别最小的项
        if c_distortion[i] < nearest_item:
            nearest_item_position = i
            nearest_item = c_distortion[i]

    ###找到泛化集
    c1 = not_k_person[i]
    c2 = nearest_person[i]
    # print(f'c1 = {c1}')
    # print(f'c2 = {c2}')
    if i == 0:
        c1_status = age_d[c1]
        c2_status = age_d[c2]
        # print(f'c1_status = {c1_status}')
        # print(f'c2_status = {c2_status}')
        c1_upper = c1
        c2_upper = c2
        c1_upper_status = c1_status
        c2_upper_status = c2_status
        while c1_upper != c2_upper:
            # print(f'c1_upper = {c1_upper}')
            # print(f'c2_upper = {c2_upper}')
            # print(f'c1_upper_status = {c1_upper_status}')
            # print(f'c2_upper_status = {c2_upper_status}')
            if c1_upper_status == c2_upper_status and c1_upper != c2_upper:
                c1_upper = age_generalization[c1_upper]
                c2_upper = age_generalization[c2_upper]
                c1_upper_status = age_d[c1_upper]
                c2_upper_status = age_d[c2_upper]
            elif c1_upper_status > c2_upper_status:  # c1低
                c1_upper = age_generalization[c1_upper]
                c1_upper_status = age_d[c1_upper]
            elif c1_upper_status < c2_upper_status:  # c2低
                c2_upper = age_generalization[c2_upper]
                c2_upper_status = age_d[c2_upper]
        # print(f'c1_upper = {c1_upper}')
        # print(f'c2_upper = {c2_upper}')
        # print(f'c1_upper_status = {c1_upper_status}')
        # print(f'c2_upper_status = {c2_upper_status}')
    elif i == 1:
        c1_status = workclass_d[c1]
        c2_status = workclass_d[c2]
        c1_upper = c1
        c2_upper = c2
        c1_upper_status = c1_status
        c2_upper_status = c2_status
        while c1_upper != c2_upper:
            if c1_upper_status == c2_upper_status:
                c1_upper = workclass_generalization[c1_upper]
                c2_upper = workclass_generalization[c2_upper]
                c1_upper_status = workclass_d[c1_upper]
                c2_upper_status = workclass_d[c2_upper]
            elif c1_upper_status > c2_upper_status:  # c1低
                c1_upper = workclass_generalization[c1_upper]
                c1_upper_status = workclass_d[c1_upper]
            elif c1_upper_status < c2_upper_status:  # c2低
                c2_upper = workclass_generalization[c2_upper]
                c2_upper_status = workclass_d[c2_upper]
    elif i == 2:
        c1_status = education_d[c1]
        c2_status = education_d[c2]
        c1_upper = c1
        c2_upper = c2
        c1_upper_status = c1_status
        c2_upper_status = c2_status
        while c1_upper != c2_upper:
            if c1_upper_status == c2_upper_status:
                c1_upper = education_generalization[c1_upper]
                c2_upper = education_generalization[c2_upper]
                c1_upper_status = education_d[c1_upper]
                c2_upper_status = education_d[c2_upper]
            elif c1_upper_status > c2_upper_status:  # c1低
                c1_upper = education_generalization[c1_upper]
                c1_upper_status = education_d[c1_upper]
            elif c1_upper_status < c2_upper_status:  # c2低
                c2_upper = education_generalization[c2_upper]
                c2_upper_status = education_d[c2_upper]
    elif i == 3:
        c1_status = marital_status_d[c1]
        c2_status = marital_status_d[c2]
        c1_upper = c1
        c2_upper = c2
        c1_upper_status = c1_status
        c2_upper_status = c2_status
        while c1_upper != c2_upper:
            if c1_upper_status == c2_upper_status:
                c1_upper = marital_status_generalization[c1_upper]
                c2_upper = marital_status_generalization[c2_upper]
                c1_upper_status = marital_status_d[c1_upper]
                c2_upper_status = marital_status_d[c2_upper]
            elif c1_upper_status > c2_upper_status:  # c1低
                c1_upper = marital_status_generalization[c1_upper]
                c1_upper_status = marital_status_d[c1_upper]
            elif c1_upper_status < c2_upper_status:  # c2低
                c2_upper = marital_status_generalization[c2_upper]
                c2_upper_status = marital_status_d[c2_upper]
    elif i == 4:
        c1_status = occupation_d[c1]
        c2_status = occupation_d[c2]
        c1_upper = c1
        c2_upper = c2
        c1_upper_status = c1_status
        c2_upper_status = c2_status
        while c1_upper != c2_upper:
            if c1_upper_status == c2_upper_status:
                c1_upper = occupation_generalization[c1_upper]
                c2_upper = occupation_generalization[c2_upper]
                c1_upper_status = occupation_d[c1_upper]
                c2_upper_status = occupation_d[c2_upper]
            elif c1_upper_status > c2_upper_status:  # c1低
                c1_upper = occupation_generalization[c1_upper]
                c1_upper_status = occupation_d[c1_upper]
            elif c1_upper_status < c2_upper_status:  # c2低
                c2_upper = occupation_generalization[c2_upper]
                c2_upper_status = occupation_d[c2_upper]
    elif i == 5:
        c1_status = native_country_d[c1]
        c2_status = native_country_d[c2]
        c1_upper = c1
        c2_upper = c2
        c1_upper_status = c1_status
        c2_upper_status = c2_status
        while c1_upper != c2_upper:
            if c1_upper_status == c2_upper_status:
                c1_upper = native_country_generalization[c1_upper]
                c2_upper = native_country_generalization[c2_upper]
                c1_upper_status = native_country_d[c1_upper]
                c2_upper_status = native_country_d[c2_upper]
            elif c1_upper_status > c2_upper_status:  # c1低
                c1_upper = native_country_generalization[c1_upper]
                c1_upper_status = native_country_d[c1_upper]
            elif c1_upper_status < c2_upper_status:  # c2低
                c2_upper = native_country_generalization[c2_upper]
                c2_upper_status = native_country_d[c2_upper]

    nearest_person[i] = c2_upper
    same_person[nearest_person_position] = nearest_person
    same_value[nearest_person_position] += same_value[not_k_position]
    if i != 5:
        for j in range(len(not_k_multi)):
            not_k_multi[j][i] = c1_upper
        for j in range(len(nearest_person_multi)):
            nearest_person_multi[j][i] = c2_upper
    elif i == 5:
        for j in range(len(not_k_multi)):
            not_k_multi[j][8] = c1_upper
        for j in range(len(nearest_person_multi)):
            nearest_person_multi[j][8] = c2_upper
    for j in range(len(not_k_multi)):
        nearest_person_multi.append(not_k_multi[j])
    del same_person[not_k_position]
    del same_person_multi[not_k_position]
    del same_value[not_k_position]

    same_modify = [same_person, same_person_multi, same_value]
    return same_modify