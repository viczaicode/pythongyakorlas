def elso():
    n = -1
    i = 1
    ossz = 0

    while n < 0:
        N = int(input("N = "))
        n = N
    for i in range(n):
        i = i + 1
        ossz += i
    print(f"Az első{n}db természetes szám összege:{ossz}")
