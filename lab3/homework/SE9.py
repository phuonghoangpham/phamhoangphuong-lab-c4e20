def get_even_list(l):
    even_list = []
    for n in l:
        if n % 2 == 0:
            even_list.append(n)
    return even_list
print(get_even_list([1,4,5,-1,10]))