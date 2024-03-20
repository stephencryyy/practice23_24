def sort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

lst1 = [4,5,6,72,6,21,51,42,3,2,1,5,6,55,66]
sort(lst1)
print(lst1)