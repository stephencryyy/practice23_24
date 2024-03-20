def mode(lst):
    c = list()
    a = list()

    for i in range(len(lst)):
        if lst[i] not in c:
            c.append(lst[i])

    for i in range(len(c)):
        a.append(lst.count(c[i]))

    print(f'num of max element {c[a.index(max(a))]}, max element is {max(a)}')

mode([1,2,3,4,56, 3, 4,5,43,3,3,3,4,5,6,6,6,])