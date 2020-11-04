def fibonaccitreintaycinco(n):
    a, b = 0, 1
    count = 0
    while count < n + 1:
        print(a, end=' ')
        a, b = b, a+b
        count = count + 1
    print()

print(fibonaccitreintaycinco(35))
