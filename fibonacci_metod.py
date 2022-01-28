def fibonacci(sayi):
    f_liste = [1,1]
    for i in range(2,sayi):
        f_liste.insert(i, (f_liste[i-1] + f_liste[i-2]))
    return f_liste

print(fibonacci(7))