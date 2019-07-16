import numpy as np

def get_time_of_day(hour):
    if hour < 6:
        return 'Early_Morning'
    elif hour < 10:
        return 'Rush_Hour_Morning'
    elif hour < 15:
        return 'Day'
    elif hour < 19:
        return "Rush_Hour_evening"
    elif hour < 24:
        return "Night"
    else:
        return '?'

def pad_array(a, des_len, pad_val=0):
    num_pad = des_len - len(a)
    if num_pad < 0:
        print('source array too long')
        return a
    for i in range(num_pad):
        a = np.append(a, pad_val)
    return a

def permutation_test(a, b, num_perms=1000):
    count = 0
    union = np.append(a, b)
    diff = np.mean(a) - np.mean(b)
    for i in range(num_perms):
        a_samp = np.random.choice(union, size=len(a))
        b_samp = np.random.choice(union, size=len(b))
        diff2 = np.mean(a_samp) - np.mean(b_samp)
        if diff > 0:
            if diff2 >= diff:
                count += 1
        elif diff <= 0:
            if diff2 <= diff:
                count += 1
    return count/num_perms
