def bears(n):
    print("bears(" + str(n)+ ")")

    div5 = n % 5 == 0
    div43 = n % 4 == 0 or n % 3 == 0
    div2 = n % 2 == 0

    if n == 42 or n == 42.0:
        #  print("-------- n = 42 -------")
        return True
    elif n < 42:
        #  print("-------- n < 42 --------")
        return False
    else:
        #  print("-------- n > 42 -------")
        if div5:
            bears(n - 42)

        if div43:
            if (n % 10 != 0) and (((n % 100) // 10) != 0):
                bears(n - ((n % 10) * ((n % 100) // 10)))

        if div2:
            bears(n / 2)


        return False








