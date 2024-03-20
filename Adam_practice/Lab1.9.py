def number_decomposition(num):
    arr_simple = [1,2]
    arr_complex = []
    for i in range(3,num+1):
        if is_simple(i):
            arr_simple.append(i)

    for i in (arr_simple):
        if num % i == 0:
            arr_complex.append(i)


    return arr_complex

def is_simple(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

print(number_decomposition(456))