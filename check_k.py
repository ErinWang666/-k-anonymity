def check_k(same_person_multi, k):
    for i in range(len(same_person_multi)):
        if len(same_person_multi[i]) < k:
            return False
    return True