
def FIZZBUZZ(n):
    for i in n:
        if i == 0:
            continue
        if i % 3 == 0:
            if i % 5 == 0:
                print("FIZZBUZZ")
            else:
                print("FIZZ")
        elif i % 5 == 0:
            print("BUZZ")
        else:
            print(i)



FIZZBUZZ(range(1, 16))


