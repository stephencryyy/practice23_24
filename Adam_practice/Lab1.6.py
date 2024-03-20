def mean_salary(filename):
    with open(filename) as f:
        lst1 = ''
        lst2 = ''
        counter = 0
        while True:

            data = f.read(1)
            if data == '-':
                counter += 1
            elif data == '\n':
                counter -= 1
                lst2 += ' '
            elif counter == 0:
                lst1 += data
            elif counter == 1:
                lst2 += data
            if not data:
                break
    lst1, lst2 = lst1.split(sep=' '), lst2.split(sep=' ')
    dic = {lst1[i]: float(lst2[i]) for i in range(len(lst2))}
    for key, value in dic.items():
        print(f'Name of employee: {key}, his salary: {value}')
    sum = 0
    for value in dic.values():
        sum += value
    print(f'num of employers: {len(dic)}\nmean of employers salary: {sum / len(dic)}')

mean_salary('salary.txt')


