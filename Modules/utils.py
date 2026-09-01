def square(len):
    return len*len


def cube (len):
    return len*len*len


def max(num_list):
    num = num_list[0]

    for i in num_list:
        if i > num:
            num = i

    return num